#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
713. Subarray Product Less Than K

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.

==============================================================================================
SOLUTION

1. Brute force
Exhaust all possible cases, and verify.

Complexity: O(N²)

2. Cumulative product with binary search

Range product query, we can build the prefix product (cumulative product) table, just like
prefix sum.

Input:              nums = [10, 5, 2, 6], k = 100
cumulative product:     1,  10, 50, 100, 600

How to query less than efficiently?

If we do linear scan, then complexity is still O(N²).
But, note that the numbers are all positive, meaning the cumulative product must be
monotonically increasing. Increasing sequence means sorted, and sorted indicates we can
perform binary search to find the lower bound!

Complexity: O(NlogN)

But, how about overflow?

3. Dynamic programming
Still O(N²)

4. States ending here
Keep track of sum ending here, that is smaller than k. Keep it in a dictionary.

But this degenerates to brute force method for [2, 2, 2, 2, 2], k = 10^6 case.

5. Sliding window

Find maximum windows, and compute the valid subarrays.

For each right, call opt(right) the smallest left so that the product of the subarray
nums[left] * nums[left + 1] * ... * nums[right] is less than k.
opt is a MONOTONE INCREASING FUNCTION, so we can use a SLIDING WINDOW.


"""

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # result = self._numSubarrayProductLessThanKSlidingWindow(nums, k)
        result = self._numSubarrayProductLessThanKSlidingWindow2(nums, k)

        print(nums, k, result)

        return result

    def _numSubarrayProductLessThanKSlidingWindow(self, nums, k):
        # if k == 1 or not nums: return 0

        count = 0
        i, j = 0, 0 # range pointers
        product = 1 # initialization: range product of [i, ..., j], less than k
        while j < len(nums): # 0
            product *= nums[j] # multiply
            while product >= k and i <= j:
                count += j - i # add number of valid subarrays starting with i.

                product //= nums[i] #
                i += 1
            j += 1

        count += (j - i) * (j - i + 1) // 2

        return count

    def _numSubarrayProductLessThanKSlidingWindow2(self, nums, k):
        count = 0
        i, j = 0, 0 # range pointers
        product = 1 # initialization: range product of [i, ..., j - 1], maybe not than k
        while j < len(nums): # 1
            while product * nums[j] >= k and i < j: # in case of overflow
                if product < k: count += j - i # add number of valid subarrays starting with i.

                product //= nums[i]#
                i += 1

            product *= nums[j] # multiplied at last, no guarantee that product < k
            j += 1

        if product < k: count += (j - i) * (j - i + 1) // 2

        return count


def test():
    solution = Solution()

    assert solution.numSubarrayProductLessThanK([], 1) == 0
    assert solution.numSubarrayProductLessThanK([], 2) == 0
    assert solution.numSubarrayProductLessThanK([1], 3) == 1
    assert solution.numSubarrayProductLessThanK([1, 1], 3) == 3
    assert solution.numSubarrayProductLessThanK([1, 3, 1], 4) == 6
    assert solution.numSubarrayProductLessThanK([1, 3, 1], 3) == 2
    assert solution.numSubarrayProductLessThanK([3, 1, 1], 2) == 3
    assert solution.numSubarrayProductLessThanK([10, 5, 2], 100) == 5
    assert solution.numSubarrayProductLessThanK([10, 5, 2, 6], 100) == 8
    assert solution.numSubarrayProductLessThanK([10, 5, 2, 6], 1) == 0

    print("self test passed!")

if __name__ == '__main__':
    test()
