#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
67. Add Binary

Total Accepted: 116903
Total Submissions: 386742
Difficulty: Easy
Contributors: Admin

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

==============================================================================================
SOLUTION:

'''

class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        div, i = 0, 0
        for i in range(max(len(a), len(b)) + 1):
            x = int(a[len(a) - 1 - i]) if i < len(a) else 0
            y = int(b[len(b) - 1 - i]) if i < len(b) else 0
            div, mod = divmod(div + x + y, 2)
            result = str(mod) + result
        result = result.lstrip("0") or "0"
        print(result)
        return result

def test():
    solution = Solution()


    assert solution.addBinary("", "1") == "1"
    assert solution.addBinary("", "") == "0"
    assert solution.addBinary("11", "1") == "100"
    assert solution.addBinary("10", "1") == "11"
    assert solution.addBinary("1011", "11") == "1110"
    print("self test passed")

if __name__ == '__main__':
    test()
