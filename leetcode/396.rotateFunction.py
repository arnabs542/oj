#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
396. Rotate Function

Total Accepted: 11841
Total Submissions: 39524
Difficulty: Easy
Contributors: Admin

Given an array of integers A and let n to be its length.

Assume Bₖ to be an array obtained by rotating the array A k positions clock-wise, we
define a "rotation function" F on A as follow:

F(k) = 0 * Bₖ[0] + 1 * Bₖ[1] + ... + (n-1) * Bₖ[n-1].

Calculate the maximum value of F(0), F(1), ..., F(n-1).

Note:
n is guaranteed to be less than 10⁵.

Example:

A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.

==============================================================================================
SOLUTION:

This is a similar process with Convolution.
Denote the array [0, 1, 2, ..., n - 1] as Kernel.

1. Brute-force solution, max(F(k)) = max(Bₖ @ Kernel), where k = =[0, n - 1], and the vector
inner product is of time complexity O(N), so overall time complexity is O(N²).

2. Linear solution?
The high complexity results in duplicate calculations while sliding(rotating) the array. To
derive some RECURRENCE RELATION may help:
∵
    F(k) = 0 * Bₖ[0] + 1 * Bₖ[1] + ... + (n-1) * Bₖ[n-1]
and
    Bₖ[i] = Bₖ-₁[i - 1 % n]
∴
    F(k) = 0 * Bₖ[0]     + ... + (n-1) * Bₖ[n-1]
         = 0 * Bₖ-₁[n-1] + ... + (n-1) * Bₖ-₁[n-2]
         = 1 * Bₖ-₁[0]   + ... + (n-1) * Bₖ-₁[n-2]
F(k - 1) = 0 * Bₖ-₁[0]   + ... + (n-2) * Bₖ-₁[n-2] + (n-1) * Bₖ-₁[n-1]
∴
F(k) - F(k - 1) = 0 * Bₖ-₁[n-1] + Bₖ-₁[0] + ...       + Bₖ-₁[n-2] - (n - 1) * Bₖ-₁[n-1]
                = Bₖ-₁[n-1]     + Bₖ-₁[0] + ...       + Bₖ-₁[n-2] - (n) * Bₖ-₁[n-1]
                = Bₖ-₁[0]       + ...     + Bₖ-₁[n-2] + Bₖ-₁[n-1] - (n) * Bₖ-₁[n-1]
                = sum(A) - n * Bₖ-₁[n-1]

Initial condition:
Bₖ[n-1] = A[(n - 1 - k) % n]
F(0) = A @ kernel.

'''

class Solution(object):

    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # return self.maxRotateFunctionBruteForce(A)
        return self.maxRotateFunctionLinear(A)

    def maxRotateFunctionBruteForce(self, A) -> int:
        # FIXME: time limit exceeded
        if not A:
            return 0
        result = float('-inf')
        for k in range(len(A)):
            result = max(result, sum(
                map(lambda i: i * A[(i + k) % len(A)], range(len(A)))
            ))
        return result

    def maxRotateFunctionLinear(self, A) -> int:
        sumA = sum(A)
        result = curr = sum(map(lambda i: i * A[i], range(len(A))))
        for k in range(len(A)):
            curr += sumA - len(A) * A[(len(A) - 1 - k) % len(A)]
            result = max(result, curr)
        return result

def test():
    solution = Solution()

    assert not solution.maxRotateFunction([])
    assert solution.maxRotateFunction([4, 3, 2, 6]) == 26
    assert solution.maxRotateFunction([-4, -3, 2, 6]) == 19

    print('self test passed')

if __name__ == '__main__':
    test()
