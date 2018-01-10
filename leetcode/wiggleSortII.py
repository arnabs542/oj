#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
324. Wiggle Sort II

Total Accepted: 20960
Total Submissions: 83983
Difficulty: Medium
Contributors: Admin

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?

================================================================================
SOLUTION

It can be done with partition method. If there are no repeated elements, we
can greedily swap mismatched elements.

Consider some simple simple special cases where:
The array is increasing or decreasing. Just swap adjacent pairs will give the wiggle result.

1. Sort
Remove restrictions in the follow up, reduce it to a simple form.

What if the array is already sorted?
What if there are no repeated value?
Then we can swap adjacent values, and it's done.

But, if there are repeated values, swapping adjacent values won't do the work.
And we need to shuffle the repeated values.

How to shuffle same numbers?
In the sorted form, repeated values are always in a contiguous range.
To shuffle repeated values, we can select those elements in different order.

Partition the array into half. Fill even positions from first half, in
decreasing order, and fill odd positions from second half, in decreasing order.


3. Divide and conquer?

2. Linear time complexity

Maybe swap where we can?
Duplicate situation: Go find first non-duplicate, swap.

Edge cases
If an array consist of only same values, then it'll be impossible to achieve the goal.

And the problem becomes complex when there are duplicates in the array.

Greedy strategy? Quick sort? Divide and conquer?

'''

class Solution(object):

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self._wiggleSortSort(nums)
        # self._wiggleSortTwoPointers(nums)
        print(nums)

    def _wiggleSortSort(self, nums):
        nums1 = list(nums)
        nums1.sort()
        mid = (len(nums1) - 1) // 2
        end = len(nums1) - 1

        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = nums1[mid]
                mid -= 1
            else:
                nums[i] = nums1[end]
                end -= 1

    def _wiggleSortTwoPointers(self, nums: list) -> None:
        left, j = 0, 1
        sign = 1  # positive difference expected
        while j < len(nums):
            comparison = (nums[j] - nums[left]) * sign
            if comparison > 0:
                nums[j], nums[left + 1] = nums[left + 1], nums[j]
                # sign *= -1
            elif comparison == 0:
                # TODO: deal with duplicate numbers
                k = j + 1
                while k < len(nums) and nums[k] == nums[j]:
                    k += 1
                j = k
                continue
            else:
                nums[j], nums[left] = nums[left], nums[j]
            sign *= -1
            left += 1
            j = left + 1
            pass

        # TODO: virtual indexing? perfect shuffle? index mapping?

def check(nums):
    if len(nums) <= 1:
        return True
    sign = 1
    for i in range(0, len(nums) - 1):
        if sign * (nums[i + 1] - nums[i]) <= 0:
            return False
        sign *= -1
        pass
    return True

def test():
    solution = Solution()

    nums = []
    solution.wiggleSort(nums)
    assert(check(nums))

    nums = [1, 2]
    solution.wiggleSort(nums)
    assert(check(nums))

    nums = [4, 5, 5, 6] # [5, 6, 4, 5]
    solution.wiggleSort(nums)
    assert(check([5, 6, 4, 5]))
    assert(not check([5, 6, 5, 4]))
    assert(check(nums))

    nums = [4, 5, 6, 6]
    solution.wiggleSort(nums)
    assert(check([4, 6, 5, 6]))
    assert(check(nums))

    nums = [1, 2, 3, 4, 5, 6, ]
    solution.wiggleSort(nums)
    assert(check(nums))

    nums = [7, 6, 5, 4, 3, 2, 1]
    solution.wiggleSort(nums)
    assert(check(nums))

    nums = [1, 4, 3, 3, 2, 1]
    solution.wiggleSort(nums)
    assert(check(nums))

    nums = [1, 5, 1, 1, 6, 4]
    solution.wiggleSort(nums)
    assert(check(nums))

    nums = [1, 3, 2, 2, 3, 1]
    solution.wiggleSort(nums)
    assert(check(nums))

    nums = [5, 5, 5, 6, 7]
    solution.wiggleSort(nums)
    assert(check(nums))

    nums = [5, 6, 7, 7, 7] # bad case
    solution.wiggleSort(nums)
    assert(not check(nums))


    nums = [1, 3, 2, 2, 3, 1] # FIXME:
    solution.wiggleSort(nums)
    assert(check([1, 3, 2, 3, 1, 2]))
    assert(check(nums))

    print("self test passed")

if __name__ == '__main__':
    test()
