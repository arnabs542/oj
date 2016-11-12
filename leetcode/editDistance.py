# -*- encoding:utf-8  -*-

'''
Edit Distance

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character


'''

'''
Solution:Dynamic Programming
    This problem is a variation of Longest Common Subsequence.

    1. We define dp[i][j] to be the edit distance between string
    word1[0...i-1] and word2[0...j-1].
    2. Then we can find the recurrence:

                  |  dp[i-1][j-1],   word1[i-1] == word2[j-1]
        dp[i][j] =|
                  |  min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1,  insert,
                            delete or replace

'''


class Solution:
    # @return an integer

    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        dp = [[m + n for i in range(n + 1)] for j in range(m + 1)]
        dp[0][0] = 0
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # insert,delete or replace
                    dp[i][j] = min(
                        dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

        return dp[m][n]

        # distance = 0
        # while i < m and j < n:
            # if word1[i] == word2[j]:
                # copy
                # i = i + 1
                # j = j + 1
                # continue
            # elif j < n - 1 and word1[i] == word2[j + 1]:
                # insert
                # j = j + 1
                # distance += 1
            # elif i < m - 1 and word1[i + 1] == word2[j]:
                # delete
                # i = i + 1
                # distance += 1
            # else:
                # replace
                # i += 1
                # j += 1
                # distance += 1
        # if i == m:
            # distance += n - j
        # if j == n:
            # distance += m - i
        # return distance

if __name__ == "__main__":
    print(Solution().minDistance("a", "ab"))
    print(Solution().minDistance("acb", "ab"))
    print(Solution().minDistance("plasma", "altruism"))
    print(Solution().minDistance("sea", "eat"))
