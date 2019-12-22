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

1. Brute force
For each element, count the smaller numbers after self.
Complexity: O(N²)

--------------------------------------------------------------------------------
SORTING algorithm
Problems involved with COMPARING VALUES are naturally connected to SORTING process.

The count of SMALLER numbers AFTER self is exactly the number of elements move to its left
in a STABLE SORT.

The key points are two relation: smaller and after.
To tackle the AFTER relation, we can adopt a BACKWARD manner.
To tackle the SMALLER relation,  obviously, it's order model.

2. Sort - Insert sort with binary search.

Inserting SORT backward. Then every time we try to insert a new element, all
previously sorted elements are all AFTER it. Now the task is to find how many of them
are smaller than it.

Inserting index of current element is the smaller numbers after self.
Use binary search for lower bound, where the new element will be inserted.
Finding lower bound is because the problem requires number smaller than, without equality.

Complexity: O(NlogN) ?
The array inserting operation is O(N), so the  complexity is still O(N²).

TODO: using builtin bisect module will be faster.

3. Divide and conquer - Sort - Merge sort

With merge sort, the array is always partitioned into two parts: the front part and
back part. And the back part elements are always AFTER the front part elements.

Then, the task is: for every element in the front part, count number of elements
smaller than it.
Since they are already sorted, it's easy to find the upper bound with linear scan.
For each merging process, count first then merge sorted arrays.

Backward merging is a similar idea like in "./MergeSortedArray.py".

Sort the indices array while comparing array values pointed by indices.

Complexity:
O(NlogN)

4. Sort - augmented binary search tree
Augment the binary search tree with rank to contain number of nodes.

Sort backward.

--------------------------------------------------------------------------------
COUNT AS SUM, RANGE QUERY of SUM

Range smaller => range sum query.

Convert counting problem into a summing problem, and use range query to query sum.

Counting of event can be modeled as sum mathematically:
    count(event) = \sum_{i=0}^{N}I(event)
where I is the binary INDICATOR FUNCTION, equal to 1 when event is true.

Then, to count the numbers smaller, the count can be quantified as
count(nums[j] < nums[i], j > i| i)
    = \sum_{j=i + 1}^{N}I(nums[j] < nums[i])
    = \sum_{k=min(nums)}^{nums[i] - 1}I(k \in nums[i + 1:])

In this way, problem of count of smaller numbers after self is transformed to
range sum, and the range interval is [min(nums), nums[i] -1]

Then the counting problem is converted to RANGE SUM QUERY!
Range sum query can be efficiently done with trees:
    binary indexed tree or segment tree.

The AFTER relation can be tackled by processing the list BACKWARD.
To count numbers smaller than nums[i], we do range sum query over
the indicator function of elements, where the range is
[min(nums), nums[i] - 1].

Process the array backward, for each element, the indicator function
has value 1, and update the range query tree.

Procedure
---------
for i = n, ..., 1:
    rangeSumQuery.update(nums[i], 1)
    rangeSumQuery.query(nums[i] - 1)

Since only the relative order of numbers matter, we can map the values
in nums to their order index. Then the maximum range is [1, N].

Procedure:
1) (Optional) Map input values to range [1, n], to space overhead
caused by sparsity of data.
2) Process the input backwards, for each value:
    - Use the value v as indices for range sum query. For each occurrence
count as 1.
    - count smaller: do range sum query for q(v-1).

Complexity:
O(NlogN)


4. Range query - Segment tree

Complexity: O(nlogn), O(n)

5. Range query - Binary indexed tree

Complexity: O(nlogn), O(n)


'''

from _tree import BinaryIndexedTree

class Solution(object):

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # result = self._countSmallerInsertSortBinarySearch(nums)
        # result = self._countSmallerMergeSort(nums)
        result = self._countSmallerBinaryIndexedTree(nums)

        print(nums, "=>", result)

        return result

    def _countSmallerInsertSortBinarySearch(self, nums: list) -> list:
        def searchInsert(arr, left, right, target):
            while left <= right:
                mid = (left + right) >> 1
                if target > arr[mid]: left = mid + 1
                elif target <= arr[mid]: right = mid - 1
                # XXX: exactly SMALLER numbers, so keep decreasing the right pointer

            return max(left, right)

        count = [0] * len(nums)
        nums_sorted = []
        for i, num in enumerate(reversed(nums)):
            pos = searchInsert(nums_sorted, 0, i - 1, num)
            count[len(nums) - 1 - i] = pos
            nums_sorted.insert(pos, num)
        # print(count)
        return count

    def _countSmallerMergeSort(self, nums: list) -> list:
        def mergeSort(arr, low, high):
            """
            sort arr in ascending order
            """
            if low >= high: return
            mid = (low + high) // 2
            mergeSort(arr, low, mid) # divide and conquer
            mergeSort(arr, mid + 1, high)

            left = list(arr[low:mid+1]) # copy lists
            right = list(arr[mid+1:high+1])

            top = high
            i, j = mid - low, high - mid - 1 # largest index in subarray
            while i >= 0 and j >= 0:
                if nums[left[i]] > nums[right[j]]: # compare with indices
                    arr[top] = left[i]
                    count[left[i]] += j + 1
                    i -= 1 # XXX: decrement it last...
                else:
                    arr[top] = right[j]
                    j -= 1
                top -= 1
            while i >= 0:
                arr[top] = left[i]
                i -= 1
                top -= 1
            while j >= 0:
                arr[top] = right[j]
                j -= 1
                top -= 1
                pass

        count = [0 for _ in range(len(nums))]
        indices = list(range(len(nums)))
        mergeSort(indices, 0, len(nums) - 1)
        return count

    # DONE: binary indexed tree
    def _countSmallerBinaryIndexedTree(self, nums):
        # class BinaryIndexedTree:
            # def __init__(self, n: int):
                # self._tree = [0 for _ in range(n + 1)]

            # def query(self, x):
                # s = 0
                # x += 1
                # while x:
                    # s += self._tree[x]
                    # x -= x & -x
                # return s

            # def update(self, x, diff):
                # x += 1
                # while x < len(self._tree):
                    # self._tree[x] += diff
                    # x += x & -x
            # pass

        rangeQueryTree = BinaryIndexedTree(len(nums))
        num2idx = {v: i for i, v in enumerate(sorted(list(set(nums))))}
        result = [0 for _ in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            result[i] = rangeQueryTree.query(num2idx[nums[i]] - 1)
            rangeQueryTree.update(num2idx[nums[i]], 1)
        return result

    # TODO: segment tree

def test():
    solution = Solution()

    assert solution.countSmaller([]) == []
    assert solution.countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0]
    assert solution.countSmaller([0, 2, 1]) == [0, 1, 0]

    print('self test passed')

if __name__ == '__main__':
    test()
