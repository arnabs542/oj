#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
322. Coin Change

Total Accepted: 39802
Total Submissions: 153959
Difficulty: Medium
Contributors: Admin

You are given coins of different denominations and a total amount of money amount. Write a
function to compute the fewest number of coins that you need to make up that amount. If that
amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
'''

class Solution(object):

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # return self.coinChangeDP(coins, amount)
        # return self.coinChangeBFS(coins, amount)
        return self.coinChangeBFSOpt(coins, amount)

    def coinChangeDP(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        m = len(coins)
        f = [1 << 31] * (amount + 1)
        f[0] = 0
        for i in range(1, amount + 1):
            for j in range(m - 1, -1, -1):
                if i - coins[j] >= 0 and (f[i - coins[j]] + 1 < f[i]):
                    f[i] = f[i - coins[j]] + 1

        print(f[-1])
        return f[-1] if f[-1] != 1 << 31 else -1

    def coinChangeBFS(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int

        Breadth-first search
        """
        frontier = list()
        distance = {}

        frontier.append(amount)
        distance[amount] = 0

        while frontier:
            state = frontier.pop(0)
            if not state:
                return distance[state]

            for coin in coins:
                state_new = state - coin
                if state_new >= 0 and state_new not in distance:
                    frontier.append(state_new)
                    distance[state_new] = distance[state] + 1

        return -1

    def coinChangeBFSOpt(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int

        Breadth-first search.
        Treat this problem as a SHORTEST PATH problem from state `amount` to state `0`

        785ms
        """
        coins.sort(reverse=True)
        frontier = {amount}
        visited = {amount}
        frontier_new = set()
        step = 0

        while frontier:
            # print(frontier)
            for state in frontier:
                if not state:
                    return step

                for coin in coins:
                    state_new = state - coin
                    if state_new >= 0 and state_new not in visited :
                        frontier_new.add(state_new)
                        visited.add(state_new)

            frontier.clear()
            frontier, frontier_new = frontier_new, frontier
            step += 1

        return -1

    def coinChangeBiBFS(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int

        Two end(bidirectional) breadth-first search.
        Treat this problem as a SHORTEST PATH problem from state `amount` to state `0`
        """

def test():
    solution = Solution()
    assert solution.coinChange([1, 2, 5], 11) == 3
    assert solution.coinChange([2], 3) == -1
    assert solution.coinChange([], 11) == -1
    assert solution.coinChange([1, 2, 3, 5], 4) == 2
    assert solution.coinChange(
        [333, 364, 408, 118, 63, 270, 69, 111, 218, 371, 305], 5615) == 15
    assert solution.coinChange([125,146,125,252,226,25,24,308,50], 8402)
    assert solution.coinChange([2147483647], 2)
    print('self test passed')

if __name__ == '__main__':
    test()
