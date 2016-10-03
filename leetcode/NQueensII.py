'''
N-Queens II

Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.


Solution:
    @1: BACKTRACK with recursive depth-first search.
    @2: BACKTRACK with stack implemented DFS.
    @3: Bit manipulation instead of array representation of queens.

'''

import math


class Solution:

    @classmethod
    def check(cls, stack, row, col):
        for i in range(0, row, 1):
            # colinear or diagonal
            if stack[i] == col or math.fabs(stack[i] - col) == row - i:
                return False

        return True

    # @return a list of lists of string
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        num_solutions = 0
        stack = []
        stack.append(0)
        candidate_start = 0
        while True:
            # TODO(DONE): decouple the STACK's PUSH and POP operation
            stack_size = len(stack)
            if stack_size < n and candidate_start < n:
                # STACK PUSH: place a new queen
                while candidate_start < n:
                    if self.check(stack, len(stack), candidate_start):
                        stack.append(candidate_start)
                        candidate_start = 0
                        break
                    else:
                        candidate_start += 1

            else:
                # search has met its dead end
                if candidate_start >= n:
                    if not stack_size:
                        return num_solutions
                else:
                    # stack size is the board width, i.e., a solution has been found
                    num_solutions += 1
                # STACK POP
                candidate_start = stack.pop() + 1

if __name__ == "__main__":
    results = Solution().totalNQueens(8)
    print("%d solutions" % results)
