#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
459. Repeated Substring Pattern

Total Accepted: 3287
Total Submissions: 8200
Difficulty: Easy
Contributors: YuhanXu

Given a non-empty string check if it can be constructed by taking a substring of it and
appending multiple copies of the substring together. You may assume the given string consists
of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

==============================================================================================
SOLUTION:
    1. Naive solution: take possible substrings, check eligibility. O(N²)
    2. KMP: Build the Longest Prefix Suffix array, then text length - LPS[-1] would possibly
be the length of substring. O(n). LPS construction procedure takes amortized O(N) time
complexity.
'''

class Solution(object):

    def repeatedSubstringPattern(self, text):
        """
        :type text: str
        :rtype: bool
        """
        return self.repeatedSubstringPatternKMP(text)

    def repeatedSubstringPatternKMP(self, text):
        """
        :type text: str
        :rtype: bool
        """
        if not text:
            return False
        def preprocess(pattern):
            lps = [0] * len(pattern)
            q = 0
            for i in range(1, len(pattern)):
                while q and pattern[q] != pattern[i]:
                    q = lps[q - 1]
                q += pattern[q] == pattern[i]
                lps[i] = q

            return lps

        lps = preprocess(text)

        l = len(text) - lps[-1]
        return text[0:l] == text[l: 2 * l]

def test():
    solution = Solution()
    assert not solution.repeatedSubstringPattern('')
    assert solution.repeatedSubstringPattern('abab')
    assert not solution.repeatedSubstringPattern('aba')
    assert solution.repeatedSubstringPattern('abcabcabcabc')

    print('self test passed')

if __name__ == '__main__':
    test()
