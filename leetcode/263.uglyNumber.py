#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
263. Ugly Number

Total Accepted: 79362
Total Submissions: 208465
Difficulty: Easy
Contributors: Admin

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For
example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
'''

class Solution(object):

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # return self.isUglyBruteForce(num)
        return self.isUglyFactorization(num)

    def isUglyFactorization(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for f in (2, 3, 5):
            while num % f == 0 < num:
                num //= f

        return num == 1

    def isUglyModulo(self, num):
        # TODO: modulo operation
        pass

    def getPrimes(self, num):
        prime = [True] * num

        i = 2
        while i * i < num:
            if not prime[i]:
                i += 1
                continue
            j = i * i
            while j < num:
                prime[j] = False
                j += i
            i += 1
            pass

        for i in range(2, num):
            if prime[i]:
                yield i

    def isUglyBruteForce(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # FIXME: memory exhaution
        if num in (1, 2, 3, 4, 5, 6):
            return True
        if num <= 0:
            return False
        primes = list(self.getPrimes(num + 1))
        start = primes.index(5)
        for i in range(start + 1, len(primes)):
            if num % primes[i] == 0:
                print(num, primes[i])
                return False

        return True


def test():
    solution = Solution()
    assert list(solution.getPrimes(13))
    assert len(list(solution.getPrimes(121))) == 30

    assert solution.isUgly(1)
    assert solution.isUgly(6)
    assert not solution.isUgly(7)
    assert solution.isUgly(8)
    assert not solution.isUgly(14)
    assert solution.isUgly(100)
    assert not solution.isUgly(214797179)
    print('self test passed')

if __name__ == '__main__':
    test()
