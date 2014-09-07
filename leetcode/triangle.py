# -*- encoding:utf-8 -*-

'''
Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


'''


class Solution:
    # @param triangle,a list of lists of integers
    # @return an integer

    def minimumTotal(self, triangle):
        n = len(triangle)
        if n == 0:
            return 0
        curr_sum = 0
        min_sum = -1
        idx = [-1 for i in xrange(n)]
        top = -1
        top += 1
        idx[top] = 0
        curr_sum += triangle[top][idx[top]]
        while top >= 0:
            top += 1
            if top >= n:
                if min_sum == -1 or min_sum > curr_sum:
                    min_sum = curr_sum
                top -= 1
                while top >= 1 and idx[top] != idx[top - 1]:
                    curr_sum -= triangle[top][idx[top]]
                    top -= 1
                if top == 0:
                    break
                else:
                    curr_sum -= triangle[top][idx[top]]
                    idx[top] = idx[top - 1] + 1
                    curr_sum += triangle[top][idx[top]]
            else:
                idx[top] = idx[top - 1]
                curr_sum -= triangle[top][idx[top]]
                print curr_sum
        return min_sum

if __name__ == "__main__":
    print Solution().minimumTotal([
                                  [2],
                                  [3, 4],
                                  [6, 5, 7],
                                  [4, 1, 8, 3]
                                  ])
