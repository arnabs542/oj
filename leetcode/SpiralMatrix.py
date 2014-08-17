'''
Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''

'''
SOLUTION:
    Similar to Spiral Matrix II.Just loop!.
'''


class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers

    def spiralOrder(self, matrix):
        # the correct way to initialize python multi-dimensional array!!!
        if len(matrix) == 0:
            return []
        visit = [[-1 for i in range(len(matrix[0]))]
                 for j in range(len(matrix))]
        arr = []
        row = 0
        col = 0
        cdir = 0
        arr.append(matrix[0][0])
        visit[row][col] = 1
        for i in range(2, len(matrix) * len(matrix[0]) + 1, 1):
            row, col, cdir = self.nextSubscript(matrix, visit, row, col, cdir)
            arr.append(matrix[row][col])
            visit[row][col] = i

        return arr

    # the index increase of direction right,down,left and up
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    # @param arr,array
    # @param row,row index
    # @param col,column index
    # @param dir,direction
    def nextSubscript(self, matrix, visit, row, col, cdir):
        # generation completed
        # if self.probe == 4:
            # return -1, -1, -1
        new_row = row + self.direction[cdir][0]
        new_col = col + self.direction[cdir][1]
        new_cdir = cdir
        if new_row >= len(matrix) or new_row < 0 or new_col < 0 or new_col >= len(matrix[0]) or visit[new_row][new_col] != -1:
            # proceed in a new direction
            new_cdir = (cdir + 1) % 4
            return self.nextSubscript(matrix, visit, row, col, new_cdir)
        else:
            # self.probe = 0
            return new_row, new_col, new_cdir

if __name__ == "__main__":
    print Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print Solution().spiralOrder([[2, 3]])
