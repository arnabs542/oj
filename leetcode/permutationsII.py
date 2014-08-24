# -*-coding:utf-8 -*-
'''
Permutations II

Given a collection of numbers that might contain duplicates, return all
possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
    [1,1,2], [1,2,1], and [2,1,1].
'''


class Solution:
    # @param num,a list of integer
    # @return a list of lists of integers

    def permuteUnique(self, num):
        Solution.res = []
        self.permute(num, 0, len(num) - 1)
        return self.res

    res = []

    def permute(self, num, start=-1, end=-1):
        n = len(num)
        if start == -1:
            start = 0
            end = n - 1

        if start == end:
            self.res.append(list(num))
            # print num
            return num
        for i in range(start, end + 1, 1):
            dup = 0
            for j in range(start, i, 1):
                if num[j] == num[i]:
                    dup = 1
                    break
            if dup == 0:
                num[start], num[i] = num[i], num[start]
                self.permute(num, start + 1, end)
                num[start], num[i] = num[i], num[start]

if __name__ == "__main__":
    print Solution().permuteUnique([1, 1, 2, 2])
    print Solution().permuteUnique([1, 1])
