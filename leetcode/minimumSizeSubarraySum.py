#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
209. Minimum Size Subarray Sum

Total Accepted: 60552
Total Submissions: 214185
Difficulty: Medium
Contributors: Admin

Given an array of n positive integers and a positive integer s, find the minimal
length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.


More practice:
    If you have figured out the O(n) solution, try coding another solution of which
the time complexity is O(n log n).

==============================================================================================
SOLUTION:

1. Dynamic Programing
STATE:
    (
    max_ending_here: eligible MAXIMUM SUBARRAY SUM ENDING WITH CURRENT POSITION,
    size_ending_here: the subarray's size,
    ).

Scan the array from left to right, at each time, compute for current subarray
`max_ending_here`.
If add anding the new element won't make size_ending_here exceed the (minimum size - 1)
found so far, then increase `size_ending_here` by 1. Else, `size_ending_here` stay the
same, but remove the leftmost element in the current subarray.

While current max_ending_here is not smaller than target value, continue substracting the
leftmost element from max_ending_here and decreasing the current subarray's size by 1.

Time Complexity: Amortized O(n).

By the way, we can define the STATE to be the begin and end of the current subarray.

2. Prefix sum with Binary Search?
'''

class Solution(object):

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        return self.minSubArrayLenDP(s, nums)

    def minSubArrayLenDP(self, s: int, nums: list) -> int:
        '''
        Code can be simpler for all positive situation.

        But the implementation below would generalize to negative integers case.
        '''
        max_ending_here, size_ending_here, size_min = 0, 0, len(nums) + 1
        for i, _ in enumerate(nums):
            if max_ending_here > 0:
                max_ending_here += nums[i]
                if size_ending_here < size_min - 1:
                    size_ending_here += 1
                else:
                    max_ending_here -= nums[i - size_ending_here]
            else:
                max_ending_here = nums[i]
                size_ending_here = 1

            while max_ending_here >= s:
                size_min = size_ending_here
                if size_min == 1:
                    return 1
                # decrease the minimum size ending here (size_min, upper bound) by 1
                size_ending_here -= 1
                max_ending_here -= nums[i - size_ending_here]
            pass
        print(size_min)
        return size_min if size_min <= len(nums) else 0

    # TODO: O(NlogN) solution

def test():
    solution = Solution()

    assert solution.minSubArrayLen(100, []) == 0
    assert solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3, 8]) == 1

    print('self test passed')

if __name__ == '__main__':
    test()
