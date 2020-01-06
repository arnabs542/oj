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

1. Treated as an Graph problem shortest path - breadth first search

Define state: step[i] as the minimums steps to reach index i.
State transition:
    step[i] = min(step[j] + 1) if j + nums[j] >= i, for any 0<=j<i;

Complexity:
O(V + E)=O(N²)

Optimization
------------
An observation is that, steps[i] <= step[j] for i <= j.
    Maintain a RANGE STATE as implicit search frontier and avoid exhaust every
possible previous index.

Complexity:
O(n), where n is the array size, and m is the average
array value.

Naive BREADTH FIRST SEARCH will exceed the time limit.

2. RANGE STATE bfs with further space optimization

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
        return self._jumpGreedyBFS(nums)
        # return self._jumpGreedyBFSOpt(nums)

    def _jumpGreedyBFS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rangeEnd, steps = 0, [0] * len(nums)
        for i, num in enumerate(nums):
            if i > rangeEnd: # can't reach so far
                return -1
            if rangeEnd >= len(nums) - 1: # already here
                break

            if i + num > rangeEnd: # range expands, state transition
                for j in range(rangeEnd + 1, min(i + num + 1, len(nums))):
                    steps[j] = steps[i] + 1
                rangeEnd = i + num
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
    assert solution.jump([3, 3, 3, 3, 1]) == 2
    assert solution.jump([2, 3, 1, 1, 4]) == 2
    assert solution.jump([4, 1, 1, 3, 1, 1, 1]) == 2
    assert solution.jump([2, 1, 1, 1, 1]) == 3
    print('self test passed')

test()
