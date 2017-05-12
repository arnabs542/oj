#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
375. Guess Number Higher or Lower II

Total Accepted: 13790
Total Submissions: 39679
Difficulty: Medium
Contributors: Admin

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win
the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.

Hint:

1. The best strategy to play the game is to MINIMIZE THE MAXIMUM LOSS you could possibly face.
Another strategy is to MINIMIZE THE EXPECTED LOSS. Here, we are interested in the first scenario.
2. Take a small example (n = 3). What do you end up paying in the worst case?
3. Check out this article(https://en.wikipedia.org/wiki/Minimax) if you're still stuck.
4. The purely recursive implementation of MINIMAX would be worthless for even a small n.
You MUST use dynamic programming.
5. As a follow-up, how would you modify your code to solve the problem of minimizing the
expected loss, instead of the worst-case loss?

==============================================================================================
SOLUTION

1. Naive brute force method - minimize the worst case loss - recursive minimax
This is a discrete combinatorial problem, thus it can be solved by enumerating all possible
arrangements and inspect those case one by one.

Given an interval, we iterate through all possible first division/guess, to divide the problem
into two subproblems. There is a worst case that the target number lies between some
sub-interval, which has the highest cost to solve among all the search spaces of sub-problems.
Then we seek to minimize the worst case loss.

Time complexity: O(exponential or factorial).

2. Iterative MINIMAX
The problem is to search in an intervals. And apparently, the states are overlapping.
So there would be large amount of duplicate computations.

3. Minimize the expected loss
Mathematical expectation is is obtained by computing the integral of the product of a
variable and its probability density function: E(x) = ∫x p(x) dx.

'''

class Solution(object):

    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        amount = self.getMoneyAmountMinimax(n)
        print(n, ':', amount)
        return amount

    def getMoneyAmountMinimax(self, n):
        '''
        Minimax search algorithm as best strategy.

        The search state is the candidate interval that the target number might lie in.
        Obviously, the states are overlapping.
        '''
        # loss function: min amount in interval [i, j], adding 0 and n+1 as padding
        f = [[0 if j-i <= 0 else float('inf') for j in range(n+2)] for i in range(n+2)]
        for l in range(1, n):
            for i in range(1, n-l+1):
                # interval [i, i+l]
                for g in range(i, i+l+1):
                    # optimal decision with minimax algorithm
                    f[i][i+l] = min(f[i][i+l], g + max(f[i][g-1], f[g+1][i+l]))
        return f[1][n]

    def getMoneyAmountMinimizeExpectedLoss(self, n):
        # TODO: minimize the expected loss, instead of the worst case loss
        # loss function: min amount in interval [i, j], adding 0 and n+1 as padding
        f = [[0 if j-i <= 0 else float('inf') for j in range(n+2)] for i in range(n+2)]
        for l in range(1, n):
            for i in range(1, n-l+1):
                # interval [i, i+l]
                for g in range(i, i+l+1):
                    # optimal decision with minimax algorithm
                    f[i][i+l] = min(f[i][i+l], g + sum(
                        max(0, g-i) * f[i][g-1], max(0, i+l-g) *f[g+1][i+l]) / l)
        return f[1][n]

def test():
    solution = Solution()

    assert solution.getMoneyAmount(1) == 0
    assert solution.getMoneyAmount(2) == 1
    assert solution.getMoneyAmount(3) == 2
    assert solution.getMoneyAmount(4) == 4
    assert solution.getMoneyAmount(5) == 6
    assert solution.getMoneyAmount(100) == 400
    assert solution.getMoneyAmount(233) == 1160
    # assert solution.getMoneyAmount(1000) == 2

    print("\nself test passed")

if __name__ == '__main__':
    test()
