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

class memoize(dict):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kw):
        return self[args]

    def __missing__(self, key):
        ret = self[key] = self.func(*key)
        return ret

@memoize
def isMatchDPRecursive(s, p):
    '''
      Top-down dynamic programming, actually.

      Regular expressions have no prefix operators, BACKWARD MATCHING may suit better
      than FORWARD MATCHING.
    '''
    # print(s, p)
    if not p:
        return not s
    if not s:
        return set(p[1::2]) == {'*'} and not (len(p) % 2)
    char, exp_1, exp_2 = s[-1], p[-1], p[-2] if len(p) >= 2 else None
    if exp_1 in {'.', char}:
        return isMatchDPRecursive(s[:-1], p[:-1])
    elif exp_1 == '*':
        if exp_2 in {'.', char}:
            return isMatchDPRecursive(
                s, p[:-2]) or isMatchDPRecursive(s[:-1], p)
        else:
            return isMatchDPRecursive(s, p[:-2])
    else:
        return False

class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str, input text
        :type p: str, regex pattern
        :rtype: bool
        """
        return self.isMatchBacktrackRecursive(s, p)
        # return isMatchDPRecursive(s, p)

    def isMatchBacktrackRecursive(self, s, p, cache={('', ''): True}):
        """
        :type s: str
        :type p: str
        :rtype: bool

        Iteration where we can, recursion where we must.
        This recursive implementation is the slowest, without memoization, its time
        complexity grows exponentially.

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
        "a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*ac")
    assert solution.isMatch(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        "a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*a*ab")
    print('self test passed')
    pass

if __name__ == '__main__':
    import time
    t0 = time.clock()
    test()
    t1 = time.clock()
    print('{} ms'.format(1000 * (t1 - t0)))
