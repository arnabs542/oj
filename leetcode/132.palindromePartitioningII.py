#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

==============================================================================================
SOLUTION

1. Brute force
Exhaust all possible partitions, and get the shortest list.

Complexity is same as "palindrome partitioning", O(n2ⁿ).

2. Dynamic Programming
In this problem, there is no need to find all partition configurations.
We only need to keep track of state of minimum cuts.


1) Define stet mincuts[j] as minimum cuts needed for substring s[0:j+1]

Complexity: O(N³) without building the palindrome look up table, because
checking palindrome takes O(N) on average.


2) Preprocess to build a palindrome look up table

Define state dp[i][j] as minimum cuts needed for substring s[i:j+1]
And define state pal[i][j] as whether substring s[i:j+1] is palindrome or not.

Then pal[i][j] depends on pal[i+1][j-1].
The look up table can be filled in a reverse row-major manner:
    for  i = N, N - 1, ... 1:
        for j = i, i + 1, ..., N:
            # state transition from pal[i+1][j-1]

Or, in a column major manner:
    for j = 1, 2, ..., N:
        for  i = 1, 2, ... j:
            # state transition from pal[i+1][j-1]

Recurrence relation similar to the matrix chain order problem
Recurrence relation:
    1) pal[i][j] = (s[i]==s[j] && pal[i+1][j-1] == True)
    2) mincuts[j] = min(mincuts[j], mincuts[i-1]+1) if pal[i][j] == True

Complexity: O(N²)

3. Breadth first search

Minimum cuts can be treated as shortest path in graph.

And shortest path problem can generally be solved with breadth first search.

Define state (i: starting index, step: number of cuts taken)


'''


class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = self._minCutDp(s)

        print(s, "result: ", result)

        return result

    def _minCutDp(self, s):
        pal = [[1 if j == i  else 0 for j in range(len(s))] for i in range(len(s))]
        mincuts = [x - 1 if x else 0 for x in range(len(s) + 1)]

        # XXX: trick, update the state transition table in column major manner
        for j in range(0, len(s), 1):
            for i in range(0, j + 1, 1):
                if s[i] == s[j] and ((j - i < 2) or pal[i + 1][j - 1]):
                    pal[i][j] = 1
                    mincuts[j + 1] = min(mincuts[j + 1], mincuts[i] + (i > 0))

        # print(mincuts)
        return mincuts[len(s)]


if __name__ == "__main__":
    solution = Solution()

    assert solution.minCut("") == 0
    assert solution.minCut("1") == 0
    assert solution.minCut("aa") == 0
    assert solution.minCut("aba") == 0
    assert solution.minCut("aab") == 1
    assert (Solution().minCut("aaaaaaaaaaaaaaaaaa") == 0)
        # Solution().minCut("adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece")
    assert (Solution().minCut("ababbbabbababa") == 3)
    assert (Solution().minCut("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "abbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 1)
