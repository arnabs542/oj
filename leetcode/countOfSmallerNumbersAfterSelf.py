#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
315. Count of Smaller Numbers After Self

Total Accepted: 22253
Total Submissions: 67233
Difficulty: Hard
Contributors: Admin

You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller
elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].

==============================================================================================
SOLUTION
    The count of smaller numbers after self is exactly the number of elements move to its left
in a STABLE SORT.

1. Brute force. for each element, count the smaller numbers after self.
Complexity: O(N²)

2. Insert sort with binary search. Inserting SORT from right to left with binary search,
then the inserting index of current element is the smaller numbers after self.
Complexity: O(NlogN) ?

3. Merge sort

4. Segment tree

5. Binary indexed tree

WRAP-UP
    Problems involved with COMPARING VALUES are naturally connected to SORTING process.

'''

class Solution(object):

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.countSmallerInsertSortBinarySearch(nums)

    def countSmallerInsertSortBinarySearch(self, nums: list) -> list:
        def searchInsert(arr, left, right, target):
            while left <= right:
                mid = (left + right) >> 1
                if target > arr[mid]: left = mid + 1
                elif target < arr[mid]: right = mid - 1
                # XXX: exactly SMALLER numbers, so keep decreasing the right pointer
                else: right = mid - 1

            return max(left, right)

        count = [0] * len(nums)
        nums_sorted = []
        for i, num in enumerate(reversed(nums)):
            pos = searchInsert(nums_sorted, 0, i - 1, num)
            count[len(nums) - 1 - i] = pos
            nums_sorted.insert(pos, num)
        # print(count)
        return count

    def countSmallerMergeSort(self, nums: list) -> list:
        '''
        merge sort solution
        '''
        # TODO: merge sort
        def mergeSort(arr, left, right):
            pass

        count = [0] * len(nums)
        mergeSort(list(enumerate(nums)), 0, len(nums) - 1)

    # TODO: binary indexed tree
    # TODO: segment tree

def test():
    solution = Solution()

    assert solution.countSmaller([]) == []
    assert solution.countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0]

    print('self test passed')

if __name__ == '__main__':
    test()
