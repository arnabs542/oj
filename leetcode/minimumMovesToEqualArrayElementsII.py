#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
462. Minimum Moves to Equal Array Elements II

Total Accepted: 5223
Total Submissions: 10353
Difficulty: Medium
Contributors: andrew56

Given a non-empty integer array, find the minimum number of moves required to make
all array elements equal, where a move is incrementing a selected element by 1 or
decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

==============================================================================================
SOLUTION

The solution is equal to the problem to minimizing the absolute loss:
f(x) = ∑|x - a[i]|, where i is in [1, ..., n]

For quadratic loss, the solution is the mean value, and for absolute loss, it's the median.
If n is even, then every number in [medianLeft, medianRight] is fine, so just pick one.

'''

class Solution(object):

    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.minMoves2Median(nums)

    def minMoves2Median(self, nums):
        def median():
            return sorted(nums)[len(nums) // 2]
        m = median()
        return sum(abs(m - n) for n in nums)

    # TODO: quick select algorithm to get the median(the kth element)

def test():
    solution = Solution()

    assert solution.minMoves2([1, 2, 3]) == 2

    print("self test passed")

if __name__ == '__main__':
    test()
