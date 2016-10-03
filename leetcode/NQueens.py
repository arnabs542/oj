'''
N-Queens

The n-queens puzzle is the problem of placing n queens on an n*n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
[".Q..",  // Solution 1
"...Q",
"Q...",
"..Q."],

["..Q.",  // Solution 2
 "Q...",
 "...Q",
 ".Q.."]
 ]


Solution:
    @1: BACKTRACK with recursive depth-first search.
    @2: BACKTRACK with STACK implemented DFS.
    @3: Bit manipulation instead of array representation of queens.

'''

import math


class Solution:

    @classmethod
    def check(cls, stack, row, col):
        for i in range(row):
            # colinear or diagonal
            if stack[i] == col or math.fabs(stack[i] - col) == row - i:
                return False

        return True

    @classmethod
    def show(cls, stack, n):
        # print stack
        resl = []
        for i in range(n):
            resl.append("")
            for j in range(n):
                if stack[i] == j:
                    resl[i] = resl[i] + 'Q'
                else:
                    resl[i] = resl[i] + '.'

        return resl

    # @return a list of lists of string
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        solutions = []
        stack = []
        stack.append(0)
        col_candidate_start = 0
        while True:
            # TODO(DONE): decouple the STACK's PUSH and POP operation
            row = len(stack)
            if row < n and col_candidate_start < n:
                # STACK PUSH: place a new queen
                while col_candidate_start < n:
                    if self.check(stack, len(stack), col_candidate_start):
                        stack.append(col_candidate_start)
                        col_candidate_start = 0
                        break
                    else:
                        col_candidate_start += 1

            else:
                # search has met its dead end
                if col_candidate_start >= n:
                    if not row:
                        return solutions
                else:
                    # stack size is the board width, i.e., a solution has been found
                    solutions.append(Solution.show(stack, n))
                # STACK POP
                col_candidate_start = stack.pop() + 1

if __name__ == "__main__":
    result = Solution().solveNQueens(4)
    print('{} queens solution: '.format(4), result)
    result = Solution().solveNQueens(8)
    print('{} queens with {} solutions'.format(8, len(result)))
