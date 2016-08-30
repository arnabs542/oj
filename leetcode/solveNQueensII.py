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

'''

import math


class Solution:

    @classmethod
    def check(cls, stack, row, col):
        for i in range(0, row, 1):
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
    def solveNQueen(self, n):
        res = []
        stack = []
        stack.append(0)
        start = 0
        while True:
            sl = len(stack)
            if sl < n:
                # place a new queen
                for i in range(start, n, 1):
                    if Solution.check(stack, len(stack), i):
                        stack.append(i)
                        start = 0
                        break

                # no new queen is placed,backtrack or return
                if sl == len(stack):
                    if sl == 0:
                        return res
                    else:
                        start = stack.pop() + 1
                else:
                    pass

            else:
                res.append(Solution.show(stack, n))
                start = stack.pop() + 1

if __name__ == "__main__":
    res = Solution().solveNQueen(8)
    print("%d solutions" % len(res))
