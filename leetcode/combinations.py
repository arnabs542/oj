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
SOLUTION:
    Combinations are like permutations except that the elements are unordered. To address the
unordered property, we can force the elements to be increasing sequence to avoid duplicates.

    1. Top-down strategy: recursion or stack iteration
    2. Bottom-up strategy: generate by lexicographical order or by 'next combination relation'
    3. Bottom-up dynamic programming
'''
class Solution(object):

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = self.combineRecursion(n, k)
        # result = self.combineDP(n, k)
        print(result)
        return result

    def combineRecursion(self, n, k, combination=[], result=None):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]

        Fill k slots with n candidates one by one, recursively.
        Another recurrence relation could be C(n,k)=C(n-1,k-1)+C(n-1,k).
        """
        # TODO: top-down recursive solution
        if result is None:
            result = []

        if not k:
            result.append(list(combination))
            return result

        low = combination[-1] + 1 if combination else 1
        high = n - k + 1
        for i in range(low, high + 1):
            # XXX: pass new object seems faster than restore state later
            # combination.append(i)
            self.combineRecursion(n, k - 1, combination + [i], result)
            # combination.pop()

        return result

    def combineIterative(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]

        We can use Stack to emulate recursion or we can do this bottom-up like
        """
        # TODO:

    def combineDP(self, n, k):
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

    def combineGenerateNext(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # TODO

    def combineLexicography(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # TODO

def test():
    solution = Solution()

    assert solution.combine(5, 1) == [[1], [2], [3], [4], [5]]
    assert solution.combine(3, 2) == [[1, 2], [1, 3], [2, 3]]
    # assert solution.combine(20, 16)

    print('self test passed')

if __name__ == '__main__':
    test()
