#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
201. Bitwise AND of Numbers Range

Total Accepted: 50034
Total Submissions: 150261
Difficulty: Medium
Contributors: Admin

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all
numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.

==============================================================================================
SOLUTION

Some heuristics shows that we might want to consider the intervals bounded by power of 2.

Denote f as the function that will solve the problem.

By analyzing some cases:

f(1) = 1
f(2, 3) = 2
f(4, 7) = 4
f(8, 15) = 8,
...

1. Range perspective
we can easily find that:
    f(2ⁿ, 2ⁿ+¹ - 1) = 2ⁿ

And we can find that, f(2^m, 2ⁿ+1 - 1) = 0 if n > m else 2^m.

1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024.
1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000

We can divide the range by powers of two. And compute the result of ranges bounded by
powers of two. Then compute the remaining(leading and trailing) intervals. The integers
within one remaining range must share a common most significant bit 1. Thus, we can
solve the problem recursively.

But, the procedure is too complicated

2. Bitwise perspective
In a bitwise perspective, we can reduce the problem bit by bit with shifting operation.

'''

class Solution(object):

    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.rangeBitwiseAndBitwise(m, n)

    def rangeBitwiseAndBitwise(self, m, n):
        return (self.rangeBitwiseAnd(m >> 1, n >> 1) << 1) if m < n else m


def test():
    solution = Solution()

    assert solution.rangeBitwiseAnd(0, 0) == 0
    assert solution.rangeBitwiseAnd(16, 31) == 16
    assert solution.rangeBitwiseAnd(16, 63) == 0

    print("self test passed")

if __name__ == '__main__':
    test()
