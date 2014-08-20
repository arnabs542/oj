'''
Surrounded Regions


Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

'''


'''
SOLUTION:
    Search is a good way to solve this problem!
First and easy thought might, scan all the element, if meets 'O', looking
for a path to the boundary, if not exist, put it to 'X'. To look for the
path, if all the four directions all have no way out, this element has no
way out. The DFS can be used.  See code(small case) below. Actually, it
only cannot pass the last big test case (where 250x250 matrix is provided
).

However, it will not pass the big test, because the complexity is too high
. One common thought is to use BFS instead of DFS, which use more space,
but less time.

So how BFS is conducted, we can think from out to inside. Because the
boundary 'O' are definitely "live" (have a path out) element, so, we BFS
from each 'O' in the boundary, mark all its four directions (where is also
'O') as "live". If you think here, you almost done, the standard BFS using
a queue (here I use vector for simplicity) can solve the problem. Last
step is to flip "O" to "X" because there is no way out, and flip "P"(live)
to "O", because it has a path out. See code (big case) for details. All
the test cases are passed.
'''


class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.

    def solve(self, board):
        # BFS search elements on the boundary
        if len(board) == 0:
            return
        rl = len(board)
        cl = len(board[0])
        for row in [0, rl - 1]:
            for col in range(cl):
                if board[row][col] == 'O':
                    self.BFS(board, row, col)
        for col in [0, cl - 1]:
            for row in range(rl):
                if board[row][col] == 'O':
                    self.BFS(board, row, col)

        for row in range(rl):
            for col in range(cl):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'P':
                    board[row][col] = 'O'

    def BFS(self, board, row, col):
        rl = len(board)
        cl = len(board[0])
        queue = []
        if board[row][col] == 'O':
            board[row][col] = 'P'
            queue.append([row, col])
        while len(queue) > 0:
            r, c = queue.pop(0)
            for i in range(4):
                nr = r + self.nextIndexDiff[i][0]
                nc = c + self.nextIndexDiff[i][1]
                if nr not in range(rl) or nc not in range(cl):
                    continue
                if board[nr][nc] == 'O':
                    board[nr][nc] = 'P'
                    queue.append([nr, nc])

    # index difference in direction of UP,RIGHT,DOWN,LEFT
    nextIndexDiff = [[-1, 0], [0, 1], [1, 0], [0, -1]]

if __name__ == "__main__":
    board = [
        ['X', 'O', 'X', 'X'],
        ['O', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'O'],
        ['O', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'O'],
        ['O', 'X', 'O', 'X']]
    Solution().solve(board)
    print board
    board = []
    Solution().solve(board)
    print board
