#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
377. Combination Sum IV

Total Accepted: 20453
Total Submissions: 49477
Difficulty: Medium
Contributors: Admin

Given an integer array with all positive numbers and no duplicates, find the number
of possible combinations that add up to a positive integer target.

Example:

    nums = [1, 2, 3]
    target = 4

    The possible combination ways are:
    (1, 1, 1, 1)
    (1, 1, 2)
    (1, 2, 1)
    (1, 3)
    (2, 1, 1)
    (2, 2)
    (3, 1)

    Note that different sequences are counted as different combinations.

    Therefore the output is 7.

Follow up:

What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

==============================================================================================
SOLUTION:
    Graph finding paths being able to go through an edge multiple times. Treat this as a
Directed Acyclic Graph. VERTICES are target number and its transited STATE, EDGES are number in
the given array.

The total number of valid paths is huge, we just need to count the number of them.

Define the STATE:
    The number of possible combinations that add up to current value.

STATE RECURRENCE RELATION:
    n_ways[state] = sum(n_ways[state - num] for num in nums if num <= state)

1. Recursive DFS with cache/memoization
The STATE in RECURSION can reside either function parameters or return values. And this problem
involves overlapping subproblems(with optimal substructure), so MEMOIZATION can speed it up. A
top STATE depends on all its subproblems(adjacent vertices).

2. Dynamic Programming?
In bottom-up fashion build the lookup table. But the lookup table might be SPARSE, because it
calculates lots of unnecessary intermediate STATE.

3. Breadth-first approach.
In this directed graph, a vertex's state depends on all vertices adjacent with it. So while
doing BFS, we mustn't proceed until all its predecessors are done for consistency. Because
numbers are positive, so predecessors are definitely smaller than descendants.

This indicates we can use a MIN-HEAP as the search frontier. At each time, pop out the smallest
state, add a number from the candidate array, push the new state into the heap. When search is
done, the target value's state what we want.
Still, we could just use a STATIC ARRAY of length as target number to reduce the heap maintaining
time complexity.

Follow up with negative numbers:
    If negative numbers are allowed, then the target value state transition graph is CYCLIC,
meaning there would be INFINITE paths through the circle. In graph traversal, we can restrict
every vertex is visited at most once to avoid such cycles. In this problem, we may want to
restrict that during state transition with possible combination sequence, the state may not be
duplicate. The top-down depth-first search solution will still do.
    Another problem is the target could be acquired by reducing a infinite large number.
    So, restrict one number can be used at most once can tackle this problem for sure.

'''

import heapq

class Solution(object):

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # return self.combinationSum4BFS(nums, target)
        return self.combinationSum4BFSOpt(nums, target)
        # return self.combinationSum4DFS(nums, target)

    def combinationSum4DFS(self, nums: list, target: int) -> int:
        cache = {0: 1}
        def dfs(value: int):
            if value not in cache:
                cache[value] = 0
                for _, num in enumerate(nums):
                    if num > value: continue
                    cache[value] += dfs(value - num)
                    pass
            return cache[value]
        return dfs(target)
    # TODO(done): follow up with negative numbers

    # TODO: convert the recursive procedure to iterative one?

    def combinationSum4BFS(self, nums: list, target: int) -> int:
        cache = {0: 1}
        frontier = [0] # min-heap as frontier data structure
        color = {0}
        while frontier:
            state = heapq.heappop(frontier)
            for num in nums:
                state_new = state + num
                cache[state_new] = cache.get(state_new, 0) + cache[state]
                if state_new > target:
                    continue
                if state_new not in color:
                    heapq.heappush(frontier, state_new)
                    color.add(state_new)
                pass
            pass
        print(cache)
        return cache.get(target, 0)

    def combinationSum4BFSOpt(self, nums: list, target: int) -> int:
        '''
        Dynamic Programming way to do breadth-first search.

        The search frontier is a single variable with index increasing along a static array.
        For each vertex(indicating a target state), update the number of combinations of
        current vertex's adjacent vertexes.

        Beats 99.87%, 2016-11-30 13:40.
        '''
        dp = [1] + [0] * target
        for i, n in enumerate(dp):
            if n == 0:
                continue
            for num in nums:
                if i + num <= target:
                    dp[i + num] += n
            pass
        print(dp)
        return dp[-1]


def test():
    solution = Solution()

    assert solution.combinationSum4([], 4) == 0
    assert solution.combinationSum4([1, 2], 4) == 5
    assert solution.combinationSum4([1, 2, 3], 4) == 7
    assert solution.combinationSum4([4, 2, 1], 32) == 39882198

    print('self test passed')

if __name__ == '__main__':
    test()
