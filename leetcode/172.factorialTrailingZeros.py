#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
172. Factorial Trailing Zeroes

Total Accepted: 75324
Total Submissions: 218932
Difficulty: Easy
Contributors: Admin

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

SOLUTION
===============================================================================================

1. Naive solution: Compute the factorial, and then count trailing zeroes.

Complexity: O(n!)


--------------------------------------------------------------------------------
The factorial result can be factorized into products of prime factors. Zeroes occur
when prime factor 5 and 2 get multiplied, one zero for each pair. In a factorial's
prime factors, occurrences of 2 would literally be more than 5. So we just need
to compute the number of 5s in prime factors.

2. Iterate and count number of factor of 5s
For each i in range(1, n):
    count number of factor 5s in i, and add up

Complexity:
O(NlogN)=O(Nlog₅N)

3. Logarithm recurrence relation - f(n) -> f(n/5)

Denote the trailing zeroes of factorial of n by g(n).
Numbers with 5s as a factors must be 5's MULTIPLES, showing the 5's multiples:

6! = 1x2x...x (1x5) x6, f(6) = 1
11! = 1x2x...x (1x5) x6x...x (2x5) x 11, g(11) = 2 zeros
25! = 1x2x...x (1x5) x6x...x (2x5) x...x (3x5) x...x(4x5)...x(5x5), g(25) = 5+1=6 zeros

In order the find the number of 5s in prime factors, we can find those number of MULTIPLES OF 5
first. There would be at least FLOOR(N/5) multiples of 5. But still, those MULTIPLIERS OF 5 could
contribute 5 as prime factors too. Then the problem is as follows:
    We are here to find number of multiples of 5 in a series of numbers from 1 to FLOOR(n/5)
Apparently, this is a recursive definition and the base case is when some n/5 < 1.

To sum it up,
    g(n) = floor(n / 5) + g(floor(n/ 5)).

Complexity: O(logN), O(1).

'''

class Solution(object):

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.trailingZeroesFactorization(n)

    def trailingZeroesFactorization(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_zeros = 0
        while n:
            n //= 5
            n_zeros += n
        return n_zeros

def test():
    solution = Solution()
    assert solution.trailingZeroesFactorization(1) == 0
    assert solution.trailingZeroesFactorization(5) == 1
    assert solution.trailingZeroesFactorization(25) == 6
    assert solution.trailingZeroesFactorization(1000) == 249

    print('self test passed')

if __name__ == '__main__':
    test()
