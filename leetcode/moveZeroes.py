#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
283. Move Zeroes

Total Accepted: 145052
Total Submissions: 304601
Difficulty: Easy
Contributors: Admin

Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums
should be [1, 3, 12, 0, 0].

Note:
- You must do this in-place without making a copy of the array.
- Minimize the total number of operations.

==============================================================================================
SOLUTION

Minimizing the total number of operations is actually minimizing the time complexity.

1. Brute force method.
Move zeroes to the end one by one like in bubble sort procedure.

Time complexity: O(N²).

2. PARTITION ALGORITHM with TWO POINTERS (quick sort partition, Dutch National Flag problem).

Lomuto partition scheme!

This partition scenario resembles what's used in the quick sort:
partition the different data into separating spaces with a division point.

Define state
------------
Maintain state of a tuple:
    (
    p: partition index, representing that elements on the left are all nonzero,
    i: iterating index,
    )

But quick sort partition uses swap, will it violate the original order?

Maintenance
-----------
Use two pointers p and i.
Pointer p indicating the BOUNDARY(DIVISION POINT) where the left part are non-zero
elements, and the other pointer i keeps track of the first non-zero element after p.
Then swap the element at p and i, and update p = p + 1, i = i + 1.

The core idea is to move all non-zero elements in the front of the array,
which are perfectly separated by the partition index p, and the nonzero numbers' order
are kept intact.

To minimize the total number of operations, avoid swapping if p == i.

Complexity
O(N), O(1)

################################################################################
FOLLOW UP
1. Remove elements in target array.
Mark the elements to delete as "zero", as in above problem. Then move "zero" numbers
to the end of the array. Then pop trailing "zero" elements.

Complexity
O(n), O(1)

'''

class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        return self.moveZeroesTwoPointers(nums)

    def moveZeroesTwoPointers(self, nums):
        i, j = 0, 0
        for j, _ in enumerate(nums):
            if nums[j] == 0: continue
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        return nums

def test():
    solution = Solution()

    assert solution.moveZeroes([]) == []
    assert solution.moveZeroes([0, 0, 1, 2, 3]) == [1, 2, 3, 0, 0]
    assert solution.moveZeroes([0, 0, 0]) == [0, 0, 0]
    assert solution.moveZeroes([1, 2, 3]) == [1, 2, 3]
    assert solution.moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]

    print("self test passed")

if __name__ == '__main__':
    test()
