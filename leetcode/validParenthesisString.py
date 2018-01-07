#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
678. Valid Parenthesis String

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].

================================================================================
SOLUTION

Apparently, it involves reverse order processing, indicating STACK!

The problem is, how to deal with '*', it indicates multiple search branches.
Depth first search then!
Since we only need to verify it, we don't have to actually maintain a stack,
just to keep track of current occurrence number difference between '(' and ')'.

1. Brute force backtrack - depth first search

Complexity: O(2ⁿ)

2. Backtracking with pruning and memoize
Above brute  force backtracking will be pretty slow if the nested search
goes too deep.

And another major problem is, it involves lots of duplicate computations.

Complexity: O(NM), where M is the number of '*'?

3. Dynamic programming

4. Greedy strategy - reduce combination state range state

The character '*' indeed brings multiple search branches. However,
the states in those search BRANCHES will form a contiguous INTERVAL.

Then, tracking the interval state will do.

Complexity: O(N),  O(1)

"""

from _decorators import memoize

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # result = self._checkValidStringDfs(s)
        result = self._checkValidStringGreedy(s)

        print(s, result)

        return result

    def _checkValidStringDfs(self, s):
        @memoize
        def dfs(i, diff):
            while i < len(s):
                if s[i] == '(': diff += 1
                elif s[i] == ')': diff -= 1
                else:
                    while i < len(s) - 1 and s[i + 1] == '*': i += 1
                    return dfs(i + 1, diff) or dfs(i + 1, diff + 1) or dfs(i + 1, diff - 1)
                if diff < 0: return False
                i += 1

            return diff == 0
        return dfs(0, 0)

    # DONE: greedy strategy
    def _checkValidStringGreedy(self, s):
        low, high = 0, 0 # range of difference between occurrence count of '(' and ')'
        for i in range(len(s)):
            if s[i] == '(':
                low += 1
                high += 1
            elif s[i] == ')':
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1
            if high < 0: return False # absolutely less '(' than ')'
            low = max(low, 0) # XXX: greedily trim invalid range: can't have less '(' than ') at anytime
        print(low, high)
        return low == 0
        # return low <= 0 <= high

def test():
    solution = Solution()

    assert solution.checkValidString("")
    assert solution.checkValidString("()")
    assert solution.checkValidString("(*)")
    assert solution.checkValidString("(****************************)")
    assert solution.checkValidString("(*************************************************************)")
    assert solution.checkValidString("()*)**")
    assert not solution.checkValidString(")")
    assert not solution.checkValidString("*(")
    assert not solution.checkValidString("*)*(")
    assert not solution.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())")

    print("self test passed")

if __name__ == "__main__":
    test()
