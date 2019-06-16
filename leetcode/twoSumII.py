#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
167. Two Sum II - Input array is sorted

Total Accepted: 38994
Total Submissions: 81136
Difficulty: Medium
Contributors: Admin

Given an array of integers that is already sorted in ascending order, find two numbers
such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the
target, where index1 must be less than index2. Please note that your returned answers (both
index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2


================================================================================
SOLUTION

1. Hash
inverted index: (key=element, value=element's position/index)

Complexity: O(N), O(N)

2. Binary search

Complexity: O(NlogN), O(1)

3. Two pointers - Graph search, ordered tree, pruning
Think this as a graph search process, but with some pruning process with some greedy strategy.

The target indices i, j must satisfy 0 <= i, j <= n - 1, where n is the length of the array.
Initialize i = 0, j = n - 1, then search inward(from both ends to middle).

Define state = (i, j), treat this as a graph search problem, then we have state transition
illustrated as below.

If sum of two pointers' value is less than the target value, then increment i by 1.
If sum of two pointers' value is greater than the target value, then decrease j by 1.
Repeat until we have the sum of two pointers value equal to target value.

PROOF
-----

This is similar to "container with most water".

. 1 2 3 4 5 6
1 x ------- o
2 x x - o o o
3 x x x o | |
4 x x x x | |
5 x x x x x |
6 x x x x x x

The solution correctness can be proved with SET THEORY.
- The combination coordinates compose of vertices set of a GRAPH.
- The graph is a CONNECTED COMPONENT itself: each pair of vertices are connected by paths.
- At each vertex (i, j) there are four directions/edges to go:
    (i-1, j), (i+1, j), (i, j-1), (i, j+1).
- At each vertex (i, j), left branch {(x, j)| x < i} yields smaller result,
    and below/right branch {(x, j)| x > j} yields larger result.
    This has a similar structure to binary search tree, because the array is ORDERED.
- Start traversing with (0, n - 1), as the root of the TREE, then this tree
    is like a BINARY SEARCH TREE.
    1) Every node can be reached from the ROOT by traversing leftward and downward.
    2) To not traverse backward, only left and below directions are followed.
    3) At each time without a match of target sum, the of left/below branch of set
    of vertices are PRUNED.
    4) Then finally we traverse to the target point, because graph SET is composed
    of the solution set and non-solution set, and non-solution set is PRUNED.

Complexity: O(N), O(1)


'''
class Solution(object):

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                return [left + 1, right + 1]
            pass

def test():
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [1, 2]

    print('self test passed')

if __name__ == '__main__':
    test()
