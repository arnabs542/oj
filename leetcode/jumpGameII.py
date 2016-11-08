#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
45. Jump Game II

Total Accepted: 77874
Total Submissions: 300721
Difficulty: Hard
Contributors: Admin

Given an array of non-negative integers, you are initially positioned at the first index
of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1,
then 3 steps to the last index.)
===============================================================================================
SOLUTION:
    1. Treated as an Graph problem, naive BREADTH FIRST SEARCH will exceed the time limit.
    2. Greedy strategy. In a bottom-up manner, update the furthest index that we can reach by
jumping. Harnessing a data structure to maintain the steps to take to get a position. To
speed it up, we can just use a single variable to keep track of the current step range so that
we can determine when to update the number of steps so far.
'''

class Solution(object):

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self.jumpGreedyBFS(nums)
        return self.jumpGreedyBFSOpt(nums)

    def jumpGreedyBFS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        reach, steps = 0, [0] * len(nums)
        for i, num in enumerate(nums):
            if i > reach:
                return -1
            if reach >= len(nums) - 1:
                break

            if i + num > reach:
                for j in range(reach + 1, min(i + num + 1, len(nums))):
                    steps[j] = steps[i] + 1
                reach = i + num
            pass
        print(steps)
        return steps[-1]

    def jumpGreedyBFSOpt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stepEnd, steps, furthest = 0, 0, 0
        for i in range(len(nums) - 1):
            furthest = max(i + nums[i], furthest)

            if i == stepEnd:
                # update the number of steps when out of current range
                stepEnd = furthest
                steps += 1

                # early stop
                # if furthest >= len(nums) - 1:
                    # break
            pass
        print(steps)
        return steps if furthest >= len(nums) - 1 else -1

def test():
    solution = Solution()

    assert solution.jump([3, 4, 3, 2, 5, 4, 3]) == 3
    assert solution.jump([1]) == 0
    assert solution.jump([2, 3, 1, 1, 4]) == 2
    assert solution.jump([4, 1, 1, 3, 1, 1, 1]) == 2
    assert solution.jump([2, 1, 1, 1, 1]) == 3
    print('self test passed')

test()
