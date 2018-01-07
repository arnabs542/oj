# -*-coding:utf-8 -*-

'''
88. Merge Sorted Array
Easy

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

================================================================================
SOLUTION

1. Inplace insert

Complexity: O(N²)

2. Backward insert

Initially, elements are located at the beginning of the arrays, so inserting
at the beginning involves moving all elements behind.

This moving complexity can be reduced by inserting backward!

Complexity: O(N)

'''


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        print(nums1, nums2)
        # result = self._mergeInsert(nums1, m, nums2, n)

        result = self._mergeBackward(nums1, m, nums2, n)

        print('after merge: \n', nums1)

    def _mergeInsert(self, nums1, m, nums2, n):
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                i = i + 1
            elif nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                m = m + 1
                i = i + 1
                j = j + 1

        if i < m:
            pass
        if j < n:
            while j < n:
                nums1.insert(i, nums2[j])
                m = m + 1
                i = i + 1
                j = j + 1

        return nums1

    def _mergeBackward(self, nums1, m, nums2, n):
        top = m + n - 1
        i = m - 1
        j = n - 1
        while i > -1 and j > -1:
            if nums1[i] >= nums2[j]:
                nums1[top] = nums1[i]
                i -= 1
            else:
                nums1[top] = nums2[j]
                j -= 1
            top -= 1
            pass
        while i > -1:
            nums1[top] = nums1[i]
            top -= 1
            i -= 1
            pass
        while j > -1:
            nums1[top] = nums2[j]
            top -= 1
            j -= 1
            pass
        pass

if __name__ == "__main__":
    print(Solution().merge([1, 3, 5, 0, 0, 0, 0], 3, [2, 4, 6, 8], 4))
