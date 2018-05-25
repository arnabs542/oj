#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
491. Increasing Subsequences

Given an integer array, your task is to find all the different possible increasing subsequences
of the given array, and the length of an increasing subsequence should be at least 2 .

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
Note:
  1. The length of the given array will not exceed 15.
  2. The range of integer in the given array is [-100,100].
  3. The given array may contain duplicates, and two equal integers should also be considered
as a special case of increasing sequence.

================================================================================
SOLUTION

1. Brute force
Enumerate all possible subsequences, and verify.

Complexity: O(2^N)

2. State transition with dynamic programming

However, there are some issues to concern.

How to deal with the duplicates elements?

Each increasing subsequence can be generated with an existing one S₀ and a new larger number p.
And duplicates occur when such combination is used more than once. To tackle that, we can use
a division point, just like partitioning in quick sort.

Procedure:
    Initialize an empty list, f, of increasing subsequences, including those with only one
element.
    Scan the list. For a new number p  Add [p] as an increasing subsequence to f. Scan f
from last second one to left to combine with an existing increasing subsequence to give a
new one, until a subsequence ending with p is found.

But this method still can't deal with the case where a number may occur multiple times. Then
it will produce multiple copies of sequence like [1, 1].

--------------------------------------------------------------------------------
How to prune duplicate sequences?

Use set of tuples?
Use auxiliary space to MARK VISITED?

To solve the problem of duplicates, we need to figure out how it happens!
Duplicates occur when a shorter sequence gets appended by the same value more than once.

Sequences are not easy to hash and memorize, but, their position in the output list,
is static. So represent visited state with tuple of:
    (i: increasing subsequence index, n: appended number)

Complexity: O(2ⁿ)

3. State transition as graph search - depth first search
Model this problem as a graph, where vertices are the integers given, and
edges are the AFTER relation between integer positions.

The problem is to find increasing path on the graph, which can be done with dfs.

Define state as a tuple:
    (s: increasing sequence, i: starting index of nums, a vertex)
Then the state transition happens when we have another element no less than the
last element of the current sequence.

The problem is, how to avoid duplicates?
How does the case of duplicates happen in this depth first search scenario?
Remember?

This scenario is similar to permutations containing duplicate number!
The duplicates occur when same value goes to a position more than once.

Filter the duplicate paths by filtering duplicate neighbour vertices.


'''

class Solution(object):

    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # result = self._findSubsequencesDP(nums)
        result = self._findSubsequencesDfs(nums)
        print(nums, '=>', result)
        return result

    def _findSubsequencesDP(self, nums):
        slices = []
        visited = set()
        for n in nums:
            for i in range(len(slices) - 1, -1, -1):
                if slices[i] and slices[i][-1] <= n and (i, n) not in visited:
                    visited.add((i, n))
                    slices.append(slices[i] + [n])
            if (-1, n) not in visited: slices.append([n])
            visited.add((-1, n))
        print('slices: ', slices)
        return [x for x in slices if len(x) >= 2]

    def _findSubsequencesDfs(self, nums):
        def dfs(seq, i):
            if len(seq) >= 2: result.append(seq)
            for j in range(i, len(nums)):
                if nums[j] in nums[i:j]: continue # duplicate: value already used
                if seq and nums[j] < seq[-1]: continue
                dfs(seq + [nums[j]], j + 1)
        result = []
        dfs([], 0)
        return result


def test():
    solution = Solution()

    assert sorted(solution.findSubsequences([])) == sorted([])
    assert sorted(solution.findSubsequences([1])) == sorted([])
    assert sorted(solution.findSubsequences([1, 1])) == sorted([[1, 1]])
    assert sorted(solution.findSubsequences([1, 1, 1])) == sorted([[1, 1], [1, 1, 1]])
    assert sorted(solution.findSubsequences([0, 1, 1, 1])) == sorted(
        [[0, 1], [0, 1, 1], [0, 1, 1, 1], [1, 1], [1, 1, 1]])
    assert sorted(solution.findSubsequences([1, 2, 3])) == sorted(
        [[1, 2], [1, 3], [2, 3], [1, 2, 3]])
    assert sorted(solution.findSubsequences(
        [1, 9, 3])) == sorted([[1, 9], [1, 3], ])
    assert sorted(solution.findSubsequences([4, 6, 7, 7])) == sorted([
        [4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7, 7], [4, 7, 7]])
    assert sorted(solution.findSubsequences([4, 6, 7, 7, 7])) == sorted(
        [[4, 6, 7, 7, 7], [4, 7], [4, 6], [4, 7, 7, 7], [6, 7], [6, 7, 7, 7],
            [7, 7], [7, 7, 7], [6, 7, 7], [4, 6, 7], [4, 6, 7, 7], [4, 7, 7]]
    )
    import yaml
    with open("./increasingSubsequences.json" , "r") as f:
        data = yaml.load(f)
    for r in data:
        assert sorted(solution.findSubsequences(r['input'])) == sorted(r['output'])

    # assert sorted(solution.findSubsequences([1, 2, 3, 1, 1])) == sorted([])
    # assert sorted(solution.findSubsequences(
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1])) == sorted([])

    print("self test passed")

if __name__ == '__main__':
    test()
