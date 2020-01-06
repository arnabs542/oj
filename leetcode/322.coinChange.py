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

================================================================================
SOLUTION

1. Brute force - permutation

The problem could be modeled as the following mathematical optimization problem :
```latex
\min_{x}m \\
\text{subject to} \sum_{i=0}^{m-1}c_i = S
```

A trivial solution is to perform graph search, to explore all permutations.

Define state as a tuple of (S, m).
Then the search initial state is (S, 0), and terminal state is (0, m).

Complexity: O()

2. Brute force - combination

Permutations are too complex, we can restrict the order to reduce it to combination.

--------------------------------------------------------------------------------
Or, for your information, we can reduce the sequence length by modeling another way.
The problem could be modeled as another mathematical optimization problem:

```latex
\min_{x}\sum_{i=0}^{n-1}x_i \\
\text{subject to} \sum_{i=0}^{n-1}x_i\cdot c_i = S
```

Where S is the amount, c_i is the coin dominations, x_i is the number of coins with
dominations c_i used in change of amount S, and n is the number of coins.
Obviously, x_i is in [0, S/c_i].

A trivial solution is to enumerate all subsets of coin frequencies [x0… xn−1] that
satisfy the constraints above, compute their sums and return the minimum among them.

Define state as a tuple of (S, X).
Then the search initial state is (S, \vec{0}), and terminal state is (0, Xₜ).

--------------------------------------------------------------------------------
Complexity:  O(\prod_{i=0}^{n-1}\frac{S}{c_i}) = O(Sⁿ) in worst case.
Space complexity: O(n).

3. Dynamic programming

Above brute force methods have STATE SPACE of overlapping subproblems,
involving duplicate computation.

Define state f(s) as the minimum number of coins need to change amount s.

Complexity: O(Sn).

4. Breadth first search
Minimal number of coins can be thought as GRAPH SHORTEST PATH problem.
For shortest path, breadth first search is better than depth first search.

In this graph, vertices are the amount, and edges are available coins.

Define state (amount, )
In a naive BFS, edges is a static set, at each state we can choose any of the coins.
This will involve many duplicate equivalent situations. For example, choosing coins
"1, 2, 3" is actually equivalent to "2, 1, 3". These PERMUTATIONS are equivalent.


Define state (amount, available coin index)
To avoid duplicate computations because of permutations, restrict the ORDER
of selecting coins to be monotonic, since the sum of values is order invariant!
Then it's reduced to COMBINATION.

5. Bidirectional breadth first search
TODO:

'''

from _decorators import timeit

class Solution(object):

    @timeit
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # result = self._coinChangeDP(coins, amount)
        # result = self._coinChangeBFS(coins, amount)
        # result = self._coinChangeBFSOpt(coins, amount)
        # result = self._coinChangeBFSCombinationTwoFrontiers(coins, amount)
        result = self._coinChangeBFSCombination(coins, amount)

        print(coins, amount, result)

        return result

    def _coinChangeDP(self, coins, amount):
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

    def _coinChangeBFS(self, coins, amount):
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

    def _coinChangeBFSOpt(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int

        Breadth-first search.
        Treat this problem as a SHORTEST PATH problem from state `amount` to state `0`

        A different implementation of bfs, without using auxiliary space `distance`.
        Instead, at each step, exhaust all vertices in the search frontier, and
        keep track of the step used.

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

    def _coinChangeBFSCombination(self, coins: list, amount: int):
        coins.sort(reverse=True)
        frontier = [(amount, 0)]
        distance = {amount: 0}

        while frontier:
            state, i = frontier.pop(0) # queue pop front
            if not state: return distance[state]
            for j in range(i, len(coins)):
                amountNew = state - coins[j]
                if amountNew in distance or amountNew < 0: continue
                frontier.append((amountNew, j))
                distance[amountNew] = distance[state] + 1
        return -1

    def _coinChangeBFSCombinationTwoFrontiers(self, coins: list, amount: int):
        """
        Using two set frontiers, keep track of step used, and eliminate duplicate search
        """
        # FIXME: this is surprisingly much slower
        coins.sort(reverse=True)
        frontier = {amount: 0}
        frontierNew = {}
        step = 0

        while frontier:
            for state, i in frontier.items(): # exhaust frontier set
                # print(state, i)
                if not state: return step
                for j in range(i, len(coins)):
                    amountNew = state - coins[j]
                    if amountNew < 0: continue
                    # frontierNew.setdefault(amountNew, j)
                    frontierNew[amountNew] = j
            frontier, frontierNew = frontierNew, {}
            step += 1
        return -1

    def _coinChangeBiBFS(self, coins, amount):
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
    assert solution.coinChange([125, 146, 125, 252, 226, 25, 24, 308, 50], 8402)
    assert solution.coinChange([2147483647], 2)
    print('self test passed')

if __name__ == '__main__':
    test()
