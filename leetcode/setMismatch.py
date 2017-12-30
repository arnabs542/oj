#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
645. Set Mismatch

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.

==============================================================================================
SOLUTION

1. Hash count

Complexity: O(N), O(N)

2. Bucket count

Complexity: O(N), O(N)

3. Inplace  bucket

Complexity: O(N), O(1)

4. XOR
Calculate XOR result filter = XOR(nums, [1, n]) = missing ^ duplicate.

Using one bit in filter as mask, divide nums into nums0 and nums1, where for each number x in nums0,
x & mask = 0, and for y in nums1, y & mask = mask.
Similarly, do divide [1, n] into set0 and set1.

After this filtering, the duplicate number and missing number are separated into two different sets.

Take XOR result of set0 and nums0, giving result denoted by a.
Take XOR result of set1 and nums1, giving result denoted by b.

Then a and b must be the missing and duplicate number, but the mapping is unknown yet.
Traverse nums to check which one of a and b exist. Then which one is duplicate and missing is known.

Complexity: O(N), O(1)

Pro: don't have to modify the input data
Con: can't deal with situation where one element can repeat for more than once.

"""

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = self._findErrorNumsBucket(nums)

        print(nums, result)

        return result

    def _findErrorNumsBucket(self, nums):
        dup, missing = -1, -1
        n = len(nums)
        i = 0

        while i < n:
            j = nums[i] - 1 # should go to this bucket
            if nums[i] == nums[j]:
                if i != j: dup = nums[i]
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                missing = i + 1
        return dup, missing

def test():
    solution = Solution()

    nums = []
    nums = [1, 1]
    assert solution.findErrorNums(nums) == (1, 2)

    nums = [2, 2]
    assert solution.findErrorNums(nums) == (2, 1)

    nums = [1, 2, 2, 4]
    assert solution.findErrorNums(nums) == (2, 3)

    print("self test passed!")

if __name__ == "__main__":
    test()

