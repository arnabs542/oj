#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
50. Pow(x, n)

Total Accepted: 122876
Total Submissions: 452328
Difficulty: Medium
Contributors: Admin

Implement pow(x, n).

==============================================================================================
SOLUTION

1. Naive method:
        Simply multiply x n times
2. O(logN) method:
        Binary method
'''


class Solution(object):
    # 1.1 using built in pow function
    # myPow = pow
    # 1.2

    def _myPowBuiltin(self, x, n):
        return x ** n

    # 2 recursive
    def _myPowRecursive(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float

        38ms, beats 86.86%, 2016-10-07 10:51
        """
        if not x:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return 1.0 / self._myPowRecursive(x, -n)

        if n % 2 == 1:
            return x * self._myPowRecursive(x, n - 1)
        else:
            # n % 2 == 0
            # XXX: this is actually binary search
            return self._myPowRecursive(x * x, n / 2)

    # 3 iterative
    def _myPowIterative(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float

        Every number, including n, can be represented by a sum of power of 2. This is the
        concept of binary representation. So the order n can be rewritten, and we have relation
        between x^{2^(k+1)} and x^{2^k} given an integer k:
            x^{2^(k+1)} = x^{2^k * 2} = (x^{2^k})^2
        x ^ n = \prod_{k = 0}^{m-1} x^{a_k \times 2^k}
        """
        if not x:
            return 0
        if not n:
            return 1
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n:
            if n & 1:
                result *= x
            x *= x
            n = n >> 1
        return result

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float

        pow(0, 0) == 1?
        """
        # return self._myPowRecursive(x, n)
        return self._myPowIterative(x, n)
        pass


def test():
    print(Solution().myPow(-4, -1))
    print(Solution().myPow(3, 3))

if __name__ == "__main__":
    test()
