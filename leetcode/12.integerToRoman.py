#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
12. Integer to Roman

Total Accepted: 87369
Total Submissions: 205402
Difficulty: Medium
Contributors: Admin

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

==============================================================================================
SOLUTION:

In a greedy strategy, fill the most significant place first.
Deal with different quotients respectively.

'''

class Solution(object):

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        table = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
        }
        roman = ''
        n = 1000
        while num:
            div, num = divmod(num, n)
            if 0 < div <= 3: # (0, 3]
                roman += table[n] * div
            elif div == 4:
                roman += table[n] + table[n * 5]
            elif 5 <= div < 9:
                roman += table[n * 5] + table[n] * (div - 5)
            elif div == 9:
                roman += table[n] + table[n * 10]
            n //= 10

        print(roman)
        return roman


def test():
    solution = Solution()

    assert solution.intToRoman(0) == ""
    assert solution.intToRoman(1) == "I"
    assert solution.intToRoman(3) == "III"
    assert solution.intToRoman(4) == "IV"
    assert solution.intToRoman(5) == "V"
    assert solution.intToRoman(7) == "VII"
    assert solution.intToRoman(8) == "VIII"
    assert solution.intToRoman(9) == "IX"
    assert solution.intToRoman(10) == "X"
    assert solution.intToRoman(12) == "XII"
    assert solution.intToRoman(13) == "XIII"
    assert solution.intToRoman(14) == "XIV"
    assert solution.intToRoman(15) == "XV"
    assert solution.intToRoman(16) == "XVI"
    assert solution.intToRoman(17) == "XVII"
    assert solution.intToRoman(18) == "XVIII"
    assert solution.intToRoman(19) == "XIX"
    assert solution.intToRoman(20) == "XX"
    assert solution.intToRoman(621) == "DCXXI"

    print('self test passed')

if __name__ == '__main__':
    test()
