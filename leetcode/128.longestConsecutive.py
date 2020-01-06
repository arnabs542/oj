#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
128. Longest Consecutive Sequence

Total Accepted: 82393
Total Submissions: 238614
Difficulty: Hard
Contributors: Admin

Given an unsorted array of integers, find the length of the longest consecutive
elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

==============================================================================================
SOLUTION

1. Sort

Complexity: O(NlogN), O(N)

2.  Graph search - dfs
Treat it as a graph connected component problem.

Depth first search with hash table marking visited elements.

Complexity: O(N), O(N)

3. Union find

Treat this problem as finding a connected component in a graph.
Maintain a disjoint set for union find algorithm, and component size table.

Edge case: duplicate numbers, empty input

Complexity: O(N), O(N)

'''

from typing import List, Tuple, Dict, TextIO

class Solution(object):

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int

        """
        # return self.longestConsecutiveDFS(nums)
        return self.longestConsecutiveUnionFind(nums)

    def longestConsecutiveDFS(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Depth-first search
        """
        table = set(nums)
        length_max = 1

        for n in nums:
            if n not in table:
                continue
            length = 1
            left, right = n - 1, n + 1
            while left in table:
                length += 1
                table.remove(left)
                left -= 1
            while right in table:
                length += 1
                table.remove(right)
                right += 1
            table.remove(n)
            length_max = max(length, length_max)

        return length_max

    def longestConsecutiveUnionFind(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Union find
        """
        # DONE: union find algorithm
        parents = {} # parents mapping table
        def find(v):
            if parents[v] != v: parents[v] = find(parents[v])
            return parents[v]
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu < pv: parents[v] = pu
            elif pu > pv: parents[u] = pv

        sizes = {a: 1 for a in nums} # initially each component has size of 1
        max_size = 0
        for a in nums:
            if a in parents: continue # filter visited nodes
            parents[a] = a # mark visited, and maintain disjoint set
            if a - 1 in parents:
                sizes[find(a - 1)] += 1
                union(a - 1, a)
            if a + 1 in parents:
                sizes[find(a)] += sizes[find(a + 1)]
                union(a, a + 1)
            max_size = max(max_size, sizes[find(a)])
            # print(sizes, parents)

        return max_size

def test():
    solution = Solution()
    assert solution.longestConsecutive([]) == 0
    assert solution.longestConsecutive([1]) == 1
    assert solution.longestConsecutive([1, 4, 2]) == 2
    assert solution.longestConsecutive([1, 2, 0, 1]) == 3 # duplicate cases
    assert solution.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert solution.longestConsecutive([100, 4, 200, 1, 3, 2, 5]) == 5

    print('self test passed')

if __name__ == '__main__':
    test()
