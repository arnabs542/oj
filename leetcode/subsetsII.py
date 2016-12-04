#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
90. Subsets II

Total Accepted: 89377
Total Submissions: 267394
Difficulty: Medium
Contributors: Admin

Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

class Solution(object):

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.subsetsWithDupDFS(nums)

    def subsetsWithDupDFS(self, nums: list) -> list:
        nums.sort()
        permutations = []
        def dfs(s: list, start):
            permutations.append(s)
            for i in range(start, len(nums)):
                # filter duplicates
                if i > start and nums[i] == nums[i - 1]: continue
                dfs(s + [nums[i]], i + 1)
        dfs([], 0)
        print(permutations)
        return permutations

def test():
    solution = Solution()

    assert sorted(solution.subsetsWithDup([1, 2, 2])) == sorted([
        [],
        [1], [2],
        [1, 2], [2, 2],
        [1, 2, 2]
    ])

    print('self test passed')

if __name__ == '__main__':
    test()
