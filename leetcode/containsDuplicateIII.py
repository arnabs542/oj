#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
220. Contains Duplicate III

Total Accepted: 40368
Total Submissions: 207935
Difficulty: Medium
Contributors: Admin

Given an array of integers, find out whether there are two distinct indices i and j
in the array such that the difference between nums[i] and nums[j] is at most t and
the difference between i and j is at most k.


===============================================================================================
SOLUTION:
    The naive solution would be scan the list, at the same time, check elements within range k
to see if their difference is at most t. And this is a O(nk) time complexity.
    To reduce the time complexity we can reduce O(k) to O(logk) or O(1).

    Utilizing buckets of size k, we can put the elements whose difference is at most t, the
SCALE FACTOR, in the same or adjacent buckets if they share same sign. Thus, querying the
existence of the target number can be done in O(1) time complexity.
'''

class Solution(object):

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # return self.containsNearbyAlmostDuplicateNaive(nums, k, t)
        return self.containsNearbyAlmostDuplicateBucket(nums, k, t)

    def containsNearbyAlmostDuplicateNaive(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # FIXME: O(n*k) exceeds time limit
        for i, _ in enumerate(nums):
            for j in range(1, min(k + 1, len(nums) - i)):
                # print(i, j)
                if abs(nums[i] - nums[i + j]) <= t:
                    return True

        return False

    def containsNearbyAlmostDuplicateBST(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # TODO: binary search tree

    def containsNearbyAlmostDuplicateBucket(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool

        Maintain buckets of size k, each bucket's key is num // (t + 1), and value
        is the corresponding number itself. If we have two numbers with their absolute
        difference at most t, then they will fall into the same or adjacent buckets.

        O(n) time complexity.
        """
        # TODO: bucket
        buckets = {}  # maintain k buckets
        if t < 0:
            return False
        for i, num in enumerate(nums):
            # shrink the value by (t + 1) scale
            bucket_id = num // (t + 1)
            # there might be negative number mapped in the buckets through negative bucket_id
            if (bucket_id in buckets and abs(buckets[bucket_id] - num) <= t) or\
               (bucket_id - 1 in buckets and abs(buckets[bucket_id - 1] - num) <= t) or \
               (bucket_id + 1 in buckets and abs(buckets[bucket_id + 1] - num) <= t):
                return True
            buckets[bucket_id] = num
            # the window size is consistent with the buckets size
            if len(buckets) > k:
                del buckets[nums[i - k] // (t + 1)]

        return False

def test():
    solution = Solution()
    assert not solution.containsNearbyAlmostDuplicate([0], 0, 0)
    assert not solution.containsNearbyAlmostDuplicate([], 0, 0)
    assert solution.containsNearbyAlmostDuplicate([3, 6, 0, 2], 2, 2)

    print('self test passed')

if __name__ == '__main__':
    test()
