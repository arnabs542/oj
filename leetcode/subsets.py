#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
78. Subsets

Total Accepted: 129614
Total Submissions: 360393
Difficulty: Medium
Contributors: Admin

Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

==============================================================================================
SOLUTION:

1. Dynamic Programming. Denote number of combinations of k given n by f(k, n), we have
combinatorial recurrence relation:
    f(k, n)
    = n!/(k!(n-k)!) = (n - k + 1) / k * n!/((k - 1)!(n - k + 1)!)
    = (n - k + 1) / k * f(k - 1, n)
    = f(k, n - 1) + f(k - 1, n - 1)

To generate all the subsets, denote combinations of k given by n by f(k, n), then we have

f(0, n) = {}
f(k, n) = {s + [num]| for s in f(k - 1, n), num in nums, if num > max(s)}

All subsets is just the superset of all combinations of k given n, k = 0, ..., n.

2. Recursion version dynamic programming

Pass STATES of subsets as function return value

Denote subsets of k given by n by f(k, n), then we also have:
    f(0, n) = {}
    f(k, n) = {s + [num]| for s in f(k - 1, n), num in nums, if num > max(s)}

3. Graph finding all vertices

Treat the problem as DYNAMIC GRAPH.

Pass STATES as function parameters.

Define the STATE AS ONE SUBSET of given collection. Then the state can transit from one state
to another, giving another subset. Store each such state in the output data structure.

Method 1: dfs
Method 2: bfs

4. Bit Manipulation?

Each ELEMENT in the collection could be viewed as a BIT, and number of subsets if 2^n. So it's
like a n-digit binary number, of which each bit is 0 or 1, indicating whether the corresponding
number exist in the current subset or not.

Take collection [1, 2, 3] for example, number 0=000, means the subset is empty {}, and 5=101
indicates the subset is {1, 3}(only the 0th bit and 2nd bit/number exists in the subset), and
7=111 corresponds to {1, 2, 3}.

Then we exhaust all possible subsets, for each subset, we check its corresponding binary
number's bits to determine whether the corresponding element exists in it or not.

'''
class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # return self.subsetsDP(nums)
        return self.subsetsBit(nums)
        # return self.subsetsDFS(nums)

    def subsetsDP(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output, subsets = [], []
        subsets.append([[]])
        for _ in range(1, len(nums) + 1):
            current = []
            for s in subsets[-1]:
                for n in nums:
                    if not s or n > s[-1]: current.append(s + [n])
            subsets.append(current)
        for s in subsets: output.extend(s)
        print(output)
        return output

    def subsetsDFS(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        def dfs(s: list, start):
            subsets.append(s)
            for i in range(start, len(nums)):
                dfs(s + [nums[i]], i + 1)
                pass
            pass
        dfs([], 0)
        print(subsets)
        return subsets

    # TODO: dfs iteratively

    def subsetsBit(self, nums) -> list:
        # DONE: bit manipulation?
        subsets = [[] for _ in range(1 << len(nums))]
        for i, _ in enumerate(subsets):
            for j, _ in enumerate(nums):
                if i & (1 << j): subsets[i].append(nums[j])
            pass
        print(subsets)
        return subsets


def test():
    solution = Solution()

    assert solution.subsets([]) == [[]]
    assert sorted(solution.subsets([1, 2, 3])) == sorted([
        [],
        [1], [2], [3],
        [1, 2], [1, 3], [2, 3],
        [1, 2, 3]])

    print('self test passed')

if __name__ == '__main__':
    test()
