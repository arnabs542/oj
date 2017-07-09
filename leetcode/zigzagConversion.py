#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like
this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

==============================================================================================
SOLUTION

ZigZag for "ABCDEFGHI", nRows=4 is pattern:
A       G
|     / |
B    F  H
|   /   |
C  E    I
| /
D

----------------------------------------------------------------------------------------------
Be aware of CORNER CASES!

When nRows=1, we can't walk downward or top left, only rightward.

'''

class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = self.convertWalk(s, numRows)
        print('zigzag result: ', result)
        return result

    def convertWalk(self, s, numRows):
        # TODO: optimize
        rows = [[] for _ in range(numRows)]
        i, j = 0, 0 # actually, j is not used
        n = 0
        state = 'down' # down, topRight
        while n < len(s):
            rows[i].append(s[n])
            n += 1
            # state transition: to next state
            if state == 'down':
                if i == numRows - 1:
                    if i == 0:
                        state = 'right'
                    else:
                        state = 'topRight'
            elif state == 'topRight':
                if i == 0:
                    state = 'down'
            else:
                pass

            # get next coordinate according to the moving direction state
            if state == 'down':
                i += 1
            elif state == 'topRight':
                i -= 1
            else:
                pass
        print(rows)
        result = ''.join([''.join(row) for row in rows ])
        return result

def test():
    solution = Solution()

    assert solution.convert("", 9) == ""
    assert solution.convert("", 1) == ""
    assert solution.convert("ABCD", 2) == "ACBD"
    assert solution.convert("ABC", 1) == "ABC"
    assert solution.convert("ABC", 2) == "ACB"
    assert solution.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert solution.convert("ABCDEFGHI", 4) == "AGBFHCEID"

    print("self test passed")


if __name__ == '__main__':
    test()
