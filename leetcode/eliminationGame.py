#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
390. Elimination Game

There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.
Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
-   -   -   -   -
2 4 6 8
  -   -
2 6
-
6

Output:
6

================================================================================
SOLUTION

1. Brute force
Emulate the process.

Complexity
The elimination is performed until there is only 1 element left. And each
round of elimination takes out 1/2 of the elements.

The list scan is repeated for (log₂n) times, and each time has complexity of O(n),
so overall complexity is O(nlog₂n).

2. State transition with recurrence relation

Given integer set represented with range [1, 9],
[1, 9] => 2 * [1, 4], after 1 forward elimination

[1, 4] => 2 * [1, 3], after 1 forward elimination

--------------------------------------------------------------------------------
Define function f(interval, direction), which takes an interval of integers and
direction. Then it forms mutual recursion as follows:
    f([1, n], forward) = 2f([1, n//2], backward).

For a given interval [1, n], we have:
    f([1, n], backward) = n + 1 - f([1, n], forward)

Then, the recurrence relation is found!
And it can be implemented with mutual recursion, or reduced one recursion:
f([1, n], forward) = 2f([1, n//2], backward)
                   = 2(n//2 + 1 - f(n//2, forward)).

Recurrence relation is given by:
    f(n) = 2(m + 1 - f(m)) if n >= 2 else n, m = floor(n/2)


Complexity: O(logN), O(logN)

3. Math


################################################################################
FOLLOW UP

1. Josephus problem(https://en.wikipedia.org/wiki/Josephus_problem)

'''

class Solution(object):

    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        # result = self._lastRemainingNaive(n)
        # result = self._lastRemainingMutualRecursion(n)
        result = self._lastRemainingRecursion(n)

        print(n, " => ", result)

        return result

    def _lastRemainingNaive(self, n):
        """
        Define state:
        (
        i: start index,
        stride: stride,
        )
        for a progressive process.
        Define global state:
        (
        last remaining one,
        number of remaining,
        )
        """
        nums = list(range(1, n + 1))

        lastNumber = 1
        # forward = True
        nRemain = n # number of remaining numbers

        i = 0 # starting index
        stride = 1 # moving stride
        while nRemain > 1:
            # print(nums, i, stride)
            distance = 0
            while 0 <= i < n:
                if nums[i] == 0:
                    # lastNumber = nums[i] # skip one
                    i += stride
                    continue
                if nRemain == 1:
                    lastNumber = nums[i]
                    break
                if distance % 2 == 0:
                    nums[i] = 0 # eliminate
                    nRemain -= 1
                else:
                    lastNumber = nums[i]

                distance += 1
                i += stride

            # forward = not forward
            i = 0 if i == -1 else n - 1
            stride *= -1

        return lastNumber

    def _lastRemainingMutualRecursion(self, n):
        def forward(x):
            return 2 * backward(x//2) if x >= 2 else x

        def backward(x):
            return x + 1 - forward(x)

        return forward(n)

    def _lastRemainingRecursion(self, n):
        def dfs(x):
            return 2 * ((x >> 1) + 1 - dfs(x >> 1)) if x >= 2 else x
        return dfs(n)

    # TODO: mathematical formula

def test():
    solution = Solution()

    assert solution.lastRemaining(1) == 1
    assert solution.lastRemaining(2) == 2
    assert solution.lastRemaining(3) == 2
    assert solution.lastRemaining(4) == 2
    assert solution.lastRemaining(5) == 2
    assert solution.lastRemaining(9) == 6
    assert solution.lastRemaining(2201) == 1502
    assert solution.lastRemaining(65536) == 21846
    # assert solution.lastRemaining(1 << 31) == 2
    assert solution.lastRemaining(4_294_967_296) == 1431655766 # 2 ^ 32

    print("self test passed")


if __name__ == '__main__':
    test()
