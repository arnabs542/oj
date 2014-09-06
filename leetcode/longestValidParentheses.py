# -*-encoding:utf-8 -*-
'''
Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length
of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has
length = 2.

Another example is ")()())", where the longest valid parentheses substring
is "()()", which has length = 4.

'''


class Solution:
    # @param s,a string
    # @return an integer

    def longestValidParentheses(self, s):
        n = len(s)
        if n == 0:
            return 0
        # length[i]:length of longest valid parentheses ending with s[i]
        length = [0 for i in xrange(n + 1)]
        max_len = 0
        for i in xrange(1, n + 1, 1):
            l = 0
            j = i
            if s[i - 1] == '(':
                length[i] = 0
            else:
                while length[j - 1] > 0:
                    l += length[j - 1]
                    j -= l
                if j >= 2 and s[j - 2] == '(':
                    length[i] = l + 2 + length[j - 2]
                    if max_len < length[i]:
                        max_len = length[i]
                else:
                    length[i] = 0

        print length
        return max_len

if __name__ == "__main__":
    print Solution().longestValidParentheses(")()())")
    print Solution().longestValidParentheses("()(())")
