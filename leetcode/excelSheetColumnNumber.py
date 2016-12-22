#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
171. Excel Sheet Column Number

Total Accepted: 110655
Total Submissions: 245793
Difficulty: Easy
Contributors: Admin
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

==============================================================================================
SOLUTION:
    Again, start with the least significant place.

'''

class Solution(object):

    symbol2int = {}
    for i in range(26):
        symbol2int[chr(ord('A') + i)] = i + 1

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        mul = 1
        for c in reversed(s):
            num += self.symbol2int[c] * mul
            mul *= 26
        return num

def test():
    solution = Solution()

    assert solution.titleToNumber('Z') == 26
    assert solution.titleToNumber('AA') == 27
    assert solution.titleToNumber('AB') == 28
    assert solution.titleToNumber('AZ') == 26 * 2
    assert solution.titleToNumber('YZ') == 26 * 26
    print('self test passed')

if __name__ == '__main__':
    test()
