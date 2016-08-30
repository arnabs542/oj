# -*-coding:utf-8 -*-
'''
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
'''


class Solution:
    # @return a string

    def longestCommonPrefix(self, strs):
        n = len(strs)
        if n == 0:
            return ""
        cp = []
        for i in range(len(strs[0])):
            for j in range(n):
                if i > len(strs[j]) - 1 or strs[0][i] != strs[j][i]:
                    return "".join(cp)
            cp.append(strs[0][i])

        return "".join(cp)

if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["hell", "hellsf", "hellao"]))
