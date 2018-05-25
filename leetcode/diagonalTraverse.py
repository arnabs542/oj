#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
498. Diagonal Traverse

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:

Note:
The total number of elements of the given matrix will not exceed 10,000.


================================================================================

1. State machine
Maintain a state of:(
    x coordinate,
    y coordinate,
    traversing direction,
)

State transition
----------------

When traversing to right top with current coordinate (x, y), next coordinate
will be in ((x - 1, y + 1), (x, y + 1), (x + 1, y)), with priority.

When traversing to left bottom with current coordinate (x, y), next coordinate
will be in ((x + 1, y - 1), (x + 1, y), (x, y + 1)), with priority.


"""

class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = self._findDiagonalOrder(matrix)

        print(matrix, " => ", result)

        return result

    def _findDiagonalOrder(self, matrix):
        LEFT, RIGHT = 0, 1
        result = []

        if not matrix or not matrix[0]:
            return result
        m, n = len(matrix), len(matrix[0])

        # initialization
        i = 0
        x, y = 0, 0
        direction = RIGHT

        while i < m * n:
            result.append(matrix[x][y])
            i += 1

            # next state
            if direction == RIGHT:
                if x - 1 >= 0 and y + 1 < n:
                    x -= 1
                    y += 1
                else:
                    direction = LEFT
                    if y + 1 < n:
                        y += 1
                    else:
                        x += 1

            elif direction == LEFT:
                if x + 1 < m and y - 1 >= 0:
                    x += 1
                    y -= 1
                else:
                    direction = RIGHT
                    if x + 1 < m:
                        x += 1
                    else:
                        y += 1

        return result

    # TODO: more concise solution


def test():
    solution = Solution()

    assert solution.findDiagonalOrder([
    ]) == []
    assert solution.findDiagonalOrder([
        [1, 2, 3, 4]
    ]) == [1, 2, 3, 4]
    assert solution.findDiagonalOrder([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
    ]) == [1, 2, 5, 6, 3, 4, 7, 8]

    assert solution.findDiagonalOrder([
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ],
    ]) == [1, 2, 4, 7, 5, 3, 6, 8, 9]

    print("self test passed!")

if __name__ == '__main__':
    test()
