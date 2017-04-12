#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
357. Count Numbers with Unique Digits

Total Accepted: 22281
Total Submissions: 49914
Difficulty: Medium
Contributors: Admin

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100,
excluding [11,22,33,44,55,66,77,88,99])

Hint:

1. A direct way is to use the backtracking approach.
2. Backtracking should contains three states which are (the current number, number of steps to
get that number and a bitmask which represent which number is marked as visited so far in the
current number). Start with state (0,0,0) and count all valid number till we reach number of
steps equals to 10n.
3. This problem can also be solved using a dynamic programming approach and some knowledge
of combinatorics.
4. Let f(k) = count of numbers with unique digits with length equals k.
5. f(1) = 10, ..., f(k) = 9 * 9 * 8 * ... (9 - k + 2) [The first factor is 9 because a number
cannot start with 0].

==============================================================================================
SOLUTION:

1. Brute force counting every number within range .
O(N).

2. Dynamic Programming

Dynamic Programming recurrence relation:
f(0) = 1, f(1) = 9, ..., f(k) = 9 * 9 * 8 * ... (9 - k + 2) [The first factor is 9 because
a number cannot start with 0]

O(n). (could be reduced to O(1) with pigeonhole principle).

3. Graph model - backtracking
Append a digit at each time?
Vertex = number, edge = appending a digit to keep the number still in range

4. Lookup table
Dirichlet's DRAWER PRINCIPLE (pigeonhole principle):
    For n > 10(10 digits), there would always be duplicate digits in a n-digits number.
So we can build a lookup table. O(1).
'''

class Solution(object):

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.countNumbersWithUniqueDigitsDP(n)

    def countNumbersWithUniqueDigitsDP(self, n: int) -> int:
        f = [0] * (n + 1)
        f[0] = 1
        for i in range(1, n + 1):
            f[i] = 9
            for j in range(i - 1):
                f[i] *= 9 - j
        return sum(f)

    # TODO: BACKTRACKING?

def test():
    solution = Solution()

    assert solution.countNumbersWithUniqueDigits(0) == 1
    assert solution.countNumbersWithUniqueDigits(1) == 10
    assert solution.countNumbersWithUniqueDigits(2) == 91

    print('self test passed')

if __name__ == '__main__':
    test()
