# -*-coding:utf-8 -*-
'''
47. Permutations II

Given a collection of numbers that might contain duplicates, return all
possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
    [1,1,2], [1,2,1], and [2,1,1].

================================================================================
SOLUTION

1. Brute force - permutation
Just like permutations without duplicates, generate all of them, and check
for duplicates.

Define state as a tuple:
    (permutation, i: next position to fill)

Complexity: O(n!)

2. Avoid duplicates on the fly

With a graph search(depth first search) algorithm, how does duplicates occur?
It occurs when we fill one position with same number more than once!

Well, then we avoid that, and problem is solved.

'''


class Solution(object):
    # @param nums,a list of integer
    # @return a list of lists of integers

    def permuteUnique(self, nums):
        result = self._permuteDfs(nums)

        print(nums, " => ", result)
        return result

    def _permuteDfs(self, nums):
        '''
        Method 1: Treat the problem as a DYNAMIC GRAPH

        Backtracking with DEPTH-FIRST SEARCH.

        When would the duplicate permutations emerge? When duplicate elements appear in the
        same place more than once!

        While swapping the element on ith index with another element of index j, check for
        duplicates in range [i, j]. If there are duplicates, then don't swap to produce
        duplicate permutations.
        '''
        permutations = []
        def dfs(start):
            if start == len(nums) - 1:
                permutations.append(list(nums))
                return
            for i in range(start, len(nums)):
                dup = False
                # NOTE: when start == i, this loop will not execute
                for j in range(start, i):
                    if nums[j] == nums[i]:
                        dup = True # TODO: avoid duplicate more efficiently?
                        break

                if dup: continue
                # swap
                nums[start], nums[i] = nums[i], nums[start]
                dfs(start + 1)
                # unswap to RESTORE STATES
                nums[start], nums[i] = nums[i], nums[start]

        dfs(0)
        return permutations

if __name__ == "__main__":
    Solution().permuteUnique([1, 1, 2, 2])
    Solution().permuteUnique([1, 2, 3])
    assert Solution().permuteUnique([1, 2, 2]) == [[1, 2, 2], [2, 1, 2], [2, 2, 1]]
    # 1 [2,1,2], 1 [2,2,1]
    Solution().permuteUnique([1, 1])
