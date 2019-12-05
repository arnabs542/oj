#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
221. Maximal Square

Total Accepted: 43196
Total Submissions: 165352
Difficulty: Medium
Contributors: Admin

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and
return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.


SOLUTION
================================================================================

1. In a brute-force way.
We need to check m*n points in the matrix, for which
we have to verify the valid square in amortized min(m, n)^2 time complexity,

Complexity: O(M^2N^2min(M,N)^2)

2. 2D Prefix sum optimization

Optimize brute force method by build a 2D prefix sum array,
to check rectangle (x0,y0) and (x0+h, y0+h) form a square in O(1),

Complexity:
O(M^2*N^2).

3. Prefix sum with binary search

It takes O(log(M+N)) to iterate all possible rectangles, if we do
binary search.

Complexity:
O(MNlog(M+N))

4. Dynamic Programming - locally optimal state ending here

Keep track of side length of maximum square with
a bottom-right vetex at (i, j) in the matrix.
Then we have state transition solved in O(1) time complexity.

Complexity: O(MN)

'''

class Solution(object):

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        side_length = [
            [0 for j in range(n + 1)] for i in range(m + 1)]
        length_max = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "0":
                    side_length[i - 1][j - 1] = 0
                    continue
                side_length[i][j] = min(side_length[i - 1][j],
                                        side_length[i][j - 1],
                                        side_length[i - 1][j - 1]) + 1
                # l = min(side_length[i - 1][j] if i else 0,
                        # side_length[i][j - 1] if j else 0)
                # if matrix[i - l - 1][j - l - 1] == '1':
                    # side_length[i][j] = l + 1
                # else:
                    # side_length[i][j] = max(1, l)
                length_max = max(length_max, side_length[i][j])

        print(length_max ** 2)
        return length_max ** 2

def test():
    solution = Solution()
    assert solution.maximalSquare(["1"]) == 1
    assert solution.maximalSquare([
        "10100",
        "10111",
        "11111",
        "10010"]) == 4
    assert solution.maximalSquare([
        "1010",
        "1011",
        "1011",
        "1111"]) == 4
    assert solution.maximalSquare(["00000", "10000", "00000", "00000"]) == 1
    print('self test passed')

if __name__ == '__main__':
    test()
