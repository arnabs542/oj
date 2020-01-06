#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
97. Interleaving String

Total Accepted: 59392
Total Submissions: 251280
Difficulty: Hard
Contributors: Admin

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
===============================================================================================
SOLUTION:
    m, n, l = len(s1), len(s2), len(s3)
    Let i, j denote the substrings' length of s1 and s2, then their interleaving string can only
match string of length i + j.
    Then the problem is composed of sub-structures.
    1. Dynamic Programming
    2. Breadth-first search or depth-first search.
'''

class Solution(object):

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # return self.isInterleaveRecursive(s1, s2, s3)
        # return self.isInterleaveDP(s1, s2, s3)
        # return self.isInterleaveBFS(s1, s2, s3)
        return self.isInterleaveDFS(s1, s2, s3)

    def isInterleaveRecursive(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not (s1 and s2 and s3):
            return s3 == s1 + s2
        elif s3[-1] == s1[-1] != s2[-1]:
            return self.isInterleave(s1[:-1], s2, s3[:-1])
        elif s3[-1] == s2[-1] != s1[-1]:
            return self.isInterleave(s1, s2[:-1], s3[:-1])
        elif s3[-1] == s1[-1] == s2[-1]:
            return self.isInterleave(s1[:-1], s2, s3[:-1]) or\
                self.isInterleave(s1, s2[:-1], s3[:-1])
        else:
            return False

    def isInterleaveDP(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # TODO: space complexity can be optimized(sliding array)
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        f = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(0, m + 1):
            for j in range(0, n + 1):
                f[i][j] = s1[:i] + s2[:j] == s3[:i + j] if not i * j else \
                    s3[i + j - 1] == s1[i - 1] and f[i - 1][j] or \
                    s3[i + j - 1] == s2[j - 1] and f[i][j - 1]
        # print(f)
        return f[-1][-1]

    def isInterleaveDFS(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # TODO(done): depth-first search
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        # string lengths tuple as state
        stack, visited = [(0, 0)], set()
        while stack:
            (i, j) = state = stack.pop()
            if state == (m, n):
                return True
            # XXX: mark as visited while first encountered will speed up the search
            # since we are not finding all paths in a graph
            if i < m and s1[i] == s3[i + j] and (i + 1, j) not in visited:
                stack.append((i + 1, j))
                visited.add((i + 1, j))
            if j < n and s2[j] == s3[i + j] and (i, j + 1) not in visited:
                stack.append((i, j + 1))
                visited.add((i, j + 1))

        return False

    def isInterleaveBFS(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # TODO(done): breadth-first search
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        # string lengths tuple as state
        queue, visited = [(0, 0)], set()
        while queue:
            (i, j) = state = queue.pop(0)
            if state == (m, n):
                return True
            # XXX: mark as visited while first encountered will speed up the search
            # since we are not finding all paths in a graph
            if i < m and s1[i] == s3[i + j] and (i + 1, j) not in visited:
                queue.append((i + 1, j))
                visited.add((i + 1, j))
            if j < n and s2[j] == s3[i + j] and (i, j + 1) not in visited:
                queue.append((i, j + 1))
                visited.add((i, j + 1))

        return False


def test():
    solution = Solution()
    assert solution.isInterleave("aabcc", "dbbca", "aadbbcbcac")
    assert not solution.isInterleave("aabcc", "dbbca", "aadbbbaccc")
    assert solution.isInterleave("abc", "", "abc")
    assert not solution.isInterleave("abc", "", "abx")
    print('self test passed')

if __name__ == '__main__':
    test()
