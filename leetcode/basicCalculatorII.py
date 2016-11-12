#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
227. Basic Calculator II

Total Accepted: 33178
Total Submissions: 121211
Difficulty: Medium
Contributors: Admin

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces.
The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
===============================================================================================
'''

class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        numstack = []
        opstack = []
        token = ''

        def compute(opstack, numstack):
            num2, num1 = numstack.pop(), numstack.pop()
            op = opstack.pop()
            num3 = 0
            if op == '+':
                num3 = num1 + num2
            elif op == '-':
                num3 = num1 - num2
            elif op == '*':
                num3 = num1 * num2
            elif op == '/':
                num3 = num1 // num2
            numstack.append(num3)

        for i in range(len(s)):
            if '0' <= s[i] <= '9':
                token += s[i]
            elif s[i] in ('+', '-'):
                numstack.append((int(token)))
                token = ''
                while opstack:
                    # compute
                    compute(opstack, numstack)
                opstack.append(s[i])
            elif s[i] in ('*', '/'):
                numstack.append((int(token)))
                token = ''
                while opstack and opstack[-1] in ('*', '/'):
                    # compute
                    compute(opstack, numstack)
                opstack.append(s[i])

        if token:
            numstack.append(int(token))
            token = ''

        print(numstack, opstack)
        while opstack:
            compute(opstack, numstack)

        return numstack[0]

def test():
    solution = Solution()
    assert solution.calculate('3/2') == 1
    assert solution.calculate('3 + 2*2') == 7
    assert solution.calculate('3+5 / 2') == 5
    assert solution.calculate("1*2-3/4+5*6-7*8+9/10") == -24
    print('self test passed')

if __name__ == '__main__':
    test()
