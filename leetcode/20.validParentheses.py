#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
20. Valid Parentheses

Total Accepted: 149775
Total Submissions: 473368
Difficulty: Easy
Contributors: Admin

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid
but "(]" and "([)]" are not.

==============================================================================================
SOLUTION:
    STACK!
'''

class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pair = {')': '(', ']': '[', '}': '{'}
        for _, c in enumerate(s):
            if c in ('(', '[', '{'):
                stack.append(c)
            else:
                if not stack or stack.pop() != pair[c]:
                    return False
            pass

        return not stack


def test():
    solution = Solution()

    assert solution.isValid('()')
    assert solution.isValid('()[]{}')
    assert not solution.isValid('(]')
    assert not solution.isValid('([)]')

    print('self test passed')

if __name__ == '__main__':
    test()
