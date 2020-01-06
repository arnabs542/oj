#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
233. Number of Digit One

Total Accepted: 24063
Total Submissions: 89990
Difficulty: Hard
Contributors: Admin

Given an integer n, count the total number of digit 1 appearing in all non-negative integers
less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

Hint:

Beware of overflow.

===============================================================================================
SOLUTION

1. Brute force

Enumerate all numbers and count.

Complexity: O(N)

2. Perspective - count w.r.t positions - mathematically

NOT WORKING, NOT FEASIBLE

Divide the integers into groups.

Sum of number of digit one in ones place , \text{tens} place, \text{hundreds} place, ...

Add numbers having 1 on each place separately: 1 as least significant digit,
1 as tens place, 1 as hundreds place, ...

Seems not feasible?


Reference
https://leetcode.com/articles/number-of-digit-one

3. State transition - Dynamic programming

Idea is similar to binary indexed tree. We partition the integer range into several intervals
in log space. In log space means the partition is done with terms of power, based on 10, in
this case.

For example, 999 = 900 + 99 + 9 = 899 + 1 + 99 + 9.
Then we can find a way to reduce the problem and use some recurrence relation.

Recurrence relation can be built with respect to the partitions.

Let m = floor(log₁₀n), a, r = divmod(n, 10^m).

f(n) = f(10^m - 1) + f'.

And residual f', number of digits appearing in numbers within range [10^m, n], can be
computed recursively.

If a > 1, the most significant digit is bigger than 1.
f' = #(numbers like 1xx, in range [10^m, 19...9])x1 + f(1xx, 2xx,..., (a-1)xx) + f(r)
   = #(numbers like 1xx, in range [10^m, 19...9])x1 + (a-1)f(10^m - 1) + f(r)
   = 10^m + (a - 1)f(10^m -1) + f(r).

If a = 1, the most significant digit is 1.
f' = #(numbers like 1xxx, in range [10^m, 19...9])x1 + f(r)
   = (n - 10^m + 1) + f(r).

Cases to analyze
1
2
10
100
999
111
313


Complexity
O(log₁₀n)

'''

import math

class Solution(object):

    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = self._countDigitOne(n)

        print("n: ", n, ", result: ", result)

        return result

    def _countDigitOne(self, n):
        def dfs(x):
            if x < 1:
                return 0
            if x == 1:
                return 1
            m = math.floor(math.log10(x)) # 1
            a, r = divmod(x, 10 ** m) # 9, 9

            dp = dfs(10**m - 1) # dfs(9)
            if a > 1:
                dp += 10**m + (a - 1) * dfs(10**m - 1) + dfs(r) #
            elif a == 1:
                dp += (x - 10**m + 1) + dfs(r) # 0
            return dp
        return dfs(n) # dfs(99) =

    # TODO: optimization, cache?
    # TODO: more mathematical abstraction?

def test():

    solution: Solution = Solution()

    assert solution.countDigitOne(0) == 0
    assert solution.countDigitOne(-1) == 0
    assert solution.countDigitOne(1) == 1
    assert solution.countDigitOne(2) == 1
    assert solution.countDigitOne(9) == 1
    assert solution.countDigitOne(10) == 2
    assert solution.countDigitOne(11) == 4
    assert solution.countDigitOne(13) == 6
    assert solution.countDigitOne(99) == 20
    assert solution.countDigitOne(100) == 21
    assert solution.countDigitOne(10000) == 4001
    assert solution.countDigitOne(9999) == 4000
    assert solution.countDigitOne(11111) == 5560
    assert solution.countDigitOne(242242176) == 300427715

    print("self test passed!")

    pass

if __name__ == '__main__':
    test()
