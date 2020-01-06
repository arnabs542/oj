#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
334. Increasing Triplet Subsequence

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.

Credits:
Special thanks to @DjangoUnchained for adding this problem and creating all test cases.

================================================================================
SOLUTION

Find pattern sequence in array.

1. Brute force combination

Complexity: O(C(n, 3)) = O(n³).

2. Greedy strategy - interval with range [nums[i], nums[j]]

Maintain i, j pointers, and modify them under different circumstances.


"""

class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        result = self._increasingTripletStack(nums)

        print(nums, " => ", result)

        return result

    def _increasingTripletStack(self, nums):
        i0, j0 = -1, -1
        i1 = -1
        for k, _ in enumerate(nums):
            if i0 == -1:
                i0 = k # initialize 1
                continue
            if j0 == -1: # 2 not initialized
                if nums[k] > nums[i0]:
                    j0 = k
                else:
                    i0 = k
                continue

            if nums[k] > nums[j0]: return True # match
            if nums[i0] < nums[k] < nums[j0]: j0 = k # replace 2 with smaller one
            elif nums[k] < nums[i0]:
                if i1 == -1: i1 = k # hold: new minimal 1
                elif nums[i1] < nums[k]:
                    i0, j0 = i1, k # replace: 1, 2 with new pair
                    i1 = -1
                else: i1 = k

        return False

    # TODO: simpler implementation

def test():
    solution = Solution()

    assert solution.increasingTriplet([]) is False
    assert solution.increasingTriplet([1]) is False
    assert solution.increasingTriplet([1, 2]) is False
    assert solution.increasingTriplet([1, 2, 3]) is True
    assert solution.increasingTriplet([1, 2, 3, 4, 5]) is True
    assert solution.increasingTriplet([5, 4, 3, 2, 1]) is False
    assert solution.increasingTriplet([1, 2, -10, -8, -7]) is True

    print("self test passed!")

if __name__ == '__main__':
    test()

