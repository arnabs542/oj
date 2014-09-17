# -*- encoding:utf-8  -*-

'''
Edit Distance

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character


'''


class Solution:
    # @return an integer

    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        distance = 0
        while i < m and j < n:
            if word1[i] == word2[j]:
                # copy
                i = i + 1
                j = j + 1
                continue
            elif j < n - 1 and word1[i] == word2[j + 1]:
                # insert
                j = j + 1
                distance += 1
            elif i < m - 1 and word1[i + 1] == word2[j]:
                # delete
                i = i + 1
                distance += 1
            else:
                # replace
                i += 1
                j += 1
                distance += 1
        if i == m:
            distance += n - j
        if j == n:
            distance += m - i
        return distance

if __name__ == "__main__":
    print Solution().minDistance("a", "ab")
    print Solution().minDistance("acb", "ab")
