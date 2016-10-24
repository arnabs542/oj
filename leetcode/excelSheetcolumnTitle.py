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
    base 26 number system.
'''

class Solution(object):

    idx2char = {}
    for i in range(26):
        idx2char[i + 1] = chr(ord('A') + i)

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        title = ''
        while n:
            n, r = divmod(n, 26)
            if r == 0:
                r = 26
                n -= 1
            title = self.idx2char[r] + title

        print(title)
        return title

def test():
    solution = Solution()

    assert solution.convertToTitle(26) == 'Z'
    assert solution.convertToTitle(27) == 'AA'
    assert solution.convertToTitle(28) == 'AB'
    assert solution.convertToTitle(26 * 2) == 'AZ'
    assert solution.convertToTitle(26 * 26) == 'YZ'
    print('self test passed')

if __name__ == '__main__':
    test()
