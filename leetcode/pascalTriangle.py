# -*- encoding:utf-8 -*-

'''
Pascal's Triangle

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution:
    # @return a list of lists of integers

    def generate(self, numRows):
        triangle = []
        if numRows == 0:
            return []
        triangle.append([1])
        for i in xrange(2, numRows + 1):
            row = [1 for j in xrange(i)]
            for j in xrange(1, i - 1):
                row[j] = triangle[i - 2][j - 1] + triangle[i - 2][j]
            triangle.append(row)

        return triangle

if __name__ == "__main__":
    print Solution().generate(6)
