#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
453. Minimum Moves to Equal Array Elements

Total Accepted: 10067
Total Submissions: 21931
Difficulty: Easy
Contributors: amehrotra2610

Given a non-empty integer array of size n, find the minimum number of moves required
to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

==============================================================================================
SOLUTION

1. Brute-force greedy strategy, always increment the elements smaller than the maximum,
until equivalency achieved.

2. Backward reduction: increment all elements but one is equal to decrease that one.

3. Another perspective, perhaps dynamic programming?

Assume the array is sorted already. Then we can solve the problem is a recursive way:

    Solve the problem with elements with indices in [1, n - 1], then increment all
those n - 1 elements to be equal to the last element.
Then we can define such state:
state[i] = (steps, target)
         = (steps to take to move first n - 1 elements equal, the target number after moving)

Then,
    steps[i] = (nums[i] + steps[])

'''

class Solution(object):

    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self.minMovesBruteForce(nums)
        return self.minMovesMath(nums)

    def minMovesBruteForce(self, nums):
        """
        Time limit exceeded
        """
        if not nums:
            return 0
        max_old = max_new = nums.index(max(nums))
        step = 0
        while min(nums) != max(nums):
            for i, n in enumerate(nums):
                if i != max_old:
                    nums[i] += 1
                    max_new = i if nums[i] > nums[max_new] else max_new
            step += 1
            max_old = max_new
        print(nums, step)
        return step

    def minMovesMath(self, nums):
        if not nums:
            return 0
        return sum(nums) - min(nums) * len(nums)

    # TODO: another perspective

def test():
    solution = Solution()

    assert solution.minMoves([]) == 0
    assert solution.minMoves([1, 2, 3]) == 3

    assert solution.minMoves([1, 2147483647]) == 2147483646

    print("self test passed")

if __name__ == "__main__":
    test()
