'''
Spiral Matrix II

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

'''
SOLUTION:
    There four direction in spiral order.
'''


class Solution:
    # @return a list of lists of integer

    def generateMatrix(self, n):
        # the correct way to initialize python multi-dimensional array!!!
        if n <= 0:
            return []
        arr = [[-1 for i in range(n)] for j in range(n)]
        row = 0
        col = 0
        cdir = 0
        arr[row][col] = 1
        for i in range(2, n * n + 1, 1):
            row, col, cdir = self.nextSubscript(arr, row, col, cdir)
            # if row == -1:
                # return arr
            # else:
            arr[row][col] = i

        return arr

    # the index increase of direction right,down,left and up
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    probe = 0

    # @param arr,array
    # @param row,row index
    # @param col,column index
    # @param dir,direction
    def nextSubscript(self, arr, row, col, cdir):
        # generation completed
        # if self.probe == 4:
            # return -1, -1, -1
        new_row = row + self.direction[cdir][0]
        new_col = col + self.direction[cdir][1]
        new_cdir = cdir
        if new_row >= len(arr) or new_row < 0 or new_col < 0 or new_col >= len(arr) or arr[new_row][new_col] != -1:
            # proceed in a new direction
            # print(row, col, cdir, new_row, new_col, new_cdir)
            new_cdir = (cdir + 1) % 4
            # self.probe += 1
            return self.nextSubscript(arr, row, col, new_cdir)
        else:
            # self.probe = 0
            return new_row, new_col, new_cdir

if __name__ == "__main__":
    print(Solution().generateMatrix(1))
    print(Solution().generateMatrix(0))
    print(Solution().generateMatrix(4))
