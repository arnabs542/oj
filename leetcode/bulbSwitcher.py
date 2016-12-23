#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
319. Bulb Switcher

Total Accepted: 32816
Total Submissions: 78511
Difficulty: Medium
Contributors: Admin

There are n bulbs that are initially off. You first turn on all the bulbs. Then, you
turn off every second bulb. On the third round, you toggle every third bulb (turning
on if it's off or turning off if it's on). For the ith round, you toggle every i bulb.
For the nth round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Given n = 3.

At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off].

So you should return 1, because there is only one bulb is on.

==============================================================================================
SOLUTION:

1. Brute-force: switch the bulbs round by round, O(N²).

2. Optimization?

Analysis:
1 -> 1 (1)
2 -> 2 (1 2)
3 -> 2 (1 3)
4 -> 3 (1 2 4)
5 -> 2 (1 5)
6 -> 4 (1 2 3 6)
7 -> 2 (1 7)
8 -> 4 (1 2 4 8)
9 -> 3 (1 3 9)

Only square root numbers are kept on.

Mathematical proof
----------------------------------------------------------------------------------------------
Actually, every operation is toggle. And the bulbs remaining on after n operations are those
have ODD NUMBER OF DIVISORS.

Let's say m-th bulb is on at the end, and its divisors, in ascending order, are d₁, d₂, ..., dₖ.
Then we have dᵢ * dⱼ = m, if and only if i + j = 1 + k.

In another word, d₁ * dₖ = d₂ * dₖ-₁ = ... = m

If k is odd, we we have the middle number c, where c = (1 + k) / 2, and d_c * d_c = m.
Given that, m is a square number.

Conclusion: Only SQUARE NUMBERS have ODD number of positive DIVISORS.

'''

import math

class Solution(object):

    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))


def test():
    solution = Solution()

    assert solution.bulbSwitch(1) == 1
    assert solution.bulbSwitch(9) == 3

    print("self test passed")

if __name__ == '__main__':
    test()
