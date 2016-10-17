#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

329. Longest Increasing Path in a Matrix

Total Accepted: 23219
Total Submissions: 67914
Difficulty: Hard
Contributors: Admin

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down.
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

'''

class Solution(object):

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        distances = [[-1 for j in range(n)] for i in range(m)]

        distance = 0
        for i in range(m):
            for j in range(n):
                if distances[i][j] == -1:
                    # not explored yet
                    self.DFS((i, j), matrix, distances, (m, n))
                distance = max(distance, distances[i][j])
        print(distances)
        return distance

    def neighbors(self, coordinate, size):
        '''
        A general neighbor coordinate generator.
        For 2D cases, see neighbors2,.
        '''
        steps = (-1, 1,)
        for i in range(len(coordinate)):
            for step in steps:
                neighbor = tuple(map(lambda x: x[1] if x[0] != i else x[
                    1] + step, enumerate(coordinate)))
                if 0 <= neighbor[i] < size[i]:
                    yield neighbor

    def neighbors2(self, coordinate, size):
        (i, j) = coordinate
        if i - 1 >= 0:
            yield (i - 1, j)
        if i + 1 < size[0]:
            yield (i + 1, j)
        if j - 1 >= 0:
            yield (i, j - 1)
        if j + 1 < size[1]:
            yield (i, j + 1)

    def DFS(self, coordinate, matrix, distances, size):
        i0, j0 = coordinate
        distances[i0][j0] = 1  # 0 denotes exploring, -1 for unexplored

        for (i, j) in self.neighbors2(coordinate, size):
            if matrix[i][j] > matrix[i0][j0]:
                if distances[i][j] == -1:
                    # depth-first search
                    self.DFS((i, j), matrix, distances, size)
                # update vertex's state when a neighbor is finished
                distances[i0][j0] = max(distances[i][j] + 1, distances[i0][j0])
        pass
        return distances[i0][j0]

def test():
    solution = Solution()

    assert solution.longestIncreasingPath([]) == 0

    assert solution.longestIncreasingPath([[3, 2, 1]]) == 3

    assert solution.longestIncreasingPath(
        [[9, 9, 4],
         [6, 6, 8],
         [2, 1, 1]]) == 4
    assert solution.longestIncreasingPath([
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1],
    ]
    ) == 4
    assert solution.longestIncreasingPath([
        [3, 6],
        [3, 5],
        [2, 1],
    ]) == 5
    print('self test passed')

if __name__ == '__main__':
    test()
