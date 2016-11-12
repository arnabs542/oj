#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
200. Number of Islands

Total Accepted: 71133
Total Submissions: 228454
Difficulty: Medium
Contributors: Admin

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
===============================================================================================
SOLUTION:
    1. A graph problem, such as finding strongly connected components in undirected graph?
    2. union find?
'''

class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        return self.numIslandsBFS(grid)

    def numIslandsBFS(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # TODO(done): breadth-first search algorithm to find connected components
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        visited = set()
        n_islands = 0
        for i0 in range(m):
            for j0 in range(n):
                if grid[i0][j0] != '1' or (i0, j0) in visited:
                    continue
                frontier = [(i0, j0)]
                while frontier:
                    # i, j = state = frontier.pop(0) # BFS
                    i, j = state = frontier.pop()  # DFS
                    print(n_islands, state)
                    visited.add(state)
                    for neighbor in ((i - 1 if i else i, j),
                                     (i + 1 if i < m - 1 else i, j),
                                     (i, j - 1 if j else j),
                                     (i, j + 1 if j < n - 1 else j)):
                        if neighbor not in visited and \
                           grid[neighbor[0]][neighbor[1]] == '1':
                            frontier.append(neighbor)
                    pass
                n_islands += 1
                pass

        print(n_islands, 'islands')
        return n_islands

    def numIslandsUnionFind(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # TODO: union-find?

def test():
    solution = Solution()
    assert solution.numIslands([
        "11110",
        "11010",
        "11000",
        "00000",
    ]) == 1
    assert solution.numIslands([
        "11000",
        "11000",
        "00100",
        "00011",
    ]) == 3
    print('self test passed')

if __name__ == '__main__':
    test()
