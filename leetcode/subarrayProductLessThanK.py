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

SOLUTION
================================================================================

1. Brute force
Exhaust all possible cases, and verify.

With cumulative product calculation, complexity is reduced from O(N³) to O(N²).
Complexity: O(N²)

2. Brute force optimized with binary search

Build a data structure for O(1) range query, and do binary search on that.

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
1) Use logarithm to transform product to addition
Overflow can be tackled with logarithm operation:
\log(\prod(xi)) = \sum(\log(xi))

Multiplication is transformed to addition with logarithm.

2) Check for overflow manually

3. Dynamic programming
Still O(N²)

4. States ending here
Keep track of sum ending here, that is smaller than k. Keep it in a dictionary.

But this degenerates to brute force method for [2, 2, 2, 2, 2], k = 10^6 case,
since we don't need to keep track of all sums, we can just find the intervals and count!

5. Sliding window

To find all globally optimal, we can keep track of all locally optimal intervals.

Keep track of state (i, j, p) = (start index of window, end index of window, eligible product),
denoting longest subarray ending here,  with product less than k.

State transition:
    Similar to max subarray problem, shrink left or expand right end of the window.

Find maximum windows, and compute the valid subarrays.

For each right, call opt(right) the smallest left so that the product of the subarray
nums[left] * nums[left + 1] * ... * nums[right] is less than k.
opt is a MONOTONE INCREASING FUNCTION, so we can use a SLIDING WINDOW.

Complexity:
O(N)


"""

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # result = self._numSubarrayProductLessThanKSlidingWindow(nums, k)
        # result = self._numSubarrayProductLessThanKSlidingWindow2(nums, k)
        result = self._numSubarrayProductLessThanKSlidingWindowEndingHere(nums, k)

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
        """
        This is an approach to compute from beginning index
        """
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

    def _numSubarrayProductLessThanKSlidingWindowEndingHere(self, nums, k):
        """
        This is an approach to compute from end index
        """
        count = 0
        i, j = 0, 0 # (optimal) sliding window start index, end index
        product = 1 # product of sliding window ending at j
        for j in range(len(nums)):
            while product * nums[j] >= k and i < j:
                product //= nums[i]
                i += 1 # shrink
            product *= nums[j] # expand, product ending here
            if product < k: count += j - i + 1

        return count


def test():
    solution = Solution()

    assert solution.numSubarrayProductLessThanK([], 1) == 0
    assert solution.numSubarrayProductLessThanK([], 2) == 0
    assert solution.numSubarrayProductLessThanK([1], 0) == 0
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
