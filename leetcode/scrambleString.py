#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
87. Scramble String

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

================================================================================
SOLUTION

The problem is defined recursively, so of course, the solution illustrate
recursive structure.

1. Brute force - depth first search

For every possible split of the two strings, if the split strings are scramble
strings, then they are a match.

Define state as a four tuple of:
    (
    l1: s1 substring left index,
    r1: s1 substring right index,
    l2: s2 substring left index,
    r2: s2 substring right index,
    )

Because we try every possible split, there are n branches.
Time complexity recurrence relation:
T(n) = T(n - 1) + T(n - 2) + ... + T(1)

Complexity:
T(n) = O(2ⁿ)

2. Depth first search - pruning, memoize

At each recursive procedure call, tuple (l2, r2) is determined by (l1, r1) correspondingly.

There are O(n²) combinations of (l1, r1), so, with memoization,
Complexity: O(n²)

Prune with heuristics that scramble strings must have same character occurrence
frequencies.

With pruning, the complexity can be reduced greatly, by how much?

3. Dynamic programming?

When we split s1 into first part and second part. The first part may correspond to
the back part in the s2, because of scramble.
That's why the state transition is not straightforward to build in a bottom up fashion.

Can we prove it's reversal invariant and make use of that?
If it's reversal invariant, then the problem is converted to match s1 against s2 or
reversed s2.
Then the state will move in a deterministic order.

"""


from _decorators import timeit, memoizeFunc as memoize
from collections import Counter

class Solution:

    @timeit
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        result = self._isScrambleDfs(s1, s2)

        print(s1, s2, "=>", result)

        return result

    def _isScrambleDfs(self, s1, s2):
        prefixCounts = [[Counter()], [Counter()]]
        for i, s in enumerate((s1, s2,)):
            for j in range(1, len(s) + 1):
                mapping = Counter(prefixCounts[i][j - 1])
                mapping[s[j - 1]] = mapping.get(s[j - 1], 0) + 1
                prefixCounts[i].append(mapping)

        @memoize
        def dfs(l1, r1, l2, r2):
            if s1[l1:r1+1] == s2[l2:r2+1]: return True
            # check occurrence count
            counter1 = prefixCounts[0][r1+1] - prefixCounts[0][l1]
            counter2 = prefixCounts[1][r2+1] - prefixCounts[1][l2]
            if counter1 != counter2: return False
            for mid in range(l1, r1): # 0
                if dfs(l1, mid, l2, l2 + mid - l1) and dfs(mid + 1, r1, l2 + mid - l1 + 1, r2) or \
                   dfs(l1, mid, r2 - (mid - l1), r2) and dfs(mid + 1, r1, l2, l2 + r1 - mid - 1):
                    return True

            return False
        return dfs(0, len(s1) - 1, 0, len(s2) - 1)


def test():
    solution = Solution()

    assert solution.isScramble("", "")
    assert solution.isScramble("a", "a")
    assert solution.isScramble("aa", "aa")
    assert solution.isScramble("ab", "ab")
    assert solution.isScramble("ab", "ba")
    assert solution.isScramble("abc", "cba")
    assert solution.isScramble("great", "great")
    assert solution.isScramble("great", "rgeat")
    assert solution.isScramble("great", "rgtae")
    assert solution.isScramble("great", "treag")
    assert not solution.isScramble("a", "b")
    assert not solution.isScramble("aa", "ab")
    assert not solution.isScramble("great", "egtra")


    print("self test passed!")

if __name__ == '__main__':
    test()
