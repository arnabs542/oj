# -*-coding:utf-8 -*-
'''
14. Longest Common Prefix

Total Accepted: 152227
Total Submissions: 494694
Difficulty: Easy
Contributors: Admin
Write a function to find the longest common prefix string amongst an array of strings.

==============================================================================================
SOLUTION

1. Brute force
Position-wise comparing.
Time complexity: O(NM). where N is the size of collection, and M is the length of the shortest
string.

2. Binary search in string length space/collection size space.

3. Trie tree.

'''


class Solution:
    # @return a string

    def longestCommonPrefix(self, strs):
        if not strs: return ""
        cp = []
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return "".join(cp)
            cp.append(strs[0][i])

        return "".join(cp)

def test():
    print(Solution().longestCommonPrefix(["hell", "hellsf", "hellao"]))

    print("self test passed")

if __name__ == "__main__":
    test()
