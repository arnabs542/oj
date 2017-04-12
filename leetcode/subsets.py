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

1. 2D Dynamic Programming.
Denote number of combinations of k given n by f(k, n), we have combinatorial recurrence relation:
f(k, n)
    = n!/(k!(n-k)!) = (n - k + 1) / k * n! / ((k - 1)!(n - k + 1)!)
    = (n - k + 1) / k * f(k - 1, n)
    = f(k, n - 1) + f(k - 1, n - 1)

To generate all the subsets, denote combinations of k given by n by f(k, n), then we have

f(0, n) = {}
f(k, n) = {s + [num]| s ∈ f(k - 1, n), num ∈ nums, num > max(s)}

All subsets is just the superset of all combinations of k given n, k = 0, ..., n.

2. 1 dimensional dynamic programming

Denote all subsets of k from n by f(k, n), where n is constant, then we also have:
    f(0) = {}
    f(k) = {s + [num]| s ∈ f(k - 1), num ∈ nums}

We can use recursion by passing STATES of subsets as function return value.

3. Graph: traversing all vertices

Treat the problem as DYNAMIC GRAPH. The complete graph edges set is the given set, and
vertices are possible subsets. Available edges in set are different for each vertex.

Define state:
    State = (subset, available edges).
Then state transition happens given some edge.

The traversal can be implemented with both dfs and bfs. In recursive dfs, we can pass STATES
as function parameters.

4. Bit representation

A set with n elements has 2ⁿ subsets, which is related to number 2, of course, binary number
system.

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
        # subsets = self.subsetsDP(nums)
        # subsets = self.subsetsDP1D(nums)
        # subsets = self.subsetsBit(nums)
        subsets = self.subsetsDFS(nums)
        print(subsets)
        return subsets

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
        return output

    def subsetsDP1D(self, nums: list) -> list:
        subsets, new = [[]], []
        for n in nums:
            for s in subsets:
                new.append(s + [n])
            subsets.extend(new)
            new.clear()
        return subsets

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
        dfs([], 0)
        return subsets

    # TODO: dfs iteratively

    def subsetsBit(self, nums) -> list:
        # DONE: bit manipulation?
        subsets = [[] for _ in range(1 << len(nums))]
        for i, _ in enumerate(subsets):
            for j, _ in enumerate(nums):
                if i & (1 << j): subsets[i].append(nums[j])
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
