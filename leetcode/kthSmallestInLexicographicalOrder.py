#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
440. K-th Smallest in Lexicographical Order

Total Accepted: 1304
Total Submissions: 6584
Difficulty: Hard
Contributors: Stomach_ache

Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 ≤ k ≤ n ≤ 10⁹.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest
number is 10.

================================================================================

1. Brute force
Sort according to lexicographical order, and take the nth smallest one.

Complexity: O(nlogn), O(n)


2. Graph traversal - dfs
Lexicographical order is determined in a greedy strategy fashion.

At each step, searching for next smallest number, and there are two search branches:
1) append a zero after the current number: multiply by 10
2) increment the current number by 1: add by 1

1 - 10 - 100 - 1000
|    |
|   11 - 110
|   ...
|   19 - 190
|
2 - 20 - 200 - 2000
|
3 - 30 - 300 - 3000

Treat it as a graph problem, and perform depth first traversal on the graph.
The process is like tree preorder traversal.

Complexity: O(k), O(k)

This method is linear to k, when k is large, it's slow.

3. Divide and conquer - binary search - like binary search tree!

The graph constructed above has a binary tree structure.
And for each integer node, the integers on the left tree are lexicographically
larger than the right tree.

The idea is to calculate count of integers beginning with specific prefix,
and divide and conquer.

Then, at each node, compute the number of integers starting with current integer
as prefix. This is actually the number of integers on the right tree plus 1.

Assume the count is c, if c > k, then target number is on the right subtree(x10).
If c < k, then target number is on the left subtree(+1).


Complexity: O((logn)²)


'''

from _decorators import timeit

class Solution(object):

    @timeit
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # result = self._findKthNumberNaiveDfs(n, k)
        result = self._findKthNumberBinarySearch(n, k)

        print(n, k, " => ", result)

        return result

    def _findKthNumberNaiveDfs(self, n, k):
        def dfs(start, order):
            """
            Inputs
            ------
            start: current integer
            order: the kth order

            Returns
            -------
            A tuple: order, found number
            """
            # print(start, order)
            if order <= 1: return 0, start
            if start > n: return order, start
            order -= 1 # 1
            if start * 10 <= n:
                order, found = dfs(start * 10, order) # 10, 2
                if order <= 0: return order, found
            if start + 1 <= n and start % 10 != 9:
                order, found = dfs(start + 1, order)
                if order <= 0: return order, found

            return order, 0

        ret, result = dfs(1, k)
        return result

    def _findKthNumberBinarySearch(self, n, k):
        # TODO: iterative implementation
        def countSubtree(x):
            if x > n: return 0
            y = 0
            total = 0
            while x <= n:
                c = min(10**y, n - x + 1)
                total += c

                x *= 10
                y += 1

            return total

        def dfs(start, order):
            if order <= 1: return start
            right = countSubtree(start)
            if order > right:
                order -= right
                return dfs(start + 1, order) # go to left tree
            else:
                return dfs(start * 10, order - 1) # go to right tree
            pass

        return dfs(1, k)

def test():
    solution = Solution()

    # assert solution.findKthNumber(13, 0) == 0
    assert solution.findKthNumber(13, 1) == 1
    assert solution.findKthNumber(13, 2) == 10
    assert solution.findKthNumber(13, 3) == 11
    assert solution.findKthNumber(13, 4) == 12
    assert solution.findKthNumber(13, 5) == 13
    assert solution.findKthNumber(13, 6) == 2
    assert solution.findKthNumber(130000, 130000) == 99999
    assert solution.findKthNumber(1_000_000_000, 100_000_000) == 189999998
    assert solution.findKthNumber(1_000_000_000, 1_000_000_000) == 999_999_999

    print("self test passed!")

if __name__ == '__main__':
    test()
