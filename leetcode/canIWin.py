#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
464. Can I Win
Medium

In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

    Input:
    maxChoosableInteger = 10
    desiredTotal = 11

    Output:
    false

Explanation:
    No matter which integer the first player choose, the first player will lose.
    The first player can choose an integer from 1 up to 10.
    If the first player choose 1, the second player can only choose integers from 2 up to 10.
    The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
    Same with other integers chosen by the first player, the second player will always win.

================================================================================
SOLUTION

Derive from simple cases.
-------------------------
Denote the range by [1, m], target number by n.
Base case:
  m*(m+1)/2 < n: no one can win
1) m >= n: Target number is within the given range, then the first player wins.
2) 1 + m >= n: Target number can always be obtained by choosing a number after player one.
This case resembles "Two Sum" problem, in a sorted input scenario.
3)

Of course this can be solved with MINIMAX in a DEPTH FIRST SEARCH approach.
The problem is the complexity may be too high, if no appropriate memoization method
is utilized.
The STATE of pool of available numbers is of PERMUTATION SEARCH SPACE.

Now the search space is reduced to COMBINATION SPACE.
Can we reduce it to RANGE SPACE, which can be represented with two numbers?

First, to reduce the repeated calculation caused by PERMUTATION, we can restrict
the numbers are chosen in a DESCENDING ORDER.


"""

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # result = self.canIWinMinimax(maxChoosableInteger, desiredTotal)
        result = self.canIWinMinimaxBinaryRepresentation(maxChoosableInteger, desiredTotal)
        # result = self.canIWin3(maxChoosableInteger, desiredTotal)

        return result

    def canIWinMinimax(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        cache = {}
        def dfs(nums, target):
            # print(nums, target)
            # if target <= 0: return -1
            # if not nums and target > 0: return 0
            if nums[-1] >= target: return 1
            key = tuple(nums)
            if key in cache: return cache[key]
            result = -1 # XXX: initialization!
            # for i in range(len(nums) - 1, -1, -1):
            for i in range(len(nums)):
                result = max(result, -dfs(nums[:i] + nums[i+1:], target - nums[i]))
                if result > 0:
                    cache[key] = 1
                    return 1
                    # break
                pass

            cache[key] = -1
            return -1

        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            # print("early stop")
            return False
        choices = list(range(1, maxChoosableInteger + 1))
        result = dfs(choices, desiredTotal) > 0

        return result

    def canIWinMinimaxBinaryRepresentation(self, maxChoosableInteger, desiredTotal):
        # FIXME: 20, 168
        memoization = {}
        def dfs(state, target):
            # print("{} target: {}".format(bin(state), target))
            if target <= 0: return -1 # lost
            if state == 0 and target > 0: return 0 # draw game
            if (state, target) in memoization:
                return memoization[(state, target)]
            result = -1 # XXX: initialization!!!
            # for i in range(maxChoosableInteger-1, -1, -1):
            for i in range(0, maxChoosableInteger):
                if state & (1<<i):
                    if i + 1 >= target:
                        result = 1
                        break
                    state ^= (1<<i)
                    # print(bin(1<<i))
                    result = max(result, -dfs(state, target - (i+1)))
                    if result > 0: break
                    state ^= (1<<i)
            memoization[(state, target)] = result
            return result

        state = 0
        for i in range(maxChoosableInteger):
            state |= (1 << i)
        print("initial state: ", state, maxChoosableInteger, desiredTotal)
        result = dfs(state, desiredTotal) > 0
        print ("result:", maxChoosableInteger, desiredTotal, result)

        return result

    def canIWin3(self, maxChoosableInteger, desiredTotal):
        max_sum = maxChoosableInteger*(maxChoosableInteger+1)//2

        if max_sum < desiredTotal:
            return False
        elif max_sum == desiredTotal:
            return (maxChoosableInteger%2 == 1)

        if maxChoosableInteger >= desiredTotal:
            return True

        bit_mask = 1 << maxChoosableInteger # bit 0: unused, bit 1: used
        self.record = {}

        return self.checkWin(maxChoosableInteger, bit_mask, desiredTotal)

    def checkWin(self, max_num, bit_mask, remain_sum):

        if bit_mask in self.record:
            return self.record[bit_mask]

        for i in range(max_num):

            if (1&(bit_mask >> i)) != 0:
                # skip already-picked number
                continue

            n = i+1 # n: picked number
            if (n >= remain_sum) or (self.checkWin(max_num, bit_mask | (1<< i), remain_sum-n) is False):
                self.record[bit_mask] = True
                return True

        self.record[bit_mask] = False
        return False

def test():
    solution = Solution()

    # TODO: submit

    assert solution.canIWin(1, 1) == True
    assert solution.canIWin(5, 3) == True
    assert solution.canIWin(2, 3) == False
    assert solution.canIWin(7, 8) == False
    assert solution.canIWin(10, 11) == False
    assert solution.canIWin(15, 100) == True
    assert solution.canIWin(20, 168) == False
    # assert solution.canIWin2(20, 168) == False

    print("self test passed!")

if __name__ == '__main__':
    test()
