#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
461. Hamming Distance

Total Accepted: 27790
Total Submissions: 39088
Difficulty: Easy
Contributors: Samuri

The Hamming distance between two integers is the number of positions at which the
corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.


==============================================================================================
SOLUTION

1. bit manipulation: XOR

'''

class Solution(object):

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return self.hammingDistanceXOR(x, y)

    def hammingDistanceXOR(self, x, y):
        z = x ^ y
        count = 0
        while z:
            count += 1
            z &= z - 1 # eliminate the last trailing 1, instead of shifting bit by bit
        return count


def test():
    solution = Solution()

    assert solution.hammingDistanceXOR(1, 4) == 2
    assert solution.hammingDistanceXOR(0, 4) == 1
    assert solution.hammingDistanceXOR(7, 0) == 3

    print("self test passed")

if __name__ == '__main__':
    test()
