#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
224. Basic Calculator

Total Accepted: 37194
Total Submissions: 151703
Difficulty: Hard
Contributors: Admin

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -,
non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.

===================================================================================================
SOLUTION:
    STACK data structure.

Assume the infix expression is a string of tokens delimited by spaces. The operator tokens
are *, /, +, and -, along with the left and right parentheses, ( and ). The operand tokens are
numbers. The following steps will produce a string of tokens in postfix order.

1. Create an empty stack called `OPSTACK` for keeping operators. Create an empty list for output.
2. Convert the input infix string to a list by splitting.
3. Scan the token list from left to right.
    If the token is an operand, PUSH(append) it to the end of the output list.
    If the token is a left parenthesis, PUSH it on the `opstack`.
    If the token is a right parenthesis, POP the `opstack` until the corresponding left parenthesis
is removed. Append each operator to the end of the output list.
    If the token is an operator, *, /, +, or -, PUSH it on the `OPSTACK`. However, first remove ANY
operators already on the `opstack` that have higher or equal `PRECEDENCE` and append them to the
output list.
5. When the input expression has been completely processed, check the `opstack`. Any operators
still on the stack can be removed and appended to the end of the output list.
'''

class Solution(object):

    def tokenize(self, expression):
        # TODO: expression tokenization. Tokenize expression into operands and operators
        pass

    def infix2postfix(self, infix):
        """
        Convert a infix expression into postfix expression with STACK
        """
        # TODO(done): implement multiplication and division
        # TODO: support negative number ' 1 ----- 3 = -2'
        post = []
        opstack = []
        i = 0
        token = ''
        for i in range(len(infix)):
            if infix[i] in ('+', '-'):
                if token:
                    post.append(int(token))
                    token = ''
                # XXX: pop and push all operators preceding over current one
                while opstack and opstack[-1] not in ('(', ):
                    post.append(opstack.pop())
                opstack.append(infix[i])
            elif infix[i] in ('*', '/'):
                if token:
                    post.append(int(token))
                    token = ''
                while opstack and opstack[-1] not in ('(', '+', '-'):
                    post.append(opstack.pop())
                opstack.append(infix[i])
            elif infix[i] == '(':
                opstack.append(infix[i])
            elif infix[i] == ')':
                if token:
                    post.append(int(token))
                    token = ''
                while opstack and opstack[-1] != '(':
                    post.append(opstack.pop())
                # pop '('
                opstack.pop()
            elif '0' <= infix[i] <= '9':
                token += infix[i]
            elif infix[i] == ' ':
                continue
            else:
                print('conversion to postfix expression failed')
                return ''
        pass

        if token:
            post.append(int(token))
        while opstack:
            if opstack[-1] != '(': post.append(opstack.pop())
        print(post)
        return post

    def postfix2value(self, postfix):
        """
        postfix expression to value
        """
        output = []
        i = 0
        for i in range(len(postfix)):
            if isinstance(postfix[i], int):
                output.append(postfix[i])
            else:
                # operator
                num2 = output.pop()
                num1 = output.pop()
                num3 = 0
                if postfix[i] in ('+', '-'):
                    num3 = num1 + num2 if postfix[i] == '+' else num1 - num2
                elif postfix[i] == '*':
                    num3 = num1 * num2
                elif postfix[i] == '/':
                    num3= num1 // num2
                output.append(num3)
        print(output[0])
        return output[0]


    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.postfix2value(self.infix2postfix(s))

def test():
    solution = Solution()
    assert solution.infix2postfix('1 + 1') == [1, 1, "+"]
    assert solution.infix2postfix('2 -1 + 2') == [2, 1, '-', 2, "+"]
    assert solution.infix2postfix('2 -((1 + 2))') == [2, 1, 2, '+', "-"]
    assert solution.infix2postfix("(1+(4+5+2)-3)+(6+8)") == [
        1, 4, 5, '+', 2, '+', '+', 3, '-', 6, 8, '+', '+']
    assert solution.calculate("1*2-3/4+5*6-7*8+9/10")
    print('infix2postfix test passed')
    assert solution.calculate('1 + 1') == 2
    assert solution.calculate('2 -1 + 2') == 3
    assert solution.calculate('2 -((1 + 2))') == -1
    assert solution.calculate("(1+(4+5+2)-3)+(6+8)") == 23
    assert solution.calculate("1*2-3/4+5*6-7*8+9/10") == -24
    print('self test passed')

if __name__ == '__main__':
    test()
