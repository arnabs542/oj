#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
189. Rotate Array

Total Accepted: 96377
Total Submissions: 420656
Difficulty: Easy
Contributors: Admin

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve
this problem.

Hint:
Could you do it in-place with O(1) extra space?

SOLUTION
================================================================================

1. Copy and input

Complexity: O(n), O(n)

2. Shift one, repeat for k times

Complexity: O(kn), O(1)

3. Chain iterative rotate - doesn't work

i -> i - k -> i - k -k.
The problem is it may not be able to traverse all the points.

4. Reverse by swap
Reverse is an operation we can carry out inplace.

Suppose we will shift the array to the left by k steps.
Divide the array into two parts AB, where A = arr[0..k-1] and B = arr[k..n-1].
Then Input is AB, after rotating, it must be BA.

The idea of the algorithm is:

- Reverse A to get ArB, where Ar is reverse of A.
- Reverse B to get ArBr, where Br is reverse of B.
- Reverse all to get (ArBr) r = BA.

(ArBr)r = BA is the key property of reverse operation.

A[0] -> A[-k] -> A[n-k].
A[n-k] symmetric to A[k].
And A[0] is symmetric to A[k].

Reference:
https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/

5. Block swap

Reference:
https://www.geeksforgeeks.org/block-swap-algorithm-for-array-rotation/



Related problem:
Reverse Words in a String II
Rotate Image

'''

class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # self.rotateInsert(nums, k)
        # self.rotateSlice(nums, k)
        self.rotateReverse(nums, k)

        print (nums)

    def rotateInsert(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.

        This approach is better suited for linked list rotation.
        """
        for i in range(k):
            nums.insert(0, nums.pop())

    def rotateSlice(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    # DONE: linear space(in-place)?
    def rotateReverse(self, nums, k):
        if not nums: return
        n = len(nums)
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        k %= len(nums)
        reverse(n - k, n - 1) # AB -> Ar(B)
        reverse(0, n - k - 1) # r(A)r(B)
        reverse(0, n - 1)     # BA

def test():
    solution = Solution()

    nums = []
    k = 2
    solution.rotate(nums, k)
    assert(nums == [])

    nums = [1, 2, 3, 4, 5, 6, 7]
    solution.rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [1, 2, 3, 4, 5, 6, 7]
    solution.rotate(nums, 2)
    assert nums == [6, 7, 1, 2, 3, 4, 5]

    print('self test passed')
    pass

if __name__ == '__main__':
    test()
