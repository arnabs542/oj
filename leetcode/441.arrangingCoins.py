#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
441. Arranging Coins

Total Accepted: 10380
Total Submissions: 28655
Difficulty: Easy
Contributors: Admin

You have a total of n coins that you want to form in a staircase shape, where every k-th
row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

==============================================================================================
SOLUTION


'''

class Solution(object):

    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return self.arrangeCoinsLinearSearch(n)
        return self.arrangeCoinsBinarySearch(n)

    def arrangeCoinsLinearSearch(self, n):
        i = 0
        while i * (i + 1) // 2 <= n:
            i += 1
        return i - 1

    def arrangeCoinsBinarySearch(self, n):
        low, high = 0, n
        while low <= high:
            mid = (low + high) >> 1
            required = mid * (mid + 1) // 2
            if required > n:
                high = mid - 1
            elif required < n:
                low = mid + 1
            else:
                return mid
        return min(low, high)


def test():
    solution = Solution()

    assert solution.arrangeCoins(1) == 1
    assert solution.arrangeCoins(5) == 2
    assert solution.arrangeCoins(8) == 3

    print("self test passed")

if __name__ == '__main__':
    test()
