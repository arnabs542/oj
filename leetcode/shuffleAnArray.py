#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
384. Shuffle an Array

Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

==============================================================================================
SOLUTION

Shuffling an array is related to permutation, and this problem requires equal likelihood of all
possible permutation.

To arrange those elements, we can achieve it in a sequential process: determine every element's
position, obeying uniform distribution among available positions, one by one. In this way, every
element has equal probability of occupying a specific position.

But, to arrange the permutation in element's perspective requires us to maintain which element
is already located somewhere, which needs auxiliary space.

To do this in a perspective of positions will spare the pain.

For each position, randomly choose an available number to fill that slot. If we iterate from
left to right, current position i is the division point: all available numbers are on the
right. In this way, we don't need auxiliary space storing available candidates, because they
are separated by current search frontier.

Complexity: O(N), O(1)

'''


import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums0 = nums
        self.reset()

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = list(self.nums0)
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.nums)):
            idx = random.randint(i, len(self.nums) - 1)
            self.nums[i], self.nums[idx] = self.nums[idx], self.nums[i]

        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

def test():
    solution = Solution()

    print("self test passed")

if __name__ == '__main__':
    test()
