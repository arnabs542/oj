#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
561. Array Partition I

Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].

==============================================================================================
SOLUTION

1. Brute force
Enumerate all possible combinations.

Time complexity recurrence relation:
T(n + 1)  = T(n) + 2n(2n-1)T(n) = (4n² - 2n + 1) T(n)

Complexity: O(?)

2. Greedy strategy
To make the first choice, choose the second largest as a minimum of a pair. To make the
second largest as a minimum of its pair, we have to pair it with the largest,
giving pair (largest number, second largest number).

Repeat this process, the optimal solution is sequence of pairs (a1, b1), (a2, b2), ..., (an, bn),
where a1 <= b1 <= a2 <= b2 <= ... <= an <= bn.

Then the solution would be:
    Sort the array, and add numbers a[0], a[2], ..., a[n - 2]

TODO: how to prove this greedy strategy?

----------------------------------------------------------------------------------------------
Proof by contradiction

Prove that if it weren't the case, there would be a more optimal solution.

In the above greedy solution, all pairs can be thought of as an interval, and these intervals
are not overlapping(although they touch each other).

Suppose there are two pairs or intervals, overlapping. Let's assume its (a1, b1), and (a2, b2).

Then we have a1 <= b1, and a2 <= b2.
There are two cases, a1 <= a2 or the other way around. Assume a1 <= a2.
Since they are overlapping, then we have a2 < b1.

The objective is a1 + a2, and applying the inequality property, a1 + a2 < a1 + min(b1, b2).
And the latter result can be obtained with pairs (a1, a2), (min(b1, b2), max(b1, b2)).

It's proved that there will be a more optimal solution if some pairs are overlapping.
So, the optimal solution will have no pairs overlapping. Then it will take the sorted form:
a1 <= b1 <= a2 <= b2 <= ... <= an <= bn.


"""

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = self._arrayPairSumGreedy(nums)

        print(nums, result)

        return result

    def _arrayPairSumGreedy(self, nums):
        nums.sort()

        result = sum(nums[0:len(nums) - 1:2])

        return result

def test():
    solution = Solution()

    assert solution.arrayPairSum([1, 4, 3, 2]) == 4

    print("self test passed")

if __name__ == '__main__':
    test()
