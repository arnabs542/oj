#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
463. Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0
represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid
is completely surrounded by water, and there is exactly one island (i.e., one or more connected
land cells). The island doesn't have "lakes" (water inside that isn't connected to the water
around the island). One cell is a square with side length 0. The grid is rectangular, width and
height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:

==============================================================================================
SOLUTION

Mathematics in the perimeter: the perimeter is the sum of all edge length contributed by
cells. And a cell 1 contributes m edges, if it has n neighbor cells of 1, where m + n = 4.

For example, then inner cells contribute nothing(4 - 4 = 0).

1. Brute force
Iterate all the cells, and draw statistics with respect to its valid edges that will contribute
to the total perimeter.

'''

class Solution(object):

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = self._islandPerimeter(grid)
        print(result)
        return result

    def _islandPerimeter(self, grid):
        perimeter = 0
        if not grid or not grid[0]: return perimeter
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                numNeighbor1 = 0
                if grid[i][j] != 1: continue
                for p, q in ((i, j - 1), (i - 1, j), (i, j + 1), (i + 1, j)):
                    if not (0 <= p < m and 0 <= q < n): continue
                    numNeighbor1 += grid[p][q]
                # print(i, j, numNeighbor1)
                perimeter += (4 - numNeighbor1)
        return perimeter


def test():
    solution = Solution()

    assert solution.islandPerimeter([]) == 0
    assert solution.islandPerimeter([[1]]) == 4
    assert solution.islandPerimeter([[0, 0, 0]]) == 0
    assert solution.islandPerimeter([[1, 1]]) == 6
    assert solution.islandPerimeter([[0, 1]]) == 4
    assert solution.islandPerimeter([[1], [1], [1], [1]]) == 10
    assert solution.islandPerimeter([[0, 1, 0, 0],
                                     [1, 1, 1, 0],
                                     [0, 1, 0, 0],
                                     [1, 1, 0, 0]]) == 16

    print("self test passed")

if __name__ == '__main__':
    test()
