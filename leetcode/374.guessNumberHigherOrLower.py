#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
374. Guess Number Higher or Lower

Total Accepted: 32685
Total Submissions: 98199
Difficulty: Easy
Contributors: Admin

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!

Example:

n = 10, I pick 6.

Return 6.

==============================================================================================
SOLUTION

1. Linear search

Complexity: O(n)

2. Binary search
Narrow down the search state space by half at each time.

Complexity: O(logn)


'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):


class Solution(object):

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = self._guessNumberBinarySearch(n)

        print(n, result)

        return result

    def _guessNumberBinarySearch(self, n):
        low, high = 1, n
        while low <= high:
            mid = (low + high) >> 1
            ret = guess(mid)
            if ret == 1:
                low = mid + 1
            elif ret == -1:
                high = mid - 1
            else:
                return mid

def test():
    solution = Solution()

    global guess

    guess = lambda x: -1 if 6 < x else (1 if 6 > x else 0)
    assert solution.guessNumber(10) == 6

    print("self test passed!")

if __name__ == '__main__':
    test()
