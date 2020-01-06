#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
628. Maximum Product of Three Numbers

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,10⁴] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

==============================================================================================
SOLUTION

1. Brute force

Complexity: O(N³)

Don't even think about it...

2. Sort
Sort the array.

But there might be negative numbers.
And the possible product can be in these scenarios:
    1) There are at least 3 positive numbers: product of top 3 positive numbers, or bottom 2 and top 1
    2) Only 2 positive numbers:  bottom 2 and top 1
    3) Only 1 positive numbers: bottom 2 and top 1
    3) 0 positive numbers: top 3

In a word, there are only two cases:
    1) product of top 3 numbers
    2) product of top 1 and bottom 2 numbers
Return the maximum of those two situations.

Complexity:

O(nlogn), O(logn)

Sorting takes O(logn) space.

3. Top K

Since the maximum product has only two different combinations, get the top 3 and bottom 2
numbers in linear time, and then return the largest product.

Complexity: O(n), O(log3) = O(1)

"""

import heapq

class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # result = self._maximumProduct(nums)
        result = self._maximumProductTopK(nums)

        print(nums, result)

        return result

    def _maximumProduct(self, nums):
        if len(nums) < 3: return 0
        nums.sort()
        i = len(nums) - 1
        # nPositive = 0
        # while i >= 0 and nums[i] > 0 and nPositive <= 3:
            # nPositive += 1
            # i -= 1

        return max(nums[-1] * nums[-2] * nums[-3], nums[-1]*nums[0]*nums[1])

    def _maximumProductTopK(self, nums):
        if len(nums) < 3: return 0
        a = heapq.nlargest(3, nums)
        b = heapq.nsmallest(2, nums)

        return max(a[0] * a[1] * a[2], a[0] * b[0] * b[1])

def test():
    solution = Solution()

    assert solution.maximumProduct([1, 2 ]) == 0
    assert solution.maximumProduct([1, 2, 3]) == 6
    assert solution.maximumProduct([1, 2, 3, 4]) == 24
    assert solution.maximumProduct([-1, -2, 3, 4]) == 8
    assert solution.maximumProduct([-1, -2, -3, 4]) == 24
    assert solution.maximumProduct([-1, -2, 0, 4]) == 8
    assert solution.maximumProduct([-1, 0, 0, 4]) == 0
    assert solution.maximumProduct([-1, -2, -3, -4]) == -6

    nums = [722,634,-504,-379,163,-613,-842,-578,750,951,-158,30,-238,-392,-487,-797,-157,-374,999,-5,-521,-879,-858,382,626,803,-347,903,-205,57,-342,186,-736,17,83,726,-960,343,-984,937,-758,-122,577,-595,-544,-559,903,-183,192,825,368,-674,57,-959,884,29,-681,-339,582,969,-95,-455,-275,205,-548,79,258,35,233,203,20,-936,878,-868,-458,-882,867,-664,-892,-687,322,844,-745,447,-909,-586,69,-88,88,445,-553,-666,130,-640,-918,-7,-420,-368,250,-786]
    assert solution.maximumProduct(nums) == 943695360

    print("self test passed!")

if __name__ == '__main__':
    test()
