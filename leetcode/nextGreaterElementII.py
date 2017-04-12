#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
503. Next Greater Element II

Total Accepted: 4414
Total Submissions: 9460
Difficulty: Medium
Contributors: love_FDU_llp

Given a circular array (the next element of the last element is the first element of the array),
print the Next Greater Number for every element. The Next Greater Number of a number x is the
first greater number to its traversing-order next in the array, which means you could search
circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:

Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.

Note: The length of given array won't exceed 10000.

==============================================================================================
SOLUTION

Similar to previous problem, except that we need to fill the last element's next greater
element first.

'''
class Solution(object):

    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nge = self.nextGreaterElementsFSM(nums)
        print(nge)
        return nge

    def nextGreaterElementsFSM(self, nums):
        nge = [i + 1 for i in range(len(nums))] # pointing to next element initially
        # pass 1, find circular next greater element for last element
        # for i in range(len(nums) - 1):
            # if nums[i] > nums[-1]:
                # nge[-1] = i
                # break
        # pass 2, build the rest of the lookup table
        for i in range(len(nums) - 1, -1, -1):
            q = nge[i] % len(nums)
            while q not in (i, len(nums)) and nums[i] >= nums[q]:
                q = nge[q]
            nge[i] = q if q != i else len(nums)
        return [nums[x] if x != len(nums) else -1 for x in nge]

    def nextGreaterElementsStack(self, nums):
        # TODO: stack
        pass

def test():
    solution = Solution()

    assert solution.nextGreaterElements([]) == []
    assert solution.nextGreaterElements([4, 3, 2, 1]) == [-1, 4, 4, 4]
    assert solution.nextGreaterElements([2, 3, 1]) == [3, -1, 2]
    assert solution.nextGreaterElements([1, 2, 1]) == [2, -1, 2]
    assert solution.nextGreaterElements([1, 4, 2, 3]) == [4, -1, 3, 4]
    assert solution.nextGreaterElements([1, 2, 3, 4]) == [2, 3, 4, -1]
    assert solution.nextGreaterElements([1, 2, 3, 2, 1]) == [2, 3, -1, 3, 2]

    print("self test passed")

if __name__ == '__main__':
    test()
