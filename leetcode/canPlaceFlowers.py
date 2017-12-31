#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
605. Can Place Flowers

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
  The input array won't violate no-adjacent-flowers rule.
  The input array size is in the range of [1, 20000].
  n is a non-negative integer which won't exceed the input array size.

================================================================================
SOLUTION

The greedy strategy can easily be proved that we can scan the list
from left to right, and place flowers where we can.

1. Brute force search

Complexity: O(2ⁿ)

2. Greedy strategy

If we have slot placable, like the middle one in [0, 0, 0], the using it will
be optimal.

Otherwise, if these all of these three are not used, then we apparently have
a more optimal solution by using one of them(the middle one).

If one of three is used, then we can always place the flower in the middle.

If two of three is used, impossible!

That being said, using available whenever possible yields optimal solution.

Complexity: O(n), O(1)

"""

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        result = self._canPlaceFlowersGreedy(flowerbed, n)

        print(flowerbed, n)

        return result

    def _canPlaceFlowersGreedy(self, flowerbed, n):
        for i, slot in enumerate(flowerbed):
            if slot: continue
            if i and flowerbed[i - 1]: continue
            if i < len(flowerbed) - 1 and flowerbed[i + 1]: continue
            flowerbed[i] = 1
            n -= 1
            if not n: return True
        return n <= 0

def test():
    solution = Solution()

    assert solution.canPlaceFlowers([], 0)
    assert not solution.canPlaceFlowers([], 1)
    assert not solution.canPlaceFlowers([1], 1)
    assert not solution.canPlaceFlowers([1, 0], 1)
    assert solution.canPlaceFlowers([1, 0, 0], 1)
    assert solution.canPlaceFlowers([1, 0, 0, 0, 1], 1)
    assert not solution.canPlaceFlowers([1, 0, 0, 0, 1], 2)

    print('self test passed')

if __name__ == '__main__':
    test()
