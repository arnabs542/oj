#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
423. Reconstruct Original Digits from English

Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
    Input contains only lowercase English letters.
    Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
    Input length is less than 50,000.

Example 1:
    Input: "owoztneoer"

    Output: "012"

Example 2:
    Input: "fviefuro"

    Output: "45"


================================================================================
SOLUTION

In this problem, the order is messed up, so the only feature is OCCURRENCE COUNT.

Then the objective is to find a combination of digits that contribute equal
histogram of the occurrence count of the letters.

In a mathematical perspective, this is a SYSTEM OF LINEAR EQUATIONS.

Where the constant matrix A, of 10x26, represent occurrence count of
each of 26 characters in each of 10 digits.
And the variable vector x, of 10x1, represents the occurrence count of each digits,
in the given input.
And there product Ax = b, is the occurrence count distribution/histogram of 26
characters in the input.

Reference:
https://en.wikipedia.org/wiki/System_of_linear_equations

1. Graph search - dfs


2. Mathematics - Gaussian elimination

3. Mathematics - Matrix inversion

4. Sparse solution

This system of linear equations have very sparse matrix in A.
Then we can use some observation to speed up the general Gaussian elimination process.

Some observation:
only "zero" contains "z", eliminated
only "two" contains "w", eliminated
only "four" contains "u", eliminated
only "six" contains "x", eliminated
only "eight" contains "g", eliminated
--
only "three" contains "r" except 0, 4, eliminated
only "five" contains "f", except "four", eliminated
only "seven" contains "s", except "six", eliminated
only "nine" contains "i", except 5, 6, 8
# only "ten" contains "t", except 2, 3, 8...
"one" contains "n", except 7, 9

Complexity:
O(N), where N is the length of the input string.


"""

from collections import Counter
# import numpy as np

class Solution:

    digitsMap = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = self._originalDigitsGaussianEliminationOpt(s)

        print(s, result)

        return result

    def _originalDigitsDfs(self, s):
        # TODO:
        pass

    def _originalDigitsGaussianElimination(self, s):
        # TODO:
        pass

    def _originalDigitsGaussianEliminationOpt(self, s):
        """
        Optimize Gaussian elimination algorithm with observation on sparse matrix
        """
        counter = Counter(s)
        nDigits = [0 for _ in range(26)]

        # one degree of freedom
        nDigits[0] = counter['z']
        nDigits[2] = counter['w']
        nDigits[4] = counter['u']
        nDigits[6] = counter['x']
        nDigits[8] = counter['g']

        nDigits[3] = counter['r'] - nDigits[0] - nDigits[4]
        nDigits[5] = counter['f'] - nDigits[4]
        nDigits[7] = counter['s'] - nDigits[6]
        nDigits[9] = counter['i'] - nDigits[5] - nDigits[6] - nDigits[8]
        nDigits[1] = counter['n'] - nDigits[7] - 2 * nDigits[9]

        result = ""
        for i, _ in enumerate(nDigits):
            # if nDigits[i] == 0: continue
            # for j in range(nDigits[i]):
            result += str(i) * nDigits[i]

        return result

def test():
    solution = Solution()

    assert solution.originalDigits("") == ""
    assert solution.originalDigits("owoztneoer") == "012"
    assert solution.originalDigits("fviefuro") == "45"

    print("self test passed!")

if __name__ == '__main__':
    test()
