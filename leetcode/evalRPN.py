'''
Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /.
Each operand may be an integer or another expression.

Some examples:
    ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
    ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
    '''

'''
Solution:
    Stack Data Structure.
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
    print s.evalRPN(["2", "1", "+", "3", "*"])
    print s.evalRPN(["4", "13", "5", "/", "+"])
    print s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
