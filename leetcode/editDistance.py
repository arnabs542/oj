# -*- encoding:utf-8  -*-

'''
72. Edit Distance

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

==============================================================================================
SOLUTION

1. Dynamic Programming with backward induction

This problem is a variation of Longest Common Subsequence.

1. We define transition state f[i][j] as the edit distance between string word1[0...i-1] and word2[0...j-1].
2. The recurrence relation is given by:
              |  f[i-1][j-1],   if word1[i-1] == word2[j-1]
    f[i][j] =|
              |  min(f[i][j-1], f[i-1][j], f[i-1][j-1]) + 1 = min(insert, delete or replace)


##############################################################################################
FOLLOW UP
(http://www.geeksforgeeks.org/longest-repeated-subsequence/)

Longest Repeated Subsequence

Given a string, print the longest repeating subseequence such that the two subsequence don’t have same string character at same position, i.e., any i’th character in the two subsequences shouldn’t have the same index in the original string.

Examples:
    Input: str = "aabb"
    Output: "ab"

    Input: str = "aab"
    Output: "a"
    The two subssequence are 'a'(first) and 'a'
    (second). Note that 'b' cannot be considered
    as part of subsequence as it would be at same
    index in both.

==============================================================================================
SOLUTION

This is a modification of Longest Common Subsequence problem.

1. Two dimensional dynamic programming state
The idea is to find the LCS(str, str) where str is the input string with the restriction that
when both the characters are same, they shouldn’t be on the same index in the two strings.

Recurrence relation:
    if (str[i-1] == str[j-1] && i != j)
            dp[i][j] =  1 + dp[i-1][j-1];

    // If characters do not match
    else
        dp[i][j] = max(dp[i][j-1], dp[i-1][j]);

Complexity: O(N²), O(N²)

2. One dimensional dynamic programming state

Define dp[i] as the length of longest common subsequence of inclusive substring str[0...i].

Then dp[i] = dp[j] + 1, if j < i and str[i] == str[j].

For example, given string str="AABEBCDD",
we have table,
  A A B E B C D D
0 0 1 1 1 2 2 2 3

The result is 3, and the sequence can be found by concatenating characters i if corresponding
dp[i] > dp[i-1].

Complexity: O(N²), O(N)

'''

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        result = self._minDistanceDP(word1, word2)
        return result

    def _minDistanceDP(self, word1, word2):
        m = len(word1)
        n = len(word2)
        f = [[m + n for i in range(n + 1)] for j in range(m + 1)]
        f[0][0] = 0
        for i in range(1, m + 1):
            f[i][0] = i
        for j in range(1, n + 1):
            f[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    # insert, delete or replace
                    f[i][j] = min(
                        f[i][j - 1], f[i - 1][j], f[i - 1][j - 1]) + 1

        return f[m][n]


if __name__ == "__main__":
    print(Solution().minDistance("a", "ab"))
    print(Solution().minDistance("acb", "ab"))
    print(Solution().minDistance("plasma", "altruism"))
    print(Solution().minDistance("sea", "eat"))
