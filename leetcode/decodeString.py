#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
394. Decode String

Total Accepted: 10324
Total Submissions: 26118
Difficulty: Medium
Contributors: Admin

Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the
square brackets is being repeated exactly k times. Note that k is guaranteed
to be a positive integer.

You may assume that the input string is always valid; No extra white spaces,
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k. For example, there won't
be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

===============================================================================================
SOLUTION:
    There is nested structure, which indicates that this would involve RECURSION or STACK.
'''

class Solution(object):

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.decodeStringStack(s)

    def decodeStringStack(self, s):
        """
        :type s: str
        :rtype: str
        """
        # TODO: STACK based depth-first search
        output, opstack = [], []
        result, token = '', ''

        for _, c in enumerate(s):
            if c.isdigit():
                if token and not token.isdecimal():
                    output.append(token)
                    token = ''
                token += c
            elif c == '[':
                output.append(c)
                opstack.append(token)
                token = ''
            elif c == ']':
                # TODO(done): POP
                k = int(opstack.pop())
                while output and output[-1] != '[':
                    token = output.pop() + token
                if output: output.pop()
                token *= k
                output.append(token)
                token = ''
            else:
                token += c
            pass

        # token = int(opstack.pop()) if opstack else 1 * token
        output.append(token)
        result = ''.join(output)

        print(result)
        return result

def test():
    solution = Solution()

    assert solution.decodeString("xyz") == 'xyz'
    assert solution.decodeString("3[a]2[bc]") == 'aaabcbc'
    assert solution.decodeString("3[2[a]]") == 'aaaaaa'
    assert solution.decodeString("3[a2[c]]") == 'accaccacc'
    assert solution.decodeString("1[x]3[a2[c]]") == 'xaccaccacc'

if __name__ == '__main__':
    test()
