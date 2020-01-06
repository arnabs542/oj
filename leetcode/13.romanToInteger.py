#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

13. Roman to Integer   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 119843
Total Submissions: 277454
Difficulty: Easy
Contributors: Admin
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.


==============================================================================================
SOLUTION:

The character value table:
Roman numeral (n)	Decimal value (v)
I	1
IV	4
V	5
IX	9
X	10
XL	40
L	50
XC	90
C	100
CD	400
D	500
CM	900
M	1000

The conversion algorithm:
    Keep track of the monotonicity of sequence, if a token has smaller value than its
adjacent latter letter, then it's sign is negative.

'''

class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        value = 0
        for i in range(len(s) - 1):
            sign = -1 if table[s[i]] < table[s[i + 1]] else 1
            value += sign * table[s[i]]

        value += table[s[-1]] if s else 0
        return value


def test():
    solution = Solution()

    assert solution.romanToInt("") == 0
    assert solution.romanToInt("V") == 5
    assert solution.romanToInt("IV") == 4
    assert solution.romanToInt("IIII") == 4
    assert solution.romanToInt("XIV") == 14
    assert solution.romanToInt("XVI") == 16
    assert solution.romanToInt("DCXXI") == 621

    print('self test passed')

if __name__ == '__main__':
    test()
