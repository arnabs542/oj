#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
454. 4Sum II

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -2^28 to 2^28 - 1 and the result is guaranteed to be at most 2³¹ - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

================================================================================
1. Brute force

Complexity: O(N⁴)

2. Enumerate first three numbers, and binary search for fourth one

Complexity: O(N³logN)

3. Divide and conquer - bidirectional search - instead of sequential search
Same idea is like in 'merge k sorted lists'.

Divide the four lists into two group, each group contribute two integers.

Then we can query

Complexity: O(N²)


"""

from collections import Counter

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        result = self._fourSumCountDivideAndConquer(A, B, C, D)

        print(A, B, C, D, result)

        return result

    def _fourSumCountDivideAndConquer(self, A, B, C, D):
        counter1 = Counter([a + b for b in B for a in A])
        counter2 = Counter([c + d for d in D for c in C])
        # print(counter1, counter2)

        result = 0
        for s1 in counter1:
            c1 = counter1[s1]
            c2 = counter2[-s1]
            result += c1 * c2
        return result

def test():
    solution = Solution()

    assert solution.fourSumCount([], [], [], []) == 0
    assert solution.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2

    print("self test passed!")

if __name__ == '__main__':
    test()
