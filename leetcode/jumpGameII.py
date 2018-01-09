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

================================================================================
SOLUTION

Minimum number of jumps, is equivalent to shortest path, use breadth first search!

1. Treated as an Graph problem

Naive BREADTH FIRST SEARCH will exceed the time limit.

Complexity: O(V + E) = O(mn), where n is the array size, and m is the average
array value.

2. Keep track of RANGE STATE

In a bottom-up manner, update the furthest index that we can reach by
jumping.

Define state: (step, range)

Maintain the steps to take to get a position.
Use a single variable to keep track of the current step range so that
we can determine when to update the number of steps so far.

Complexity: O(N)

'''

class Solution(object):

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self._jumpGreedyBFS(nums)
        return self._jumpGreedyBFSOpt(nums)

    def _jumpGreedyBFS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stepEnd, steps = 0, [0] * len(nums)
        for i, num in enumerate(nums):
            if i > stepEnd:
                return -1
            if stepEnd >= len(nums) - 1:
                break

            if i + num > stepEnd:
                for j in range(stepEnd + 1, min(i + num + 1, len(nums))):
                    steps[j] = steps[i] + 1
                stepEnd = i + num
            pass
        print(steps)
        return steps[-1]

    def _jumpGreedyBFSOpt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prevFurthest, step, furthest = 0, 0, 0
        for i in range(len(nums) - 1):
            furthest = max(i + nums[i], furthest)

            if i == prevFurthest:
                # update the number of step when out of current range
                prevFurthest = furthest
                step += 1

                # early stop
                # if furthest >= len(nums) - 1:
                    # break
            pass
        print(step)
        return step if furthest >= len(nums) - 1 else -1

def test():
    solution = Solution()

    assert solution.jump([3, 4, 3, 2, 5, 4, 3]) == 3
    assert solution.jump([1]) == 0
    assert solution.jump([2, 3, 1, 1, 4]) == 2
    assert solution.jump([4, 1, 1, 3, 1, 1, 1]) == 2
    assert solution.jump([2, 1, 1, 1, 1]) == 3
    print('self test passed')

test()
