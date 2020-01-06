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

==============================================================================================
SOLUTION

1. Count with hash table
Complexity: O(N), O(N)

2. Reduced top K problem: find the kth element, where k is n/2.
1) Sort: O(nlogn)
2) Heap( top K ): O(nlogk)
3) Quick select: O(n)

3. Voting algorithm
Complexity: O(N), O(1)

'''

import random

class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self._majorityElementHashTableCount(nums)
        # return self._majorityElementSort(nums)
        return self._majorityElementDivideAndConquer(nums)
        # return self._majorityElementVote(nums)

    def _majorityElementSort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums) // 2]

    def _majorityElementHashTableCount(self, nums):
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

    def _majorityElementRandomization(self, nums):
        # TODO: randomized solution
        # randomly sample an element, check whether its occurrence is above
        # ⌊n/2⌋
        pass

    def _majorityElementDivideAndConquer(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        This problem is a degraded special case of the kth largest element, where
        k is equal to the middle of nums.

        Divide and conquer with partition
        Keep partitioning the list, until the pivot is at the middle position.
        """
        # FIXED: partitioning method exceeds time limit
        def partition(arr, p, r):
            pivot = arr[r]
            i = j = p
            for j in range(p, r):
                if arr[j] <= pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[i], arr[r] = arr[r], arr[i]
            return i

        def partitionDNF(arr, p, r):
            """
            Dutch national flag partition: tackle situation of many duplicate numbers
            """
            pivot = arr[r]
            i, j, n = p, p, r
            while j <= n:
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j += 1
                elif arr[j] > pivot:
                    arr[j], arr[n] = arr[n], arr[j]
                    n -= 1
                else: j += 1
            return i, n

        left, right = 0, len(nums) - 1
        mid = len(nums) // 2
        while left <= right:
            # q = partition(nums, left, right)
            p, q = partitionDNF(nums, left, right)
            # print(p, q)
            if q < mid:
                left = q + 1
            elif p > mid:
                right = q - 1
            else:
                break

        return nums[mid]

    def _majorityElementVote(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Boyer-Moore Majority Vote algorithm
        http://www.cs.utexas.edu/~moore/best-ideas/mjrty/


        We will sweep down the sequence starting at the pointer position shown above.
        As we sweep we maintain a pair consisting of a current candidate and a counter.
        Initially, the current candidate is unknown and the counter is 0.
        When we move the pointer forward over an element e:

            If the counter is 0, we set the current candidate to e and we set the counter to 1.
            If the counter is not 0, we increment or decrement the counter according to whether e is the
        current candidate.
            When we are done, the current candidate is the majority element, if there is a majority.

        O(n) time complexity.
        """
        count, candidate = 0, None
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        # print(candidate)
        return candidate

    def _majorityElementBit(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        If a number is majority, then each bit of value 1 must be majority too. Thus we
        can accumulate the bits.
        """
        # TODO: bit manipulation...

def test():
    solution = Solution()
    assert solution.majorityElement([1]) == 1
    assert solution.majorityElement([3, 2, 3]) == 3
    assert solution.majorityElement([1024] * 500 + [2048] * 501) == 2048
    assert solution.majorityElement([2048] * 501 + [1024] * 500) == 2048
    nums = [1] * 24999 + [2] * 25001
    assert solution.majorityElement(nums) == 2
    print('self test passed')

if __name__ == '__main__':
    test()
