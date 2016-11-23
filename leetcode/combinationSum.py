#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
39. Combination Sum

Total Accepted: 125587
Total Submissions: 358748
Difficulty: Medium
Contributors: Admin

Given a set of candidate numbers (C) and a target number (T), find all unique combinations
in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
  [
    [7],
    [2, 2, 3]
  ]

==============================================================================================
SOLUTION:
1. GRAPH finding paths problem, DEPTH-FIRST SEARCH or BREADTH-FIRST SEARCH.

Graph CONNECTIONS/EDGES correspond to the elements in the candidates set, and target number
TRANSITION STATES play the role of VERTICES.

Some cases:
    1. Duplicate state. Choosing different candidates with different order may give same state.
May be we could sort the elements in set, RESTRICT THE ORDER elements in candidate set to AVOID
DUPLICATES.
    2. All paths. To construct paths, we could do depth-first search on the stored PREDECESSORS.

2. Dynamic programming.
'''

class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.combinationSumBFS(candidates, target)

    def combinationSumBFS(self, candidates: list, target: int) -> list:
        '''
        state: (current target value, path) or just target value?
        '''
        paths = []

        def buildPath(path, vertex):
            '''
            Find all paths from source to destination using predecessors structure
            in a DEPTH-FIRST SEARCH manner.

            Prune duplicate paths.
            The elements in candidates set play the role as EDGES in the GRAPH.
            '''
            if vertex == target:
                paths.append(path)
                return
            for p in predecessors.get(vertex, []):
                edge = p - vertex
                if edge < path[-1] if path else 0:
                    continue
                buildPath(path + [edge], p)
            pass

        predecessors = {}
        frontier = [target]
        while frontier:
            state = frontier.pop(0)
            if state == 0:
                continue
            for _, num in enumerate(candidates):
                state_new = state - num
                if state_new < 0:
                    continue
                if state_new not in predecessors:
                    frontier.append(state_new)
                    # gray
                    predecessors[state_new] = []
                predecessors[state_new].append(state)
            pass

        print(predecessors)
        buildPath([], 0)
        print(paths)

        return paths

def test():
    solution = Solution()

    assert solution.combinationSum([], 9) == []
    assert solution.combinationSum([1], 1) == [[1]]
    assert solution.combinationSum([1], 0) == [[]]
    assert solution.combinationSum([2, 3, 6, 7], 7) == [[7], [2, 2, 3]]
    assert solution.combinationSum([2, 3, 4, 6, 7], 8) == [
        [4, 4], [2, 6], [2, 3, 3],
        [2, 2, 4], [2, 2, 2, 2],
    ]
    assert solution.combinationSum([10, 1, 2, 7, 6, 5], 8)

    print('self test passed')

if __name__ == '__main__':
    test()
