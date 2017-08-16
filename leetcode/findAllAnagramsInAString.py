#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
438. Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will
not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

==============================================================================================
SOLUTION

The approach is straightforward, but the problem is how to represent and verify anagram easily.

1. Naive solution

Complexity: O(NMlogM)

2. State transition: sliding window

For substring problems, apparently all subproblems are overlapping with each other. Thus, we
can't do it in brute force way. To speed up, we want reuse subproblem solutions with state
transition or recurrence relation.

In a linear structure, the technique is sliding window counter. The idea is similar to
'minimum window string' problem.

Maintain a hash table counter of the target string, and an integer `missing` indicating
how many characters not matched yet.

'''

from collections import Counter

class Solution(object):

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # return self._findAnagramsNaive(s, p)
        return self._findAnagramsCache(s, p)

    def _findAnagramsNaive(self, s, p):
        # FIXED: TLE(time limit exceeded), see optimized algorithm below
        result = []
        m = len(p)
        for i, _ in enumerate(s):
            if sorted(s[i:i+m]) == sorted(p):
                result.append(i)
        return result

    def _findAnagramsCache(self, s, p):
        result = []

        counter = Counter(p)
        missing = len(p)

        # print(counter, missing)
        i = 0
        for j, c in enumerate(s):
            # push
            missing -= counter[c] > 0
            counter[c] -= 1

            if j - i == len(p):
                # pop
                missing += counter[s[i]] == 0
                counter[s[i]] += 1
                i += 1

            # print(c, counter, missing)
            # check
            if missing == 0: result.append(i)
        return result


def test():
    solution = Solution()

    # assert solution.findAnagrams("", "") == []
    assert solution.findAnagrams("", "abc") == []
    # assert solution.findAnagrams("abc", "") == []
    assert solution.findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert solution.findAnagrams("abab", "ab") == [0, 1, 2]

    print("self test passed")

if __name__ == '__main__':
    test()
