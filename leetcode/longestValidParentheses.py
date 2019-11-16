# -*-encoding:utf-8 -*-
'''
Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length
of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has
length = 2.

Another example is ")()())", where the longest valid parentheses substring
is "()()", which has length = 4.


Solution
================================================================================

1. Brute force
Exhaust and verify.

Complexity: (On^3)

2. Dynamic Programming
    Similar to Longest Common Substring problem,let length[i] be the
length of longest valid parentheses substring that ends with s[i-1].
length[i] = 0, if s[i-1] == '(',
length[i] = length[j-2] + 2 + l, l satisfies that s[i-l-1...i-2] is valid and s[j - 1] == '(',j = i - l

f(n) = max(
    f(n-2) + 2 if s[n-1] == '(' s[n] == ')',
    f(n-1) + 2 + f(n-l-1) where l = f(n-1) s[n] == ')',
)

Complexity
time : O(n)

3. Stack
In this problem, substring that forms a valid parentheses expression are deterministic.
All valid substrings can be found via a stack.

O(n), O(n)

4. Without explicit stack

O(n), O(1)

'''


class Solution:
    # @param s,a string
    # @return an integer

    def longestValidParentheses(self, s):
        result = self.longestValidParenthesesDP(s)
        print(s + " => " + str(result))

        return result

    def longestValidParenthesesDP(self, s):
        n = len(s)
        length = [0 for i in range(n + 1)] # longest length valid parentheses ending with s[i-1]
        maxLen = 0
        for i in range(1, n + 1, 1): # length
            if s[i - 1] == '(': continue

            j = i - length[i - 1] - 1 # backwind valid parenthesis pair ending with current ')'
            if j >= 1 and s[j - 1] == '(':
                length[i] = length[i - 1] + 2 + length[j - 1]
                maxLen = max(maxLen, length[i])

        # print(length)
        return maxLen

def test():
    solution = Solution()
    s = ""
    result = 0
    assert(solution.longestValidParentheses(s) == result)
    s = "("
    result = 0
    assert(solution.longestValidParentheses(s) == result)
    s = ")"
    result = 0
    assert(solution.longestValidParentheses(s) == result)
    s = "()"
    result = 2
    assert(solution.longestValidParentheses(s) == result)
    s = "())(())"
    result = 4
    assert(solution.longestValidParentheses(s) == result)
    s = "()(())"
    result = 6
    assert(solution.longestValidParentheses(s) == result)

    assert(solution.longestValidParentheses(")()())") == 4)
    assert(solution.longestValidParentheses("()(())") == 6)
    assert(solution.longestValidParentheses("()()((()") == 4)

    print("self test passed")

if __name__ == "__main__":
    test()
