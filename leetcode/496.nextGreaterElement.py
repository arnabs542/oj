#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
496. Next Greater Element I

Total Accepted: 8617
Total Submissions: 14710
Difficulty: Easy
Contributors: love_FDU_llp

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are
subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding
places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in
nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the
second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second
array, so output -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second
array, so output -1.

Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.

==============================================================================================
SOLUTION

1. Naive solution: find the corresponding position in nums2 of elements if nums1, and search
for next greater number. O(N²).

2. Finite State Machine: preprocess to build lookup table(avoid duplicate calculation)
Process the array backward, and build a Next Greater Number lookup table. Building the
lookup table is amortized to be of linear complexity using recursive state transition
querying like KMP processing.

Still, we need to query the position of elements of nums1 in nums2 efficiently.

3. MONOTONICITY analysis - maintain monotonic/decreasing sequence with STACK

'''

class Solution(object):

    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # result = self.nextGreaterElementFSM(findNums, nums)
        result = self.nextGreaterElementStack(findNums, nums)
        print(result)
        return result

    def nextGreaterElementFSM(self, findNums, nums):
        nge = [len(nums)] * len(nums)
        num2idx = {}
        for i in range(len(nums) - 1, -1, -1):
            num2idx[nums[i]] = i
            q = i + 1
            while q < len(nums) and nums[i] > nums[q]:
                q = nge[q]
            nge[i] = q
        return list(map(lambda x: nums[nge[num2idx[x]]] if nge[
                    num2idx[x]] != len(nums) else -1, findNums))


    def nextGreaterElementStack(self, findNums, nums):
        # TODO(done): stack implementation
        nge, stack = {}, []
        for num in nums:
            while stack and num >= stack[-1]:
                nge[stack.pop()] = num
            stack.append(num)
        return [nge.get(num, -1) for num in findNums]

def test():
    solution = Solution()

    assert solution.nextGreaterElement([], [1, 3, 4, 2]) == []
    assert solution.nextGreaterElement([1, 4, 2, 3], [1, 4, 2, 3]) == [4, -1, 3, -1]
    assert solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert solution.nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]

    print("self test passed")

if __name__ == '__main__':
    test()
