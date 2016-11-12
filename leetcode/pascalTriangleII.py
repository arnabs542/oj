# -*- encoding:utf-8 -*-

'''
Pascal's Triangle II

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''

'''
Solution:滚动数组

'''


class Solution:
    # @return a list of integers

    def getRow(self, rowIndex):
        row = [1 for i in range(rowIndex + 1)]
        if rowIndex < 0:
            return []
        for i in range(rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j - 1]
        return row

if __name__ == "__main__":
    print(Solution().getRow(5))
