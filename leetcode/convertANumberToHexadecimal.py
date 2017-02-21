#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
405. Convert a Number to Hexadecimal

Total Accepted: 13207
Total Submissions: 32609
Difficulty: Easy
Contributors: Admin

Given an integer, write an algorithm to convert it to hexadecimal. For negative integer,
two’s complement method is used.

Note:

1. All letters in hexadecimal (a-f) must be in lowercase.
2. The hexadecimal string must not contain extra leading 0s. If the number is zero, it is
represented by a single zero character '0'; otherwise, the first character in the hexadecimal
string will not be the zero character.
3. The given number is guaranteed to fit within the range of a 32-bit signed integer.
4. You must not use any method provided by the library which converts/formats the number to
hex directly.

Example 1:

Input:
26

Output:
"1a"

Example 2:

Input:
-1

Output:
"ffffffff"

==============================================================================================
SOLUTION

1. Just keep dividing and converting the remainder.


'''

class Solution(object):

    digit2hex = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'a',
        11: 'b',
        12: 'c',
        13: 'd',
        14: 'e',
        15: 'f',
    }

    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        return self.toHexBit(num)

    def toHexBit(self, num: int) -> str:
        mask = 0xf
        hexadecimal = ''
        i = 0
        while num and i < 8: # at most 32 bits!
            d = num & mask # bit AND to get hexadecimal digit
            hexadecimal = self.digit2hex[d] + hexadecimal
            num >>= 4
            i += 1

        hexadecimal.strip('0')
        return hexadecimal or '0'

def test():
    solution = Solution()

    assert solution.toHex(26) == '1a'
    assert solution.toHex(-1) == 'ffffffff'

    print("self test passed")

if __name__ == '__main__':
    test()
