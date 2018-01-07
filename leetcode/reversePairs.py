#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
493. Reverse Pairs

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.

================================================================================
SOLUTION

Two core relation in the problem: after and smaller. This is similar to
"count of smaller numbers after self".

1. Brute force

Complexity: O(N²)

2. Backward insertion sort

3. Merge sort

Complexity: O(nlogn)

--------------------------------------------------------------------------------
RANGE QUERY - COUNT AS SUM of INDICATOR FUNCTION

Similar to "count of smaller numbers after self"

4. Range query - segment tree

5. Range query - binary indexed tree

"""

from _decorators import timeit
import bisect
from _tree import BinaryIndexedTree

class Solution:
    @timeit
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # result = self._reversePairsMergeSort(nums)
        result = self._reversePairsMergeSortOpt(nums)
        # result = self._reversePairsBisect(nums)

        print(nums[:100], result)

        return result

    def _reversePairsMergeSort(self, nums):
        """
        Merge sort

        Two passes: count then merge

        TLE in python
        """
        def mergeSort(arr, low: int, high: int):
            result = 0
            if low >= high: return 0
            mid = (low + high) // 2
            result = 0
            result += mergeSort(arr, low, mid)
            result += mergeSort(arr, mid + 1, high)

            left = (arr[low:mid+2])
            right = (arr[mid+1:high+1])
            # count
            i, j = mid - low, high - mid - 1
            while i >= 0 and j >= 0:
                if nums[left[i]] > 2 * nums[right[j]]:
                    # count[left[i]] += j + 1
                    result += j + 1
                    i -= 1
                else: j -= 1

            i, j = mid - low, high - mid - 1
            top = high
            # FIXME: negative numbers
            while i >= 0 and j >= 0:
                if nums[left[i]] >= nums[right[j]]:
                    arr[top] = left[i]
                    i -= 1
                else:
                    arr[top] = right[j]
                    j -= 1
                top -= 1
            while i >= 0:
                arr[top] = left[i]
                top -= 1
                i -= 1
            while j >= 0:
                arr[top] = right[j]
                top -= 1
                j -= 1
            return result

        indices = list(range(len(nums)))
        # count = [0 for _ in range(len(nums))]
        result = mergeSort(indices, 0, len(nums) - 1)
        return result

    def _reversePairsMergeSortOpt(self, nums):
        """
        Merge sort

        Two passes: count then merge

        TLE in Python 3, but not Python 2, OJ problem.
        """
        def mergeSort(low: int, high: int):
            if low >= high: return 0
            mid = (low + high) // 2
            result = mergeSort(low, mid) + mergeSort(mid + 1, high)

            i, j = mid, high
            while i >= low and j >= mid + 1:
                if nums[i] > 2 * nums[j]:
                    result += j - mid
                    i -= 1
                else: j -= 1

            nums[low:high+1] = sorted(nums[low:high+1])
            return result

        result = mergeSort(0, len(nums) - 1)
        return result

    def _reversePairsBisect(self, nums):
        """
        This is the inserting sort method

        Complexity: O(N²), since inserting is O(N)
        TLE in python
        """
        nums2 = []
        result = 0
        for n in reversed(nums):
            result += bisect.bisect_left(nums2, n)
            bisect.insort_right(nums2, 2 * n)
        return result

    def _reversePairsBinaryIndexedTree(self, nums):
        numsAll = [2 * num for num in nums] + nums
        num2idx = {v: i for i, v in enumerate(sorted(list(set(numsAll))))}
        result = 0
        rangeQueryTree = BinaryIndexedTree(len(numsAll))
        for i in range(len(nums) - 1, -1, -1):
            result += rangeQueryTree.query(num2idx[nums[i]] - 1)
            rangeQueryTree.update(num2idx[2 * nums[i]], 1)
        return result

def test():
    solution = Solution()

    assert solution.reversePairs([]) == 0
    assert solution.reversePairs([1, 2, 3]) == 0
    assert solution.reversePairs([1, 2, 3, 4, 5, 6, 7]) == 0
    assert solution.reversePairs([3, 2, 1]) == 1
    assert solution.reversePairs([1, 3, 2, 3, 1]) == 2
    assert solution.reversePairs([2, 4, 3, 5, 1]) == 3
    assert solution.reversePairs([0, 3, 1,]) == 1
    assert solution.reversePairs([4, 3, 2, 1]) == 2
    assert solution.reversePairs([5, 4, 3, 2, 1]) == 4
    assert solution.reversePairs([6, 5, 4, 3, 2, 1]) == 6
    assert solution.reversePairs([7, 6, 5, 4, 3, 2, 1]) == 9
    assert solution.reversePairs([8, 7, 6, 5, 4, 3, 2, 1]) == 12
    assert solution.reversePairs([-5, -5]) == 1
    assert solution.reversePairs([-5, -5, -3, -2]) == 4

    import yaml
    with open("./reversePairs.json", "r") as f:
        data = yaml.load(f)
    for d in data:
        assert solution.reversePairs(d['input']) == d['output']

    print("self test passed")

if __name__ == '__main__':
    test()
