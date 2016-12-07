#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
215. Kth Largest Element in an Array

Total Accepted: 89831
Total Submissions: 245221
Difficulty: Medium
Contributors: Admin

Find the kth largest element in an unsorted array. Note that it is the kth largest element in
the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

===============================================================================================
SOLUTION:
    1. sort. O(NlogN)
    2. Maintain a MIN HEAP of size k, scan the array, take the heap top element when
    finished. O(NlogK)
    3. maintain a sorted list of size k, do insert with BINARY SEARCH. O(NlogK)
    4. PARTITION to divide and conquer (quick select).

With a MIN HEAP, we can maintain such heap of size k, while scanning the list, if the current number
is bigger then the heap top element, then replace the heap top with the current element, and then
maintain the heap structure. Time Complexity is average O(n logk).


In quicksort, in each iteration, we need to select a pivot and then PARTITION the array into
three parts:
    1. Elements smaller than the pivot;
    2. Elements equal to the pivot;(for three-way partition)
    3. Elements larger than the pivot.

To find the kth largest element,
    1. Initialize left to be 0 and right to be nums.size() - 1;
    2. Partition the array, if the pivot is at the k-1-th position, return it (we are done);
    3. If the pivot is right to the k-1-th position, update right to be the left neighbor of
the pivot;
    4. Else update left to be the right neighbor of the pivot.
    5. Repeat 2.

Time Complexity:
    So, in the average sense, the problem is reduced to approximately half of its original size,
    giving the recursion
        T(n) = T(n/2) + O(n)
    in which O(n) is the time for partition. This recursion, once solved, gives
        T(n) = O(n)
    and thus we have a linear time solution. Note that since we only need to consider one half
    of the array, the time complexity is O(n). If we need to consider both the two halves of the
    array, like quicksort, then the recursion will be
        T(n) = 2T(n/2) + O(n)
    and the complexity will be O(nlogn).
    Of course, O(n) is the average time complexity. In the worst case, the recursion may become
        T(n) = T(n - 1) + O(n) and the complexity will be O(N²).
'''

from heapq import heappush, heappop
import random

class Solution(object):

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # return self.findKthLargestSort(nums, k)
        # return self.findKthLargestHeap(nums, k)
        return self.findKthLargestPartition(nums, k)

    def findKthLargestSort(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse=True)[k - 1]

    def findKthLargestBinarySearch(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # TODO: binary search insert

    def findKthLargestHeap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # TODO: min heap
        heap = []
        for num in nums:
            if len(heap) < k:
                heappush(heap, num)
            elif heap[0] < num:
                heappop(heap)
                heappush(heap, num)

        return heap[0]

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        # print(low, high, i, arr)
        return i

    def partitionRandomized(self, arr, low, high):
        # TODO(done): randomized partition
        # randomly CHOOSE THE PIVOT
        rand = random.randint(low, high)
        arr[rand], arr[high] = arr[high], arr[rand]
        pivot = arr[high]

        i = low
        # SWEEP the sequence
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    def findKthLargestPartition(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # DONE: partition to divide and conquer
        k = len(nums) - k
        p, r = 0, len(nums) - 1
        while p <= r:
            # q = self.partition(nums, p, r)
            q = self.partitionRandomized(nums, p, r)
            if q < k:
                p = q + 1
            elif q > k:
                r = q - 1
            else:
                return nums[q]


def test():
    solution = Solution()
    arr = [2, 8, 7, 1, 8, 3, 5, 6, 4, 2]
    solution.partition(arr, 0, len(arr) - 1)
    assert arr == [2, 1, 2, 8, 8, 3, 5, 6, 4, 7]
    arr = [6, 5]
    solution.partition(arr, 0, 1)
    assert arr == [5, 6]

    assert solution.findKthLargest([1], 1) == 1
    assert solution.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    print('self test passed')

test()
