'''
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n*n chessboard
such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space respectively.

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

==============================================================================================
Solution:
    N-Queens is a typical DYNAMIC GRAPH PROBLEM: BACKTRACKING! For backtracking,
we need to figure out a way to REPRESENT the candidates, to generate all
the possible candidates and ACCEPT those valid and REJECT those invalid. After
rejection, we need to backtrack, RESTORING STATE, and continue searching.

    In this solution, the representation of the candidate is a column VECTOR
"queens", where i = queen[j] is the column index of the queen in row j. Under
this representation, the way to generate all candidates is just like generate
all the permutation of vector [0...n-1].

    The key point to optimize is how to handle diagonal coordinates, which we
can tackle by utilizing ANALYTIC GEOMETRY. For diagonal line like forward slash,
the equation is y = x + k, where (x, y) is the coordinate and k is an constant.
For backward slash like diagonal lines, the equation is y = -x + k, (x, y, k)
are defined the same before. To wrap it up:

    (1) The constant of a column is its index range from 0 to n-1.
    (2) The constant of a back slash line "" is "col + row" or "x + y"
    (3) The constant of a forward slash line "/" is "col - row" or "x - y"
This way we can reject a candidate in O(1) time since we can use three hash tables
or three boolean arrays as the dynamic sets we need.

Takeaway:
    @1: BACKTRACK with recursive depth-first search.
    @2: BACKTRACK with STACK implemented DFS.
    @3: Bit manipulation instead of array representation of queens.

==============================================================================================
RECURSIVE CALL TO ITERATIVE

To convert recursive depth-first search call to iterative, we have two
difference implementations.

The first is to adapt breadth-first search process.
Change the search FRONTIER behaviour from QUEUE to STACK, and the rest
is the same with BREADTH-FIRST SEARCH. We PUSH states into the search
frontier, and pop them out, then explore adjacent vertices(states). In
this way, we are pushing all adjacent vertices at the same time.

The second way is to emulate the recursive call mechanism with STACK. We
gather the state composed of function input parameter, variables used
after recursive call, recursive call return value and store them as STACK
FRAME. Then for each frame, we determine whether to PUSH or POP.

Note that the variables used after recursive call contain necessary
information to backtrack(restore states).

The only difference between two version is whether to push adjacent
vertices(states) at one time or one by one.
'''

import math


class Solution(object):

    @classmethod
    def check(cls, stack, row, col):
        for i in range(row):
            # colinear or diagonal
            if stack[i] == col or math.fabs(stack[i] - col) == row - i:
                return False

        return True

    @classmethod
    def show(cls, queens, n):
        # print stack
        # resl = []
        # n = len(queens)
        # for i in range(n):
            # resl.append("")
            # for j in range(n):
                # if queens[i] == j:
                    # resl[i] = resl[i] + 'Q'
                # else:
                    # resl[i] = resl[i] + '.'

        # return resl
        return ['.' * q + 'Q' + '.' * (n - q - 1) for q in queens]

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        return self.solveNQueensIterative(n)

    def solveNQueensIterative(self, n: int) -> list:
        """
        :type n: int
        :rtype: List[List[str]]
        """

        solutions = []
        stack = []

        columns = [True] * n # col, range is [0, n - 1]
        backward = [True] *2 * n # col + row, range is [0, 2n - 2]
        forward = [True] * 2 * n # col - row, range is [-(n - 1), n - 1]

        # stack.append(0)
        # columns[0] = False
        # backward[0] = False
        # forward[0] = False

        row = col = 0

        while True:
            # TODO(DONE): decouple the STACK's PUSH and POP operation
            row = len(stack)
            if row < n and col < n:
                # STACK PUSH: place a new queen
                # check condition satisfied or not
                if columns[col] and backward[col + row] and forward[col - row]:
                    stack.append(col)
                    columns[col] = backward[col + row] = forward[col - row] = False
                    col = 0
                    continue
            else:
                if col >= n:
                    # search has met its dead end, and maybe
                    # the whole depth-firsts search has ended
                    if not row:
                        return solutions
                else:
                    # row gets no less than n: stack size is the board width,
                    # i.e., a solution has been found
                    solutions.append(Solution.show(stack, n))
                # STACK POP
                col = stack.pop()
                row -= 1
                # restore states to BACKTRACK
                columns[col] = backward[col + row] = forward[col - row] = True
            col += 1


if __name__ == "__main__":
    N = 4
    result = Solution().solveNQueens(N)
    print('{} queens solution: '.format(N), result)
    N = 8
    result = Solution().solveNQueens(N)
    print('{} queens with {} solutions'.format(N, len(result)))
