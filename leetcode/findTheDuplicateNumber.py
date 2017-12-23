#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
287. Find the Duplicate Number

Total Accepted: 49806
Total Submissions: 119477
Difficulty: Hard
Contributors: Admin

Given an array nums containing n + 1 integers where each integer is between 1 and n
(inclusive), prove that at least one duplicate number must exist. Assume that there
is only one duplicate number, find the duplicate one.

Note:
1. You must not modify the array (assume the array is read only).
2. You must use only constant, O(1) extra space.
3. Your runtime complexity should be less than O(n²).
4. There is only one duplicate number in the array, but it could be repeated more than once.

==============================================================================================
SOLUTION

To prove the existence of duplicate element, we can utilize pigeonhole principle.

1. Brute force method. For each number in [1, n], count its occurrence and return the one
with number of occurrence more than 1.

Complexity: O(N²), O(1)

2. Bucket
The previous solution doesn't incorporate the condition that all the integers are within
a specific RANGE [1, n]. With range defined, buckets come in handy!
But if we do it in a way like in Problem 'First Missing Positive', we need auxiliary space.

Complexity: O(N), O(N)

Can we make use of the condition that numbers are with in range [1, n] to reduce complexity?

3. Binary search
Binary search algorithm is trivial, but the key is to find the appropriate STATE to observe!

The COUNTING MODEL!

If there is not duplicates from 1 to m, then count of elements smaller than or equal to m
will be m.

Divide the array into two parts: [1, m], [m + 1, n].

Lemma
If the duplicate number is within range [1, m], then count of elements within range [1, m]
will be at least 1 + m.

Proof
Assume actual count of elements within range [1, m] is p < m + 1.

Since the array is divided into [1, m], [m + 1, n], and the duplicate is within [1, m].
So, there will be no duplicates within [m + 1, n], which can contain at most (n - m) elements.
Now, if actual count of elements within range [1, m] is p < m + 1, there will be
(n + 1 - p) > (n  + 1 - m - 1) > (n - m) elements within range [m + 1, n].

According to pigeonhole principle, there will be duplicate elements within range [m + 1, n],
which is contradict with the assumption!


With this lemme we can derive a search algorithm.
Assume there are k > (b - a + 1) elements within range [a, b]. Then divide the range [a, b],
into [a, c], [c + 1, b], where a <= c < b.
Then if the duplicate number is within range [a, c], there will be at most (b - c) elements
within range [c + 1, b], at least (k - b + c) elements within [a, c].
If the duplicate is within range [c + 1, b], there will be at most (c - a + 1) elements within
[a, c], and (k - c + a - 1) elements within [c + 1, b].

Now, it's time to do binary search.


4. Two pointers


Linked List Cycle model!

Reference: https://en.wikipedia.org/wiki/Cycle_detection

'''

class Solution(object):

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self._findDuplicateBucket(nums)
        return self._findDuplicateBinarySearch(nums)

    def _findDuplicateBucket(self, nums):
        pass

    def _findDuplicateBinarySearch(self, nums):
        if len(nums) <= 1: return

        n = len(nums) - 1 # 2
        total = n + 1
        low, high = 1, n # 1, 2

        while low < high:
            mid = (low + high) // 2 # 1
            count = 0
            # count now
            for num in nums:
                if low <= num <= mid:
                    count += 1 # 1
            if count >= total - (high - mid):
                total = count #
                high = mid #
            else:
                total -= count #
                low = mid + 1 # 2
        return low

    def findDuplicateTwoPointers(self, nums):
        # TODO: Two pointers
        pass

def test():
    solution = Solution()

    assert(solution.findDuplicate([]) is None)
    assert(solution.findDuplicate([1]) is None)
    assert(solution.findDuplicate([1, 1]) == 1)
    assert(solution.findDuplicate([2, 2, 1]) == 2)
    assert(solution.findDuplicate([2, 2, 2]) == 2)
    assert(solution.findDuplicate([1, 2, 1]) == 1)
    assert(solution.findDuplicate([1, 1, 1]) == 1)
    assert(solution.findDuplicate([2, 2, 1, 3]) == 2)

    print("self test passed")

if __name__ == '__main__':
    test()
