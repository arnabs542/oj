'''
N-Queens II

Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.


===================================================================================================
Solution:
    @1: BACKTRACK with recursive depth-first search.
    @2: BACKTRACK with stack implemented DFS.
    @3: Bit manipulation instead of array representation of queens.

'''


class Solution(object):

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int, n queens on n x n board
        """

        num_solutions = 0
        stack = []

        columns = [True] * n # col, range is [0, n - 1]
        backward = [True] *2 * n # col + row, range is [0, 2n - 2]
        forward = [True] * 2 * n # col - row, range is [-(n - 1), n - 1]

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
                        return num_solutions
                else:
                    # row gets no less than n: stack size is the board width,
                    # i.e., a solution has been found
                    num_solutions += 1
                # STACK POP
                col = stack.pop()
                row -= 1
                # mark unvisited, restoring states to BACKTRACK
                columns[col] = backward[col + row] = forward[col - row] = True
            col += 1

if __name__ == "__main__":
    results = Solution().totalNQueens(8)
    print("%d solutions" % results)
