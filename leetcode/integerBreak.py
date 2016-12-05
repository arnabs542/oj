#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
343. Integer Break

Total Accepted: 31797
Total Submissions: 71403
Difficulty: Medium
Contributors: Admin

Given a positive integer n, break it into the sum of at least two positive integers and
maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.

Hint:

There is a simple O(n) solution to this problem.
You may check the breaking results of n ranging from 7 to 10 to discover the regularities.

==============================================================================================
SOLUTION:

1. Semi-brute-force: try all possible ways to divide evenly

    Principle 1: divide the integer as evenly as possible.
Mathematic Proof: given a + b = c, where a and b are variables and c is constant. Define product
function:
    f(a, b) = ab = a(c - a)

The maximum f is obtained where first derivative is zero:
    f'(a, b) = c - a -a = c - 2a = 0, i.e., a = b = c / 2

Then we try to break the integer by 2, 3, ..., n parts, and keep track of the largest product.

    Principle 2: While we are increasing the number of parts of the divided integer, if 1 occurs
as one factor, then we could always obtain a larger product by adding that 1 to another integer,
if the mutation is allowed.

So we will stop when we have 1 as factors.

2. Optimization for the above solution.

1) Derive with calculus derivatives

Let's say n is sufficiently large, then we can break n into x * (n/x). Define the product function

    f(x) = (n/x) ^ x,
    lnf(x) = xln(n/x)

Take the derivatives:

    1/f * f' = ln(n/x) + x * (x/n * (-n / x^2)) = ln(n/x) - 1

Let f' = 0:

    f' = f(ln(n/x) - 1) = 0,
    ln(n/x) = 1

then
    n / x = e = 2.71828...

This indicates that we want break n into natural logarithm constant.

But we have integers, so possible magic factor candidates are 2 and 3, where 2 < e < 3.

2) Inequation induction
For any number n, we can divide it into 3 and n - 3, if 3 * (n - 3) > n, then n > 4.5.
Which means, for any n >= 5, we can always divide it into numbers not greater than 3 to get a
larger product. Same for factor 2. So, we never need factors larger than 3.

Assume 3 * (n - 3) >= 2 * (n - 2), then n >= 5.
Then, for n >= 5, we just take 3 as factors as many as possible. For n = 3, 4, we
take 2 as factors. For n = 1, 2, just return 1.

'''

class Solution(object):

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return self.integerBreakEvenlyDivide(n)
        # return self.integerBreakMagicFactor(n)
        return self.integerBreakMagicFactorOpt(n)

    def integerBreakEvenlyDivide(self, n):
        max_so_far = 1
        for i in range(2, n):
            div, mod = divmod(n, i)
            product = 1
            for j in range(i):
                product *= div + (mod > j)
            max_so_far = max(max_so_far, product)
            if div == 1:
                break
        return max_so_far

    def integerBreakMagicFactor(self, n) -> int:
        '''
        Using magic number factor 3, O(N)
        '''
        product = 1
        if n <= 2:
            return 1
        elif n < 5:
            product = 2 * (n - 2)
        else:
            while n >= 5:
                n -= 3
                product *= 3
            product *= n

        return product

    def integerBreakMagicFactorOpt(self, n) -> int:
        '''
        Using magic number factor 3, O(logN)
        '''
        if n <= 2:
            return 1
        elif n < 5:
            return 2 * (n - 2)
        elif n % 3 == 0: # remainder
            return pow(3, n // 3)
        elif n % 3 == 1:
            return 4 * pow(3, (n - 4) // 3) # add 1 to another 3, giving factor 2*2=4
        else:  # n % 3 == 2
            return 2 * pow(3, (n - 1) // 3) # use remainder 2 as a factor: 2 * 3 > 1 * 4

def test():
    solution = Solution()

    assert solution.integerBreak(1) == 1
    assert solution.integerBreak(2) == 1
    assert solution.integerBreak(3) == 2
    assert solution.integerBreak(4) == 4
    assert solution.integerBreak(5) == 6
    assert solution.integerBreak(6) == 9
    assert solution.integerBreak(7) == 12
    assert solution.integerBreak(8) == 18
    assert solution.integerBreak(9) == 27
    assert solution.integerBreak(10) == 36

    print('self test passed')

if __name__ == '__main__':
    test()
