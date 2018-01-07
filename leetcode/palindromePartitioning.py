#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]

==============================================================================
SOLUTION

A problem of finding all possible partitioning. It can be generally treated
as a graph search problem, solving it with depth first search or bfs.

1. Brute fore - graph search - combination
At each position, make binary decision about whether to partition here.

Define state:
    (
    palindrome substrings: as return,
    index: substring starting index
    )

Complexity

T(n) = 1 + T(n - 1) + 2 + T(n - 2) + ... + n - 1 +  T(1)

Combination subset complexity: O(n2ⁿ)
There are at most 2ⁿ different configurations of partitioning the string.
And for each configuration, it takes O(n) time to check whether it's palindrome.

Worst case is "aaaaaa".

--------------------------------------------------------------------------------
The state transition is kind of straightforward. The real problem is how to
determine whether a substring is palindrome or not.

2. Depth first search optimized with preprocessing a lookup table
Check below dynamic programming.

3. Dynamic Programming

For the last character, find all possible palindrome substring ending here.
Denote the substring ending here begins with i.
Then, f(n) = {p + s[i:n+1] for p in f(i - 1)}, for each i that s[i:n+1] is palindrome.

Complexity: Actually still more than O(N³), upper bound is O(2ⁿ), because the
palindrome set size may be exponential.

One problem is how to find palindrome ending with last character, as this can
degenerate to O(N²).

Build a palindrome table? p[i][j] = 1 indicates substring s[i:j+1] is palindrome.

Complexity: O(2ⁿ-¹) + O(N²)


"""


class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = self._partitionDfs(s)

        print(s, 'result: ', result)

        return result

    def _partitionDfs(self, s):

        isPalindrome = lambda i, j: s[i:j + 1] == s[i:j + 1][::-1]

        def dfs(start: int):
            """
            Returns
            a list of list of palindrome substrings
            """
            if start >= len(s): return [[]] # FATAL base case
            result = []
            for i in range(start, len(s)):
                # is palindrome
                if isPalindrome(start, i):
                    ret = dfs(i + 1)
                    for l in ret:
                        result.append([s[start:i + 1]] + l)
            return result
        return dfs(0)

    # TODO: dynamic programming?

def test():
    solution = Solution()

    assert solution.partition("") == [[]]
    assert solution.partition("a") == [["a"]]
    assert solution.partition("aa") == [["a", "a"], ["aa"]]
    assert solution.partition("aaa") == [['a', 'a', 'a'], ['a', 'aa'], ['aa', 'a'], ['aaa']]
    assert (Solution().partition("aab") == [["a", "a", "b"], ["aa", "b"]])

    print("self test passed!")

if __name__ == "__main__":
    test()

