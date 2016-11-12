#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
190. Reverse Bits

Total Accepted: 82393
Total Submissions: 278941
Difficulty: Easy
Contributors: Admin

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer

'''

class Solution:
    # @param n, an integer
    # @return an integer

    def reverseBits(self, n):
        m = 0
        # must shift 32 times(bits), to obtain leading zeroes as trailing zeroes
        for _ in range(32):
            m = (m << 1) + (n & 0x1)
            n >>= 1

        # print(bin(m))
        return m

def test():
    solution = Solution()

    assert solution.reverseBits(43261596) == 964176192

    print('self test passed')

test()
