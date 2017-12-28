#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
167. Two Sum II - Input array is sorted

Total Accepted: 38994
Total Submissions: 81136
Difficulty: Medium
Contributors: Admin

Given an array of integers that is already sorted in ascending order, find two numbers
such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the
target, where index1 must be less than index2. Please note that your returned answers (both
index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

==============================================================================================
SOLUTION
1 hash
inverted index: (key=element, value=element's position/index)

Complexity: O(N), O(N)

2. Two pointers
The target indices i, j must satisfy 0 <= i, j <= n - 1, where n is the length of the array.
Initialize i = 0, j = n - 1, then search inward(from both ends to middle).

Define state = (i, j), treat this as a graph search problem, then we have state transition
illustrated as below.

If sum of two pointers' value is less than the target value, then increment i by 1.
If sum of two pointers' value is greater than the target value, then decrease j by 1.
Repeat until we have the sum of two pointers value equal to target value.

Complexity: O(N), O(1)

3. Binary search

Complexity: O(NlogN), O(1)

'''
class Solution(object):

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                return [left + 1, right + 1]
            pass

def test():
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [1, 2]

    print('self test passed')

if __name__ == '__main__':
    test()
