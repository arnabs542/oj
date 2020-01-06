#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
115. Distinct Subsequences

Total Accepted: 61612
Total Submissions: 202557
Difficulty: Hard
Contributors: Admin

Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by
deleting some (can be none) of the characters without disturbing the relative positions
of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
    S = "rabbbit", T = "rabbit"

Return 3.

==============================================================================================
SOLUTION:
    Note, by 'subsequences of T', it means subsequences that are equal to T.
    T = "cat", S = "catapult", output is 3: “CATapult”, “CatApulT”, “CatApulT”
    Overlapping subproblems with optimal substructure, forming a GRAPH.

    1. Dynamic Programming

    2. Graph problem modeling with BREADTH-FIRST SEARCH or DEPTH-FIRST SEARCH
'''

class Solution(object):

    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        return self.numDistinctDP(s, t)

    def numDistinctDP(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int

        The state transition matrix depends on the previous value, not that straightforward
        to use sliding window.
        """
        m, n = len(s), len(t)
        f = [[0] * (n + 1) for _ in range((m + 1))]
        for i in range(m + 1): f[i][0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    f[i][j] = f[i - 1][j] + f[i - 1][j - 1]
                else:
                    f[i][j] = f[i - 1][j]

        return f[-1][-1]

def test():
    solution = Solution()

    assert solution.numDistinct("", "") == 1
    assert solution.numDistinct("whatever", "") == 1
    assert solution.numDistinct("", "whatever") == 0
    assert solution.numDistinct("catapult", "cat") == 3
    assert solution.numDistinct("rabbbit", "rabbit") == 3
    assert solution.numDistinct("aaaaa", "aa") == 10 # combinatorial number
    print('self test passed')

if __name__ == '__main__':
    test()
