#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
400. Nth Digit

Total Accepted: 11854
Total Submissions: 38803
Difficulty: Easy
Contributors: Admin

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 2³¹).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is
part of the number 10.


==============================================================================================
SOLUTION

DIVIDE the sequence into groups.

Count of numbers with length of
1 digit: 9
2 digit: 90
3 digit: 900
4 digit: 9000
...
n digit: 9e(n - 1)

Then the cumulative numbers, composed of numbers with no more than n digits, is
C(n) = 9 + 9 * 10 + ... + 9 * 10 ^ (n - 1), n = 1, 2, ...

Number of digits so far S(n): 1 * 9 + 2 * 90 + 3 * 900 + ... + n * 9 * 10 ^ (n - 1)
This is a variant of geometric progression, so the closed form equation can be obtained:

S(n) = n * 10 ^ n - (1 - 10 ^ n) / (1 - 10),
where n indicates that the current sequence is composed of all numbers with no more than n digits.

But equation S(n) = y is not easy to solve, so we can cumulatively calculate in a bottom-up
fashion.
1. Find the count of digits of the number where nth digit is from
2. Find the actual number
3. Find the nth digit


1. Brute-force, search starting with 1
O(N)

2. O(logN)

DIVIDE the numbers into groups of same length. Assume nth digit in the sequence is the n'th
digit in the current group, where every number is of length m.

n' = r (mod m) <=> n' - 1 = r - 1(mod m)

if n' = r (mod m), then nth digit is rth digit of the number where it's from.
But if r = 0, then it's the mth digit of the number.

'''

class Solution(object):

    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.findNthDigitLog(n)

    def findNthDigitLog(self, n):
        start, m = 1, 1 # start of group, the number length
        while True:
            groupSize = 9 * 10 ** (m - 1)
            if n <= m * groupSize: break
            start += groupSize
            n -= m * groupSize
            m += 1
        div, mod = divmod(n - 1, m)
        target = start + div
        return int(str(target)[mod])


def test():
    solution = Solution()

    assert solution.findNthDigit(1) == 1
    assert solution.findNthDigit(9) == 9
    assert solution.findNthDigit(10) == 1
    assert solution.findNthDigit(11) == 0
    assert solution.findNthDigit(12) == 1
    assert solution.findNthDigit(13) == 1
    assert solution.findNthDigit(65536) == 5

    print("self test passed")

if __name__ == '__main__':
    test()
