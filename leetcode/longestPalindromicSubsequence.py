#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
516. Longest Palindromic Subsequence
Medium

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".

================================================================================
SOLUTION

1. Brute force
Of course not...

2. Dynamic programming

Define state dp[i][j] indicates the longest palindromic subsequence length of
substring s[i:j+1].

Then we have recurrence relation...

Time limit exceeded in Python implementation...

"""

class Solution:

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = self._longestPalindromeSubseqDp(s)

        print(s, result)

        return result

    def _longestPalindromeSubseqDp(self, s):
        n = len(s)
        dp = [[i == j for j in range(n)] for i in range(n)]
        maxLen = min(1, n)
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 + (dp[i + 1][j - 1] if l >= 3 else 0)
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i + 1][j])
                maxLen = max(maxLen, dp[i][j])
        return maxLen

def test():
    solution = Solution()

    s = ""
    assert solution.longestPalindromeSubseq(s) == 0

    s = "a"
    assert solution.longestPalindromeSubseq(s) == 1

    s = "aa"
    assert solution.longestPalindromeSubseq(s) == 2

    s = "ab"
    assert solution.longestPalindromeSubseq(s) == 1

    s = "aab"
    assert solution.longestPalindromeSubseq(s) == 2

    s = "aba"
    assert solution.longestPalindromeSubseq(s) == 3

    s = "bbbab"
    assert solution.longestPalindromeSubseq(s) == 4

    s = "cbbd"
    assert solution.longestPalindromeSubseq(s) == 2

    print("self test passed!")

if __name__ == '__main__':
    test()
