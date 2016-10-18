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
    1) depth first search: recursive version gives time limit exceeded, maybe a iterative one will do
    2) Dynamic Programming: let i denote the ith character in the string
        dp[i] = (dp[i - 1] if (s[i-1] in self.num2letter) else 0) +
                (dp[i - 2] if (s[i-2:i] in self.num2letter) else  0)
'''

class memoize(dict):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kw):
        return self[args]

    def __missing__(self, key):
        ret = self[key] = self.func(*key)
        return ret

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
        # return self.numDecodingsDP(s)
        return self.numDecodingsDPRolling(s)

    def numDecodingsRecursion(self, s):
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
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = s[0] in self.num2letter and 1 or 0
        for i in range(2, len(s) + 1):
            dp[i] = (dp[i - 1] if (s[i-1] in self.num2letter) else 0) + \
                    (dp[i - 2] if (s[i-2:i] in self.num2letter) else  0)
            pass
        pass
        print(dp[-1])
        return dp[-1]

    def numDecodingsDPRolling(self, s):
        if not s:
            return 0
        dp0, dp1 = 1, s[0] in self.num2letter and 1 or 0
        for i in range(2, len(s) + 1):
            dp0, dp1 = dp1, (dp1 if (s[i-1] in self.num2letter) else 0) + \
                    (dp0 if (s[i-2:i] in self.num2letter) else  0)
        pass
        print(dp1)
        return dp1

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