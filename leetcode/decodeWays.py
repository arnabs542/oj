#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
91. Decode Ways

Total Accepted: 88906
Total Submissions: 482894
Difficulty: Medium
Contributors: Admin

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

SOLUTION:
1. Depth first search: recursive version gives time limit exceeded, maybe a iterative one
2. Dynamic Programming: let i denote the ith character in the string
    f[i] = (f[i - 1] if (s[i-1] in self.num2letter) else 0) +
            (f[i - 2] if (s[i-2:i] in self.num2letter) else  0)
'''


from _decorators import memoize

class Solution(object):

    def __init__(self):
        # self.numDecodings = memoize(self.numDecodings)
        pass

    num2letter = {}
    for i in range(26):
        num2letter[str(i + 1)] = chr(ord('a') + i)
        pass

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int

        Time Limit Exceeded or  maximum recursion depth error
        """
        # return self.numDecodingsDFS(s)
        # return self.numDecodingsDP(s)
        return self.numDecodingsDPRolling(s)

    def numDecodingsDFS(self, s):
        """
        :type s: str
        :rtype: int

        Time Limit Exceeded or  maximum recursion depth error
        """
        if not s:
            return 0
        elif len(s) == 1:
            return int(s in self.num2letter)

        n1 = s[0] in self.num2letter and self.numDecodings(s[1:])
        n2 = 0
        if len(s) == 2:
            n2 = s in self.num2letter and 1
        else:
            n2 = s[:2] in self.num2letter and self.numDecodings(s[2:])
        return n1 + n2

    # TODO: a iterative depth-first search implementation

    def numDecodingsDP(self, s):
        if not s:
            return 0
        f = [0] * (len(s) + 1)
        f[0] = 1
        f[1] = s[0] in self.num2letter and 1 or 0
        for i in range(2, len(s) + 1):
            f[i] = (f[i - 1] if (s[i-1] in self.num2letter) else 0) + \
                    (f[i - 2] if (s[i-2:i] in self.num2letter) else  0)
        print(f[-1])
        return f[-1]

    def numDecodingsDPRolling(self, s):
        if not s:
            return 0
        f0, f1 = 1, s[0] in self.num2letter and 1 or 0
        for i in range(2, len(s) + 1):
            f0, f1 = f1, (f1 if (s[i-1] in self.num2letter) else 0) + \
                    (f0 if (s[i-2:i] in self.num2letter) else  0)
        print(f1)
        return f1

def test():
    solution = Solution()
    assert solution.numDecodings('') == 0
    assert solution.numDecodings('0') == 0
    assert solution.numDecodings('023') == 0
    assert solution.numDecodings('1') == 1
    assert solution.numDecodings('12') == 2
    assert solution.numDecodings('122') == 3
    assert solution.numDecodings('129') == 2
    solution.numDecodings("101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010")
    print('self test passed')
    pass

if __name__ == '__main__':
    test()
