#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
10. Regular Expression Matching

Total Accepted: 100621
Total Submissions: 437268
Difficulty: Hard

Implement regular expression matching with support for '.' and '*'.

  '.' Matches any single character.
  '*' Matches zero or more of the preceding element.

  The matching should cover the entire input string (not partial).

  The function prototype should be:
  bool isMatch(const char *s, const char *p)

  Some examples:
  isMatch("aa","a") → false
  isMatch("aa","aa") → true
  isMatch("aaa","aa") → false
  isMatch("aa", "a*") → true
  isMatch("aa", ".*") → true
  isMatch("ab", ".*") → true
  isMatch("aab", "c*a*b") → true

SOLUTION:
    1) backtracking: recursive
    2) backtracking: iterative
    2) dynamic programming
    3) NFA(nondeterministic finite automata)
'''

class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str, input text
        :type p: str, regex pattern
        :rtype: bool
        """
        return self.isMatchBacktrackRecursive(s, p)

    def isMatchBacktrackRecursive(self, s, p, cache={('', ''): True}):
        """
        :type s: str
        :type p: str
        :rtype: bool

        Iteration where we can, recursion where we must.
        76ms, 90.79%, 2016-10-11 09:06
        """
        i, j = 0, 0
        if (s, p) in cache:
            return cache[s, p]
        while i < len(s):
            if j >= len(p):
                return False
            # say s[i] == 'a'
            if s[i] == p[j] or p[j] == '.':
                # a* or .*
                if j + 1 < len(p) and p[j + 1] == '*':
                    # a*
                    cache[s, p] = self.isMatchBacktrackRecursive(s[i:], p[j + 2:]) or \
                        self.isMatchBacktrackRecursive(s[i + 1:], p[j:])
                    return cache[s, p]
                else:
                    # single a or .
                    i += 1
                    j += 1
            else:
                if (j + 1 < len(p) and p[j + 1] == '*'):
                    # c*
                    j += 2
                else:
                    # c
                    cache[s, p] = False
                    return False
        while j < len(p) and (
                j + 1 < len(p) and p[j + 1] == '*'):
            j += 2
        cache[s, p] = not p[j:]
        return cache[s, p]

    def isMatchBacktrackIterative(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # TODO: wrong answer, need backtracking

def test():
    solution = Solution()
    assert solution.isMatch("", "")
    assert not solution.isMatch("aa", "a")
    assert solution.isMatch("aa", "aa")
    assert solution.isMatch("", ".*")
    assert not solution.isMatch("", "aa")
    assert solution.isMatch("", ".*.*")
    # assert solution.isMatch("aa", "a*")
    assert solution.isMatch("aa", ".*")
    assert solution.isMatch("ab", ".*")
    assert solution.isMatch("aaaaaaaaaab", ".*b")
    assert not solution.isMatch("aab", ".*bb")
    # assert solution.isMatch("aa", "a**") # syntax error for non FSM solution
    assert solution.isMatch("aab", "c*a*b")
    assert solution.isMatch("aab", "c*a*b*")
    assert not solution.isMatch(
        "aaaaaaaaaaaaaaaab",
        "a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*c")
    print('self test passed')
    pass

if __name__ == '__main__':
    test()
