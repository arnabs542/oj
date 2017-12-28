#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
350. Intersection of Two Arrays II

Total Accepted: 42994
Total Submissions: 99666
Difficulty: Easy
Contributors: Admin

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.

Follow up:
    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you
cannot load all elements into the memory at once?

==============================================================================================
SOLUTION

1. Brute force solution
For each element in nums1, check existence in nums2, and remove if it does exist, and update
the intersection list.

Linear search takes O(n), and deleting an element from array takes O(n).

Complexity: O(mn).


2. Hash table

Hash count.

Complexity: O(m + n), O(m + N).


3. Sort and binary search

Sort two arrays.

For each number n in nums1 that appears p times, find the lower bound and upper bound indices
of value n, denoted by j and k, in nums2. Then n appears (k - j + 1) times.

And two lists have |p - (k - j + 1)| occurrences of n in common.

Complexity
O(sort) + O(binary search) = O(nlogn + mlogm) + O(nlogm)

4. Sort and two pointers

Well, the core part of two pointers algorithm is the meaning of the pointers.
In another word, what STATE the pointers are tracking!

In this scenario, we are trying to find intersection elements. So our objective is to let the
pointers point to same value in two arrays.

What if two pointers' value are different?
To two values equal, we need to narrow the gap: increase the smaller one!

----------------------------------------------------------------------------------------------
FOLLOW UP

Follow up 1: binary search?
Follow up 2: hash/sort the smaller.
    traverse the larger and binary search, two pointers on two arrays respectively.

Follow up 3: one is large, doesn't fit into the memory
    If only nums2 cannot fit in memory, put all elements of nums1 into a hash table,
read chunks of array that fit into the memory, and record the intersections.

Follow up 4: both large, neither fit into the memory
    If both nums1 and nums2 are so huge that neither fit into the memory, SORT
them individually (EXTERNAL SORT), then read 2 elements from each array at a time in
memory, record intersections.
    Or MapReduce paradigm could be used?

Follow up 5: find the elements in nums2, that doesn't occur in nums1(set subtract).


'''

class Solution(object):

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # return self.intersectHash(nums1, nums2)
        return self.intersectTwoPointers(nums1, nums2)

    def intersectHash(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = []
        position = {}
        for i, num in enumerate(nums1):
            position.setdefault(num, [])
            position[num].append(i)

        for num in nums2:
            if position.get(num, []):
                intersection.append(num)
                position[num].pop()
            pass
        return intersection

    def intersectTwoPointers(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        """
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        intersection = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                intersection.append(nums1[i])
                i += 1
                j += 1
            pass
        return intersection

    def intersectBinarySearch(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        Already sorted, binary search?
        But how to remove already matched elements efficiently?

        Find the lower bound and upper bound indices!

        """
        # FIXME: binary search with removing elements?



def test():
    solution = Solution()
    assert solution.intersect([1, 2, 1, 1], [2, 2]) == [2]
    assert solution.intersect([1, 2, 2, 1], [2, 2, 2]) == [2, 2]

    print('self test passed')

if __name__ == '__main__':
    test()
