#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
96. Unique Binary Search Trees

Total Accepted: 103259
Total Submissions: 261515
Difficulty: Medium
Contributors: Admin

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

==============================================================================================
SOLUTION:
    Of course, this is a Catalan Number problem.
    Divide and conquer to form state transition relation.

Given n, there are n - 1 nodes to construct except the root one. The we can divide the rest of
nodes by (0, n -1), (1, n - 1), ..., (n - 1, 0), in total n ways. In each way, the number of
unique BST is the number of left subtrees times the right tree's.

Dynamic Programming:
    f[i] = sum([f[j] * f[i - 1 - j] for j in range(i)])
'''

class Solution(object):

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0] * (n + 2)
        f[0] = f[1] = 1
        for i in range(2, n + 1):
            f[i] = sum([f[j] * f[i - 1 - j] for j in range(i)])

        print(f)
        return f[n]

def test():
    solution = Solution()

    assert solution.numTrees(0) == 1
    assert solution.numTrees(1) == 1
    assert solution.numTrees(2) == 2
    assert solution.numTrees(3) == 5
    assert solution.numTrees(10) == 16796

    print('self test passed')

if __name__ == '__main__':
    test()
