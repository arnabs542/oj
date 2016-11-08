#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
169. Majority Element

Total Accepted: 154296
Total Submissions: 349677
Difficulty: Easy
Contributors: Admin

Given an array of size n, find the majority element. The majority element is the
element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.majorityElementHash(nums)
        return self.majorityElementSort(nums)
        # return self.majorityElementDivide(nums)

    def majorityElementSort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums) // 2]

    def majorityElementHash(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for num in nums:
            count.setdefault(num, 0)
            count[num] += 1
            if count[num] > len(nums) // 2:
                return num

        return -1

    def majorityElementRandomization(self, nums):
        # TODO: randomized solution
        # randomly sample an element, check whether its the majority element
        pass

    def majorityElementDivide(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


def test():
    solution = Solution()
    assert solution.majorityElement([1]) == 1
    print('self test passed')

if __name__ == '__main__':
    test()
