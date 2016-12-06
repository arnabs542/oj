#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
338. Counting Bits

Total Accepted: 56393
Total Submissions: 95207
Difficulty: Medium
Contributors: Admin

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num
calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

1. It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can
you do it in linear time O(n) /possibly in a single pass?
2. Space complexity should be O(n).
3. Can you do it like a boss? Do it without using any builtin function like
__builtin_popcount in c++ or in any other language.

Hint:

1. You should make use of what you have produced already.
2. Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate
new range from previous.
3. Or does the odd/even status of the number help you in calculating the number of 1s?

==============================================================================================
SOLUTION:

0  =    0,  0
1  =    1,  1
count 1
2  =   10,  1
3  =   11,  2
count 2 + 1
4  =  100,  1
5  =  101,  2
6  =  110,  2
7  =  111,  3
count 4 + 2 + 2 = 8
8  = 1000,  1, even
9  = 1001,  2, odd
10 = 1010,  2, even
11 = 1011,  3, odd
12 = 1100,  2, even
13 = 1101,  3, odd
14 = 1110,  3, even
15 = 1111,  4, odd
count 8 + 4 + 4 + 4 = 20

Regularities / pattern:
1. Difference of count of 1 bits of adjacent numbers in a group differs by at most 1.

2. 15 - 8 = 1111 - 1000 = 111 = 7.

For any number m in range [2 ^ k, 2 ^ (k + 1)), the leading 1 indicates the power of two, and
the remaining bits are just the same with m - 2 ^ n, which have already appeared before.
Denote the count of number as function f, then we have:
    f(i) = 1 + f(i - 2 ^ k), where k = number of valid bits in i.

Then we have RECURRENCE RELATION for dynamic programming.
Rewrite it:
    f(i) = i & 1 + f(i >> 1)

Actually, if we treat the problem as composed of overlapping subproblems, it may be easier
to find the right pattern.

'''

class Solution(object):

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # return self.countBitsDP(num)
        return self.countBitsDPOpt(num)

    def countBitsDP(self, num):
        n_bits = [0] * (num + 1)
        power = 1
        while power <= num:
            i = power
            while i <= num and i < power << 1:
                n_bits[i] = 1 + n_bits[i - power]
                i += 1
            power <<= 1
        return n_bits

    def countBitsDPOpt(self, num: int) -> int:
        f = [0] * (num + 1)
        for i in range(1, num + 1): f[i] = (i & 1) + f[i >> 1]

        return f

def test():
    solution = Solution()

    assert solution.countBits(0) == [0]
    assert solution.countBits(5) == [0, 1, 1, 2, 1, 2]
    assert solution.countBits(18) == [
        0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2]

    print('self test passed')

if __name__ == '__main__':
    test()
