#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
413. Arithmetic Slices

Total Accepted: 9353
Total Submissions: 17268
Difficulty: Medium
Contributors: XiangyuLi926

A sequence of number is called arithmetic if it consists of at least three elements
and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any
pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

================================================================================
SOLUTION

1. Naive method: exhaust and count
Exhaust all slices and verify.

Complexity: O(n³), O(1).

Optimization
-----------
Elaborate with by verifying the slices while incrementally exhausting.
Then complexity is O(N²), O(1).

2. Partition and calculate - mathematical calculation without counting one by one
Partition by finding locally longest interval and mathematically calculate each
arithmetic partition.

Overlapping subproblems result in duplicate calculations, and counting one by one
is inefficient, which can be summarized mathematically.

Find all locally longest arithmetic series subarray. Then for each such
array of length l, it has number of arithmetic slices:
    f(l) = 1 + 2 + ... + (l - 2)
         = (l - 2) * (l - 2 + 1) / 2
         = (l - 2) * (l - 1) / 2

Complexity: O(n), O(1)

3. State transition - dynamic programming - track state ending here

Convert the objective function into a sum of terms, denoting g(i) as
number of arithmetic slices ending index i, then objective is:
    f = ∑g(i), where i = 0, 1, ..., N - 1.

Define state:
    dp[i] = the number of arithmetic slices ending with A[i]
Then dp[i] = dp[i - 1] + 1 if in the same arithmetic progression.

The result = ∑dp[i], i in [0, n - 1]

Complexity: O(n)

################################################################################
FOLLOW UP

1. Arithmetic sequences

2. Geometric slices/sequences

'''

class Solution(object):

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = self._numberOfArithmeticSlicesPartitionAndCalculate(A)

        print(A, " => ", result)

        return result

    def _numberOfArithmeticSlicesPartitionAndCalculate(self, A):
        diff0, diff1 = None, None
        start = 0
        n = 0
        for i in range(1, len(A)):
            diff0, diff1 = diff1, A[i] - A[i - 1]
            if diff0 not in (None, diff1) or i == len(A) - 1:
                l = i - start + (1 if diff0 == diff1 and i == len(A) - 1 else 0)
                if l >= 3:
                    n += (l - 2) * (l - 1) // 2
                start = i - 1
        print(n)

        return n

    def _numberOfArithmeticSlicesDynamicProgramming(self, A):
        pass

def test():
    solution = Solution()

    assert solution.numberOfArithmeticSlices([]) == 0
    assert solution.numberOfArithmeticSlices([1, 2, 3]) == 1
    assert solution.numberOfArithmeticSlices([1, 3, 5, 7, 9]) == 6
    assert solution.numberOfArithmeticSlices([1, 2, 3, 4]) == 3
    assert solution.numberOfArithmeticSlices([1, 2, 3, 4, 1, 2, 3, 4]) == 6

    print("self test passed")

if __name__ == '__main__':
    test()
