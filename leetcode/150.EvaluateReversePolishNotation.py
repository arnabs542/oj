'''
150. Evaluate Reverse Polish Notation
Medium

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
Accepted
196.5K
Submissions
572.2K


Solution
================================================================================

There are different priority levels for different operators, and some calculations
need to be calculated BACKWARD, so use STACK.

'''


class Solution:
    # @param tokens,a list of string
    # @return an integer

    def evalRPN(self, tokens):
        # result = 0
        stack = []
        for i in range(len(tokens)):
            # print "operator: %d %s"%(i,tokens[i])
            if tokens[i] in ['+', '-', '*', '/']:
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == '+':
                    c = a + b
                elif tokens[i] == '-':
                    c = b - a
                elif tokens[i] == '*':
                    c = a * b
                elif tokens[i] == '/':
                    c = int(float(b) / a)

                stack.append(c)
            else:
                # print tokens[i]
                stack.append(int(tokens[i]))

        return stack[0]
    # return int(round(stack[0]))

if __name__ == "__main__":
    s = Solution()
    print(s.evalRPN(["2", "1", "+", "3", "*"]))
    print(s.evalRPN(["4", "13", "5", "/", "+"]))
    print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
