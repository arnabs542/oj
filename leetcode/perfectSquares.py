#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
279. Perfect Squares

Total Accepted: 54552
Total Submissions: 158592
Difficulty: Medium
Contributors: Admin

Given a positive integer n, find the least number of perfect square numbers (for
example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2
because 13 = 4 + 9.
===========================================================================================
SOLUTION:
    1. BFS(breadth-first search)
    2. Dynamic programming
'''

class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.numSquaresBFS(n)

    def numSquaresBFS(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = []
        i = 1
        while i * i <= n:
            squares.insert(0, i * i)
            i += 1

        frontier = {n}
        frontier_new = set()
        visited = set()
        step = 0

        while frontier:
            # print(frontier)
            for state in frontier:
                if not state:
                    print(step, 'perfect squares')
                    return step
                visited.add(state)
                for square in squares:
                    if state < square:
                        continue
                    elif state == square:
                        print(step + 1, 'perfect squares')
                        return step + 1
                    state_new = state - square
                    if state_new not in visited:
                        frontier_new.add(state_new)

            frontier.clear()
            frontier, frontier_new = frontier_new, frontier
            step += 1

        return step

def test():
    solution = Solution()
    assert solution.numSquares(0) == 0
    assert solution.numSquares(1) == 1
    assert solution.numSquares(2) == 2
    assert solution.numSquares(16) == 1
    assert solution.numSquares(12) == 3
    assert solution.numSquares(13) == 2
    assert solution.numSquares(1687) == 4
    assert solution.numSquares(9715) == 3
    assert solution.numSquares(16878932) == 2
    print('self test passed')

if __name__ == '__main__':
    test()
