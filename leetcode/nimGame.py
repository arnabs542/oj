#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
292. Nim Game

You are playing the following Nim Game with your friend: There is a heap of stones on the
table, each time one of you take turns to remove 1 to 3 stones. The one who removes the
last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to
determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter
1, 2, or 3 stones you remove, the last stone will always be removed by your friend.


==============================================================================================
SOLUTION

1. Minimax with dynamic programming

2. Dynamic programming space optimized
Since the recurrent relation only depends on the former 3 states, we only need to store
3 history states.

2. Induce patterns from cases

The pattern repeats itself with period of 4 by observation.

'''

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # return self._canWinNimMinimaxDP(n)
        return self._canWinNimMinimaxDPOpt(n)
        # return self._canWinNimMath(n)

    def _canWinNimMinimaxDP(self, n):
        f = [-1 for _ in range(n + 1)]

        for i in range(1, n + 1):
            f[i] = max(-f[i - 1], -f[i - 2] if i >= 2 else 1, -f[i - 3] if i >= 3 else 1)

        print(f)
        return f[n] >= 0

    def _canWinNimMinimaxDPOpt(self, n):
        f = (-1, 1, 1)
        if n < 3:
            return f[n] >= 0

        for i in range(3, n + 1):
            score = max(-f[2], -f[1], -f[0])
            f = (f[1], f[2], score)

        print(f)
        return score >= -2

    def _canWinNimMath(self, n):
        return n % 4 > 0

def test():
    solution = Solution()

    assert solution.canWinNim(0) is False
    assert solution.canWinNim(1)
    assert solution.canWinNim(2)
    assert solution.canWinNim(3)
    assert solution.canWinNim(4) is False
    assert solution.canWinNim(5)
    assert solution.canWinNim(6)
    assert solution.canWinNim(7)
    assert solution.canWinNim(8) is False
    assert solution.canWinNim(1348820612) is False

    print("self test passed")

if __name__ == '__main__':
    test()
