#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
55. Jump Game

Total Accepted: 99185
Total Submissions: 341333
Difficulty: Medium
Contributors: Admin

Given an array of non-negative integers, you are initially positioned at the first
index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
===============================================================================================
SOLUTION:
    1. Treat it as a Graph problem, time limit exceeded
    2. Greedy strategy. In a bottom-up manner, update the furthest index that we can reach by
jumping.
'''

class Solution(object):

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # return self.canJumpBFS(nums)
        return self.canJumpGreedy(nums)

    def canJumpBFS(self, nums: list) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        # FIXME: time limit exceed, because it could reduce to O(N²) because exploring
        # neighbors could involve lots of branches
        frontier = [0]
        visited = {0}
        while frontier:
            pos = frontier.pop(0)
            if pos >= len(nums) - 1:
                return True
            for l in range(nums[pos], 0, -1):
                pos_new = pos + l
                if pos_new not in visited:
                    frontier.append(pos_new)
                    visited.add(pos_new)
                else:
                    # range already covered by previous transition
                    break
            pass
        return False

    def canJumpGreedy(self, nums):
        '''
        Another form of BREADTH-FIRST SEARCH, with no frontier structure because the graph is
        presented as a list. A single range variable could work as the indicator of exploration
        frontier.

        Then we can sweep the list once, step by step, maintaining a BOUNDARY VARIABLE at each step.
        This boundary variable `furthest` do the trick of SEARCH FRONTIER.
        '''
        furthest = 0
        for i, num in enumerate(nums):
            if i > furthest:
                return False
            if furthest >= len(nums) - 1:
                return True
            furthest = max(furthest, i + num)

def test():
    solution = Solution()

    assert solution.canJump([2, 3, 1, 1, 4])
    assert not solution.canJump([3, 2, 1, 0, 4])

    print('self test passed')

test()
