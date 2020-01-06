#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
392. Is Subsequence

Total Accepted: 15231
Total Submissions: 34789
Difficulty: Medium
Contributors: Admin

Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is
potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by
deleting some (can be none) of the characters without disturbing the relative positions
of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check
one by one to see if T has its subsequence. In this scenario, how would you change your
code?

==============================================================================================
SOLUTION:
1. Two pointers scanning.

2. For large list of incoming S, we may preprocess the string T to obtain a HASH TABLE of which
value = (key=char, value=list of ascending occurrence indices).

Then we can reduce the time complexity while querying whether a character in S exists in T.
'''

class Solution(object):

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return self.isSubsequenceTwoPointers(s, t)
        return self.isSubsequenceHash(s, t)

    def isSubsequenceTwoPointers(self, s, t):
        '''
        Greedy algorithm.
        '''
        i, j = 0, 0
        while i < len(s):
            while j < len(t) and t[j] != s[i]:
                j += 1
            if j >= len(t):
                return False
            else:
                i += 1
                j += 1
        return True

    def isSubsequenceHash(self, s: str, t) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool

        Use hashing for the follow-up problem.
        """
        occurrence = {}
        for i, c in enumerate(t):
            occurrence.setdefault(c, [])
            occurrence[c].append(i)

        start = 0
        for i, c in enumerate(s):
            found = False
            for j in occurrence.get(c, []):
                if j >= start:
                    start = j + 1
                    found = True
                    break
            if not found: return False
        return True


def test():
    """TODO: Docstring for test.
    :returns: TODO

    """
    solution = Solution()
    assert solution.isSubsequence('abc', 'ahbgdc')
    assert not solution.isSubsequence('axc', 'ahbgdc')

    print('self test passed')
    pass

test()
