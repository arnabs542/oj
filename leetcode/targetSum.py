#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
494. Target Sum

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you
have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:
    1. The length of the given array is positive and will not exceed 20.
    2. The sum of elements in the given array will not exceed 1000.
    3. Your output answer is guaranteed to be fitted in a 32-bit integer.

==============================================================================================
SOLUTION

Apparently, this is a graph search problem.

1. Brute force
Enumerate all possible combination of sign symbols and verify.

And the traversal process can be implemented with dfs(depth first search).

Define state:
    (n, s) = (size of list containing available numbers, target sum)
Define function f(n, s) as the number of ways to sum up to s with n numbers in the list.
For each number, we have two branches to search: minus or plus this number.
Then, the recurrence relation is:
    f(n, s) = f(n - 1, s + nums[n - 1]) + f(n - 1, s - nums[n - 1]) if n > 0 else s == 0


Number of all possible combinations: O(2ⁿ).

Size of recursion tree will be 2ⁿ, n refers to the size of nums array.
The depth of the recursion tree can go up to n.

Complexity: O(2ⁿ), O(n).

2. Prune search branches - recursion with MEMOIZATION

It can be easily observed that in the last approach, a lot of redundant function calls could
be made with the same value of ii as the current index and the same value of sumsum as the
current sum, since the same values could be obtained through multiple paths in the recursion
tree. In order to remove this redundancy, we make use of memoization as well to store the
results which have been calculated earlier.

Cache(or memoize)!

Complexity: O(l*n), O(l*n), where l refers to the range of sum, and n refers to the size
of array.

3. Dynamic Programming
Obviously, the state we are tracking is a tuple (n, s), where n is the size of array, and s
is the target sum.

Since the sum of elements is bounded, it's possible to traverse possible combination of (n, s).
This indicates it can be solved with dynamic programming.
for i in range(n):
    for s in range(-1000, 10001):
        # state transition, XXX: check out of bound!
        dp[i][s + 1000] += dp[i - 1][s + 1000 + nums[i]]
        dp[i][s + 1000] += dp[i - 1][s + 1000 - nums[i]]

        # or another implementation:
        dp[i][s + 1000 + nums[i]] += dp[i - 1][s + 1000]
        dp[i][s + 1000 - nums[i]] += dp[i - 1][s + 1000]

'''

from _decorators import memoize

class Solution(object):

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        result = self._findTargetSumWaysDfs(nums, S)
        # result = self._findTargetSumWaysDfsIterative(nums, S)
        print(result)
        return result

    def _findTargetSumWaysDfs(self, nums, S):
        '''
        Brute force depth first search method.
        '''
        @memoize
        def dfs(n, s):
            if n == 0:
                return 1 if s == 0 else 0
            return dfs(n - 1, s - nums[n - 1]) + dfs(n - 1, s + nums[n - 1])
        return dfs(len(nums), S)

    def _findTargetSumWaysDfsIterative(self, nums, S):
        '''
        Convert above recursive dfs solution to iterative one implemented with STACK.

        First, we need to analyze the state of above recursive function call:

        INPUT is (n, s), indicating the available nums array size and remaining target sum.
        OUTPUT is the return value, indicating number of ways to sum up to a target.

        And there are branch control statements:
            dfs(n - 1, s - nums[n - 1]) + dfs(n - 1, s + nums[n - 1])
        which indicates an implicit LOCAL VARIABLE: branch index. This branch index
        controls the recursive procedure call order.

        Then, we have our four-tuple state, composed of INPUT, OUTPUT, LOCAL VARIABLES,
        corresponding to the recursive call:
            (array size, target sum, branch index, return value)

        OUTPUT is the return values from search sub-branches which need calculation.
        '''
        # DONE: do it iteratively. A problem is that we need to compute values
        # from return values of recursive function calls. How to emulate that?
        # method 1: hash table?
        # method 2: inplace pop and push?

        stack = [(len(nums), S, 0, 0)] # size, target sum, branch index, #ways
        # DONE: avoid duplicate visit
        visited = {} # key = (n, s), value = #ways
        nWays = 0 # return value of corresponding recursive function call
        while stack:
            n, s, i, ret = stack[-1]
            if n == 0 or i >= 2 or (n, s) in visited:
                # base case or end of exploration or visited
                if (n, s) in visited: nWays = visited[(n, s)]
                elif n == 0: nWays = 1 if s == 0 else 0
                elif i == 2:
                    nWays = ret
                    visited[(n, s)] = nWays
                stack.pop()
                if stack:
                    n, s, i, ret = stack.pop()
                    i += 1
                    nWays = ret + nWays # accumulate values
                    stack.append((n, s, i, nWays))
            else:
                # push: search branches
                new_sum = s - nums[n - 1] if i == 0 else s + nums[n - 1]
                stack.append((n - 1, new_sum, 0, 0))
        return nWays

    def _findTargetSumWaysDP(self, nums, S):
        # TODO: dynamic programming solution
        pass

def test():
    import time
    begin = time.time()

    solution = Solution()

    assert solution.findTargetSumWays([], 0) == 1
    assert solution.findTargetSumWays([], 1) == 0
    assert solution.findTargetSumWays([1], -1) == 1
    assert solution.findTargetSumWays([1, 1, 1, 1, 1, ], 3) == 5
    assert solution.findTargetSumWays([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 4) == 120

    end = time.time()

    print("self test passed in {}ms".format(1000 * (end - begin)))

if __name__ == '__main__':
    test()
