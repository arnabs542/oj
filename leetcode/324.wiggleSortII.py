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

1. Partition by median - sort - shift & insert
Remove restrictions in the follow up, reduce it to a simple form.

What if the array is already sorted?
What if there are no repeated value?
Then we can swap adjacent values, and it's done.

Observation
-----------
Numbers on odd positions must be larger than adjacent even position numbers!
Then we can fill even and odd positions with two non-overlapping range of numbers.
Then it's a partition problem, find the MEDIAN!

How to deal with duplicate numbers?
In the sorted form, repeated values are always in a contiguous range.
We can INSERT other numbers to separate adjacent same numbers.

Partition the array into half. Fill even positions from first half, in
decreasing order, and fill odd positions from second half, in decreasing order.

[1,1,1,4,5,6] => [1,4,1,5,1,6]
[1,1,2,2,3,3] => [1,2,1,3,2,3]



Linear time complexity
----------------------

Divide and conquer?
Maybe swap where we can?
Duplicate situation: Go find first non-duplicate, swap.

Edge cases
If an array consist of only same values, then it'll be impossible to achieve the goal.

And the problem becomes complex when there are duplicates in the array.

Greedy strategy? Quick sort? Divide and conquer?

2. Partitioning by median - Quick select - virtual indexing

For the sort and insert method, it works because the sorted array in partitioned
into two separate parts, and the right half is no less than the left part.
Actually we don't need strongly ordered array.
We only need to PARTITION THE ARRAY INTO TWO NON-OVERLAPPING INTERVALS.
And put the left half in even positions, right half in odd positions.

Quick select the median!

The problem is how to elements in place after partitioned, in-place.

In-place array transformation includes:
- swap two positions
- shift positions, or chained shifting(x =f(x), f(x) => f(f(x)))
- iterated function x_n=f(x_{n-1}), x_{n-1}=f(x_{n-2})

Use two pointers, one indicates left part odd position, one indicates
right part even position, swap such pair!


Complexity
O(N)


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
        # XXX: don't work
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

    def wiggleSortPartitionByMedian(self, nums):
        # partition by median
        def partition(l, h):
            i = j = l
            pivot = nums[h]
            while j < h:
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                j += 1
            return i
        l = 0
        h = len(nums) - 1
        m = (l + h)// 2
        while True:
            pass
        # swap
        pass

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
