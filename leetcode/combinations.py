#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
77. Combinations

Total Accepted: 94313
Total Submissions: 254463
Difficulty: Medium
Contributors: Admin

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

================================================================================================
SOLUTION
    Combinations are like permutations except that the elements are unordered. Different arrangement
of combination set correspond to different permutations, thereby producing duplicate combinations.
To address the unordered property, we can force the elements to be ORDERED, increasing or decreasing.

Treat this problem as a graph problem, and utilize the recurrence relation. Then we have
multiple approaches to resolve the problem.

1. Graph problem treatment - dfs(Depth First Search): recursion or stack iteration

Utilizing the recurrence relation between a sub-combination and its superset:
    any non-empty combination can be obtained by adding elements to one of its subset.
This process is equivalent to growing a graph from empty set vertex to vertices corresponding
to required combination.

2. Generative method: generate by lexicographical order or by 'next combination relation'
This method utilize the lexicographical recurrence relation between two successive combinations.

3. Bottom-up dynamic programming
Denote the combination of k elements given n as C(n, k).

C(n, k) = {B + x | B∈C(n, k-1) and x > max(B)}

'''
class Solution(object):

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # result = self._combineDfs(n, k)
        result = self._combineDfsOpt(n, k)
        # result = self._combineDP(n, k)
        # result = self._combineDfsIterative(n, k)
        print(n, k, '=>', result)
        return result

    def _combineDfs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]

        Fill k slots with n candidates one by one, recursively.
        Another recurrence relation could be C(n,k)=C(n-1,k-1)+C(n-1,k).
        """
        # FIXME: time limit exceeded. Optimization below
        result = []
        def dfs(combination, start):
            if len(combination) == k:
                result.append(combination)
                return
            for j in range(start, n): # the search range can be pruned
                # XXX: pass new object seems faster than restore state later
                dfs(combination + [j + 1], j + 1)

        dfs([], 0)

        return result

    def _combineDfsOpt(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]

        Fill k slots with n candidates one by one, recursively.
        Another recurrence relation could be C(n,k)=C(n-1,k-1)+C(n-1,k).

        While trying to add another element into a partial combination, the search range
        can actually be pruned. This is because we have to make sure there are enough
        elements to choose to fill the rest of slots.

        Assume the current partial combination already contains l elements, and we want to
        fill another slot . Then there are still k - l slots to fill. And there are at most
        n - i - 1 remaining elements left if we choose i for this slot.
        So condition n - i >= k - l must be satisfied. Then i <= n - k + l.
        """
        # FIXED: time limit exceeded
        result = []
        def dfs(combination, start):
            if len(combination) == k:
                result.append(combination)
                return
            for j in range(start, n - k + len(combination) + 1):
                # XXX: pass new object seems faster than restore state later
                dfs(combination + [j + 1], j + 1)

        dfs([], 0)

        return result

    def _combineDfsIterative(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]

        Use stack to emulate recursion
        """
        # TODO: instead of using combination list for each frame, use elements in the
        # stack to represent the current partial combination
        result = []
        stack = [([], 0)]
        while stack:
            combination, j = stack[-1]
            if len(combination) >= k or j >= n - k + len(combination) + 1: # stop criteria, recursive procedure returns
                if len(combination) == k:
                    result.append(combination)
                stack.pop()
                if not stack: break
                combination, j = stack.pop()
                stack.append((combination, j + 1))
            else:
                stack.append((combination + [j + 1], j + 1))
        return result

    def _combineDP(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]

        Dynamic programming. C(n, k - 1) => C(n, k)
        """
        # FIXME: actually, DP solution is even slower than recursive one
        # combinations = [[]]
        # for _ in range(1, k + 1):
        # combinations_new = []
        # for combination in combinations:
        # for j in range(combination[-1] +
        # 1 if combination else 1, n + 1):
        # combinations_new.append(combination + [j])
        # combinations = combinations_new

        combinations = [[]]
        for _ in range(k):
            combinations = [combination + [j]
                            for combination in combinations
                            for j in range(combination[-1] + 1 if combination else 1, n + 1)]
        return combinations

    def _combineGenerateNext(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # TODO

    def _combineLexicography(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # TODO

def test():
    solution = Solution()

    assert solution.combine(0, 0) == [[]]
    assert solution.combine(3, 0) == [[]]
    assert solution.combine(5, 1) == [[1], [2], [3], [4], [5]]
    assert solution.combine(3, 2) == [[1, 2], [1, 3], [2, 3]]
    # assert solution.combine(20, 16)

    print('self test passed')

if __name__ == '__main__':
    test()
