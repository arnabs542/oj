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


SOLUTION
================================================================================

A STACK structure is associated with two characteristics of problems:
    1) Nested structure
    2) Backward processing due to priority, ordering.

1. Two STACKS: operators and operands, compute on the fly
Assume the infix expression is a string of tokens delimited by spaces. The operator tokens
are *, /, +, and -, along with the left and right parentheses, ( and ). The operand tokens are
numbers. The following steps will produce a string of tokens in postfix order.

1. Create an empty stack called `OPSTACK` for keeping operators. Create an empty list for output.
2. Convert the input infix string to a list by splitting.
3. Scan the token list from left to right.
    If the token is an operand, PUSH(append) it to the end of the output list.
    If the token is a left parenthesis, PUSH it on the `opstack`.
    If the token is an operator, *, /, +, or -, PUSH it on the `OPSTACK`. However, first remove ANY
operators already on the `opstack` that have higher or equal `PRECEDENCE` and append them to the
output list.
    If the token is a right parenthesis, meaning all operation after corresponding left parenthesis
can be carried out now, POP the `opstack` until the corresponding left parenthesis. Append each
operator to the end of the output list.
5. When the input expression has been completely processed, check the `opstack`. Any operators
still on the stack can be removed and appended to the end of the output list.

2. Tokenize and Convert to POSTFIX expression first
POSTFIX expression are much easier to evaluate in program, and it's essentially STACK structure.
So, b.t.w, it can be easily used to construct binary tree of expression.

The only difference from above method is for each operation that can be carried out, we don't
calculate it yet, and instead, pushing operators after its operands.

##############################################################################################
FOLLOW UP

Solve linear equation with one unknown(一元一次方程).
e.g. given a string: 3 + 4 * 5 / 6 = 7 + 8 * x / 5 - 6, solve the equation and return the x.

==============================================================================================
SOLUTION

The most simple linear equation takes form like: x = 0, x - 0 = 0.
To solve a linear equation by hand, is to extract the unknown variable from the expression.
Then it's all about SEPARATING constant terms and variables terms.
To separate operands of variables and constants, we construct the inverse operation to the
other side.

So, first of all, we compute the constant terms wherever we can.
Converting it to postfix expression may make it easier to illustrate the idea.

Build two POSTFIX STACK: left hand side and right hand side. And both of them have
already been reduced, meaning the constant terms are replaced with a scalar.
The reduced form may look like:
    infix = 1 + 2 * x + 3, postfix = 1 2 x * + 3 +

Then we take the outmost operation, and construct the inverse of it, push it into the
other POSTFIX STACK, and compute to reduce the equation.

left hand side = right hand side
3 + 4 * 5 / 6 = 7 + 8 * x / 5 - 6
To postfix,
3 4 5 * 6 / + = 7 8 x * 5 / + '6' -  # swap left
3 4 5 * 6 / + 6 + = 7 8 x * 5 / +  swap right
3 4 5 * 6 / + 6 + = '7' 8x 5 / +
3 4 5 * 6 / + 6 + 7 - = 8x '5' /
3 4 5 * 6 / + 6 + 7 - 5 * = '8'x
3 4 5 * 6 / + 6 + 7 - 5 * 7 / = x

1) A problem of infinite loop: the swap operation keeps spinning, swap to left and right,
back and forth. This is the case where both sides have variables.
Example:
    1 + x = 2 * x + 3 => 1 + x - 3 = 2 * x => 1 + x = 2 * x + 3 => ...
To solve this problem, we need to make use of COMMUTATIVE property of multiplication and add:
interchange the positions of variable and constant, let the variable be the second operand.
    1 + x = 2 * x + 3 => 1 + x = 3 + 2 * x => 1 = 3 + 2 * x - x = > 1 = 3 + x

2) Another problem :
    3 * x - 2 * x should be reduced! Make use of Object Oriented Design, encapsulating operators
and operands into Token objects.
class Token:
    def __init__(self):
        self.constant = 0
        self.variable = 'x'
And tokens containing variable terms may have both `constant` and `variable`. And define
custom arithmetic for Token objects.

3) How to inverse an outmost operation?
3 * 4 - 5 * 6 => 3 4 * 5 6 * -
In this case, the root operation's operands needs to be calculated, not a single number.
Could this be a problem for variables?
No! Because  we have already reduced the expression before. And the most complex expression
containing variable x would be like: 3 + 8x - 7 => 3 8x + 7 -
So we can always extract the outmost operation from expression containing x.


----------------------------------------------------------------------------------------------
To sum it up, we convert the left hand side and right hand side to two POSTFIX STACKS of
expression.
And there are several operations: CHANGE positions of operands, SWAP the inverse of
outmost operation to the other stack, COMPUTE.

Some thoughts: maybe a postfix tree to make it easier to extract hierarchical operation?

'''

class Solution(object):

    def tokenize(self, expression):
        # TODO: expression tokenization. Tokenize expression into operands and operators
        pass

    def infix2postfix(self, infix):
        """
        Convert a infix expression into postfix expression with STACK
        """
        # done: implement multiplication and division
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
