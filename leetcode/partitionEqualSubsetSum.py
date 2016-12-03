#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
416. Partition Equal Subset Sum

Total Accepted: 8783
Total Submissions: 23758
Difficulty: Medium
Contributors: Admin

Given a non-empty array containing only positive integers, find if the array can be
partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
    Each of the array element will not exceed 100.
    The array size will not exceed 200.
Example 1:

    Input: [1, 5, 11, 5]

    Output: true

    Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

    Input: [1, 2, 3, 5]

    Output: false

    Explanation: The array cannot be partitioned into equal sum subsets.

==============================================================================================
SOLUTION:
    Get the total sum of the array, if it's even, then reduce the problem to the 'Combination Sum'
problem with target value as half the sum.

'''

class memoize(dict):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kw):
        return self[args]

    def __missing__(self, key):
        ret = self[key] = self.func(*key)
        return ret

class Solution(object):

    def canPartition(self, nums: list) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        # FIXME: maximum recursion depth exceeded
        @memoize
        def combinationSum(target, start=0) -> bool:
            if target == 0: return True
            for i in range(start, len(nums)):
                if nums[i] > target: continue
                ret = combinationSum(target - nums[i], i + 1)
                if ret: return True
            return False

        def combinationSumIterative(target, start=0) -> bool:
            # TODO: maybe bottom-up DFS/BFS
            pass

        def combinationSumDP(target):
            ''' Similar to knapsack problem. '''
            # TODO: optimize space complexity to one dimension
            if not nums: return target == 0
            m, n = len(nums) + 1, target + 1
            f = [[1 if j == 0 else 0 for j in range(n)] for _ in range(m)]
            for i in range(1, m):
                for j in range(1, n):
                    f[i][j] = f[i - 1][j] or (
                        j >= nums[i - 1] and f[i - 1][j - nums[i - 1]])
            return bool(f[-1][-1])

        total = sum(nums)
        return total % 2 == 0 and combinationSumDP(total // 2)

    # TODO: bitset ?


def test():
    solution = Solution()

    assert solution.canPartition([])
    assert not solution.canPartition([2])
    assert solution.canPartition([1, 5, 11, 5])
    assert not solution.canPartition([1, 2, 3, 5])
    assert solution.canPartition([1, 2, 3, 6])
    assert not solution.canPartition([1, 2, 3, 8])
    assert solution.canPartition([1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100,99,100])

    print('self test passed')

if __name__ == '__main__':
    test()
