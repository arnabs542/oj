#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
378. Kth Smallest Element in a Sorted Matrix

Total Accepted: 23057
Total Submissions: 53571
Difficulty: Medium
Contributors: Admin

Given a n x n matrix where each of the rows and columns are sorted in ascending order,
find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n².

==============================================================================================
SOLUTION

1. Brute-force
Sort: O(n²logn²)
Merge sort: O(n²logn), logn for retrieving smallest of n rows.

--------------------------------------------------------------------------------
Transform to "kth element of n sorted arrays"

2. Search with heap from top left or along rows
Such matrix is naturally a min heap, with heap relation:
    matrix[i][j] < matrix[i + 1][j],
    matrix[i][j] < matrix[i][j + 1]
So we can do BFS starting with (0, 0). But expanding search frontier in multiple directions
will require auxiliary storage to filter duplicate

Complexity: O(klogn+nlogn), worst O(n²logn)

Or we can search along rows, with a heap, like in merge sort.
Complexity: O(klogn), worst O(n²logn)

3. Expand search frontier in one direction: from up to down.

4. Binary search - SEARCH in VALUE SPACE INSTEAD OF INDEX SPACE and VERIFY
Since the matrix has a monotonicity property, we can use binary search.
But the trick here is not to search in the INDEX SPACE, but in the VALUE SPACE.

At each time, we search for the value that has k values no greater than it.
And the verify process can be done in O(NlogN),

Time complexity O(NlogNlog(max - min)) = O(Nlog²N).

5. Binary search - index space ?
Divide the search space into three regions:
top left rectangle S1, bottom rectangle S2, top right rectangle S3.
where area(S1) = area(S2) + area(S3)

6. Binary search tree perspective
If viewed from bottom left, it looks like a binary search tree.
At each time we can rule out one row or column!

State: (i, j).
State transition: (i-1, j), (i, j+1), kth element.

Complexity: O(n+n)=O(n)

================================================================================
SIMILAR PROBLEM
Median of two sorted arrays.

'''

from heapq import heappush, heappop

class Solution(object):

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # return self.kthSmallestBFSHeap(matrix, k)
        return self.kthSmallestBFSBinarySearchValueSpace(matrix, k)

    def kthSmallestBFSHeap(self, matrix, k) -> int:
        if not (matrix and k):
            return 0
        heap = []
        for i in range(len(matrix)): # push first values in each column
            heappush(heap, (matrix[0][i], 0, i))
        while k and heap:
            _, i, j = heappop(heap)
            # print(i, j, matrix[i][j])
            k -= 1
            i1, j1 = i + 1, j
            if i1 < len(matrix) > j1: heappush(heap, (matrix[i1][j1], i1, j1))
        print(matrix[i][j])
        return matrix[i][j]

    def kthSmallestBFSBinarySearchValueSpace(self, matrix, k) -> int:
        if not matrix:
            return 0
        low, high = matrix[0][0], matrix[-1][-1]
        while low <= high:
            mid = (low + high) >> 1
            count_no_less = 0
            j = len(matrix) - 1
            # XXX: count of values no less than, harnessing the monotonicity
            for i, _ in enumerate(matrix):
                while j >= 0 and matrix[i][j] > mid: j -= 1
                count_no_less += j + 1
            if count_no_less >= k: high = mid - 1
            else: low = mid + 1
        return low

     # TODO: binary search tree method, rule out rows and columns.


def test():
    solution = Solution()

    assert solution.kthSmallest([], 13) == 0

    assert solution.kthSmallest([
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15],
    ], 1) == 1

    assert solution.kthSmallest([
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15],
    ], 6) == 12

    assert solution.kthSmallest([
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15],
    ], 8) == 13

    print("self test passed")

if __name__ == '__main__':
    test()
