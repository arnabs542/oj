#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
216. Combination Sum III

Total Accepted: 51036
Total Submissions: 124186
Difficulty: Medium
Contributors: Admin

Find all possible combinations of k numbers that add up to a number n, given that only numbers
from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]

==============================================================================================
SOLUTION:
    Similar to Combination Sum II, except that the path depth is restricted.
    BACKTRACK with DEPTH-FIRST SEARCH.
    To implement BREADTH-FIRST SEARCH, it's more feasible to sort the candidates and pass the
start INDEX of valid candidates instead of the whole copy of candidates as STATE.
'''

class Solution(object):

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(target, path, start):
            """
            @target: target number
            @path: current tracking path
            @start: candidate start index

            Depth-first search backtracking.
            """
            if target == 0:
                if len(path) == k:
                    paths.append(list(path))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                path.append(candidates[i])
                dfs(target - candidates[i], path, i + 1)
                path.pop()
            pass
        paths = []
        candidates = list(range(1, 10))
        dfs(n, [], 0)
        print(paths)
        return paths

def test():
    solution = Solution()

    assert solution.combinationSum3(0, 0) == [[]]
    assert solution.combinationSum3(0, 1) == []
    assert solution.combinationSum3(1, 0) == []
    assert solution.combinationSum3(3, 7) == [[1, 2, 4]]
    assert solution.combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    assert solution.combinationSum3(3, 30) == []

    print('self test passed')

if __name__ == '__main__':
    test()
