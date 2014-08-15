'''
N-Queens

Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
'''

'''
Solution:
    @1: Backtrack Depth-first search.Backtrack with recursion
    @2: Backtrack with stack implementation of DFS
    @3: Bit manipulation instead of array representation of queens.
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
    def totalNQueens(self, n):
        res = []
        stack = []
        stack.append(0)
        start = 0
        while True:
            sl = len(stack)
            if sl < n:
                for i in range(start, n, 1):
                    if Solution.check(stack, len(stack), i):
                        stack.append(i)
                        start = 0
                        break

                if sl == len(stack):
                    if sl == 0:
                        return len(res)
                    else:
                        start = stack.pop() + 1
                else:
                    pass

            else:
                res.append(Solution.show(stack, n))
                start = stack.pop() + 1

if __name__ == "__main__":
    res = Solution().totalNQueens(8)
    print "%d solutions" % res
