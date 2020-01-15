/**
 *
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

FOLLOW UP
================================================================================
How to detect input expression syntax error?
Add error checking logic while computing.

 *
 */

#include <debug.hpp>

class Solution {
public:
    int calculate(string s) {
        int result;
        result = calculateStackOnePass(s);

        cout << s << " => " << result << endl;

        return result;
    }

    /**
     * General calculator supporting +-x/().
     */
    int calculateStackOnePass(string s) {
        auto compute = [](int x, int y, char op) -> int {
            if (op == '+') { return x+y; }
            else if (op == '-') return x-y;
            else if (op == '*') return x*y;
            else if (op == '/') return x/y;
            else {
                cerr << "not supported " << x << op << y << endl;
                return 0;
            }
        };
        stack<int> operands; // stack of operands: first in last out.
        stack<char> opStack; // stack of operators: first in last out.
        auto popCompute = [&compute, &operands, &opStack]() -> int {
            int y = operands.top(); operands.pop();
            int x = operands.top(); operands.pop();
            char op = opStack.top(); opStack.pop();
            //cout << "calculating " << x << op << y << " nops: " << opStack.size() << endl;
            int z = compute(x, y, op);
            operands.push(z);
            return z;
        };
        vector<char> digitList(0);
        s += '$'; // ending of file
        for (uint i = 0; i < s.size(); ++i) {
            char &si = s[i];
            if (si >= '0' && si <= '9') { // is digit, operand
                digitList.push_back(si);
            } else { // opStack
                if (digitList.size()) { // (1+2)-3
                    operands.push(stoi(string(digitList.begin(), digitList.end())));
                    digitList.clear();
                }

                if (si == '+' || si == '-') {
                    while (!opStack.empty() && opStack.top() != '(') { popCompute(); } // XXX: while
                    opStack.push(si);
                //}  if (si == '-') {
                } else if (si == '*' || si == '/') {
                    while (opStack.size() && (opStack.top() == '*' || opStack.top() == '/')) {
                        popCompute();
                    } // if will suffice
                    opStack.push(si);
                //} else if (si == '/') {
                } else if (si == '(') {
                    opStack.push(si);
                } else if (si == ')') {
                    while (opStack.size()) {
                        char op = opStack.top();
                        if (op == '(') {
                            opStack.pop();
                            break;
                        }
                        popCompute();
                    }
                } else if (si == '$') {
                    while (opStack.size()) { popCompute(); }
                }
            }
        }
        //if (digitList.size()) {
                    //int operand = stoi(string(digitList.begin(), digitList.end()));
                    //digitList.clear();
                    //operands.push(operand);
        //}
        //while (opStack.size()) { popCompute(); }

        return operands.size() ? operands.top():0;
    }
};


int test() {
    Solution solution;
    //assert(solution.infix2postfix("1 + 1") == [1, 1, "+"])
    //assert solution.infix2postfix("2 -1 + 2") == [2, 1, "-", 2, "+"]
    //assert solution.infix2postfix("2 -((1 + 2))") == [2, 1, 2, "+", "-"]
    //assert solution.infix2postfix("(1+(4+5+2)-3)+(6+8)") == [
        //1, 4, 5, "+", 2, "+", "+", 3, "-", 6, 8, "+", "+"]
    //cout << "infix2postfix test passed!" << endl;
    assert(solution.calculate("") == 0);
    assert(solution.calculate("1 + 1") == 2);
    assert(solution.calculate("2 -1 + 2") == 3);
    assert(solution.calculate("1 -(2 + (3))") == -4);
    assert(solution.calculate("2 -((1 + 2))") == -1);// 2 1 2; -((+ ))
    assert(solution.calculate("(1+(4+5+2)-3)+(6+8)") == 23);
    assert(solution.calculate("2/(4/2)") == 1);
    assert(solution.calculate("1*2-3/4") == 2);
    assert(solution.calculate("(1*2-(3)/4)") == 2);
    assert(solution.calculate("1*2+3/4") == 2);
    assert(solution.calculate("1*2-3/4+1*1") == 3);
    assert(solution.calculate("(8/1)/(4/2)/2") == 2);
    assert(solution.calculate("1*2-3/4+5*6-7*8+9/10") == -24);
    cout << "self test passed" << endl;

    // TODO: submit

    return 0;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
