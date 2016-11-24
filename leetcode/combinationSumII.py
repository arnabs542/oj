#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
40. Combination Sum II

Total Accepted: 91735
Total Submissions: 298750
Difficulty: Medium
Contributors: Admin

Given a collection of candidate numbers (C) and a target number (T), find all unique
combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

==============================================================================================
SOLUTION:
    Similar to Combination Sum. But it's restricted to vertices being visited once only.
In other word, each PATH can only one EDGE at most once, and there are duplicate elements
(EDGES with same value).

    Thus, the CONNECTIVITY(set of EDGES) is DYNAMIC. When a path crosses an edge, the
connection/edge is removed temporarily. When a new path is being followed, the EDGE is
available again!.

1. One way to tackle the situation of DYNAMIC GRAPH is to BACKTRACK using DEPTH-FIRST SEARCH,
RESTORING STATES WHEN ADJACENT VERTICES ARE FINISHED EXPLORING.

2. To implement BREADTH-FIRST SEARCH, it's more feasible(faster) to sort the candidates and
pass the start INDEX of valid candidates instead of the whole COPY OF STATE.
    To print all paths, we have to STORE PATHS while doing BREADTH-FIRST SEARCH on DYNAMIC
GRAPH.
'''

class Solution(object):

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # return self.combinationSum2DFS(candidates, target)
        return self.combinationSum2BFS(candidates, target)

    def combinationSum2DFS(self, candidates: list, target: int) -> list:
        '''
        @path: list of edges/connections
        BACKTRACKING
        '''
        def dfs(candidates: list, target: int, path: list) -> list:
            if target == 0:
                # print('done', path)
                paths.append(list(path))
                pass
            seen = set()
            for i, num in enumerate(candidates):
                if num > target or (path and num > path[-1]) or num in seen:
                    continue
                path.append(num)
                candidates.pop(i)
                dfs(candidates, target - num, path)
                # XXX: backtracking, restore state. Alternatively, we can pass copies of state
                # TODO: could be optimized if we sort the candidates list and pass indices instead
                # of objects itself
                candidates.insert(i, path.pop())
                seen.add(num)
                pass

        paths = []
        dfs(candidates, target, [])
        print(paths)
        return paths

    def combinationSum2BFS(self, candidates: list, target: int) -> list:
        """
        BREADTH-FIRST SEARCH STORING PATHS

        beats 96.93%, 2016-11-23 19:48
        """
        candidates.sort(reverse=True)

        paths = []
        frontier = [(target, [], 0)]
        while frontier:
            state, path, start = frontier.pop(0)
            if state == 0:
                paths.append(path)
                continue
            seen = set()
            for i in range(start, len(candidates)):
                # XXX: BFS instead of backtracking to prune
                # pass sorted indices as STATE instead of the whole copy of large objects!
                state_new = state - candidates[i]
                if state_new < 0 or state_new in seen:
                    continue
                frontier.append((state_new, path + [candidates[i]], i + 1))
                seen.add(state_new)

        paths.sort()
        print(paths)

        return paths

def test():
    solution = Solution()

    assert solution.combinationSum2([], 9) == []
    assert solution.combinationSum2([1], 1) == [[1]]
    assert solution.combinationSum2([1, 1], 1) == [[1]]
    assert solution.combinationSum2([1, 1], 2) == [[1, 1]]
    assert solution.combinationSum2([2, 3, 6, 7], 7) == [[7]]
    assert solution.combinationSum2([2, 3, 4, 6, 7], 8) == [[6, 2]]
    assert solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == sorted([
        [7, 1], [6, 1, 1], [6, 2], [5, 2, 1]])

    print('self test passed')

if __name__ == '__main__':
    test()
