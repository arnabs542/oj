#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
168. Excel Sheet Column Title

Total Accepted: 79332
Total Submissions: 333787
Difficulty: Easy
Contributors: Admin

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
===============================================================================================
SOLUTION:

Base 26 number system. The difference is that the valid symbol ranges from [1, 26], not [0, 25]

n = Σaₖ26^(k-1), where k = 0, 1, ..., m.

Generate the title from the least significant place.
'''

class Solution(object):

    int2symbol = {}
    for i in range(26):
        int2symbol[i + 1] = chr(ord('A') + i)

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        title = ''
        while n:
            n, r = divmod(n, 26)
            if r == 0: # there is no symbol representing zero
                r = 26
                n -= 1
            title = self.int2symbol[r] + title

        print(title)
        return title

def test():
    solution = Solution()

    assert solution.convertToTitle(26) == 'Z' # n = 1, r = 0
    assert solution.convertToTitle(1 * 26 + 1) == 'AA'
    assert solution.convertToTitle(1 * 26 + 2) == 'AB'
    assert solution.convertToTitle(1 * 26 + 26) == 'AZ'
    assert solution.convertToTitle(25 * 26 + 26) == 'YZ'
    print('self test passed')

if __name__ == '__main__':
    test()
