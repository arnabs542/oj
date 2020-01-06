#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
506. Relative Ranks Add to List

Total Accepted: 6212
Total Submissions: 12836
Difficulty: Easy
Contributors: taylorty

Given scores of N athletes, find their relative ranks and the people with the top three
highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got
"Gold Medal", "Silver Medal" and "Bronze Medal". For the left two athletes, you just need to
output their relative ranks according to their scores.

Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.

==============================================================================================
SOLUTION

1. Sort the original indices
[5, 4, 3, 2, 1] => Indices [0, 1, 2, 3, 4] in sorted form

'''

class Solution(object):

    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranks = self.findRelativeRanksSort(nums)
        print(ranks)
        return ranks

    def findRelativeRanksSort(self, nums):
        indices = list(sorted(range(len(nums)), key=lambda x: nums[x], reverse=True))
        ranks = [None] * len(nums)
        for i in range(len(indices)):
            ranks[indices[i]] = "Gold Medal" if i == 0 else (
                "Silver Medal" if i == 1 else (
                    "Bronze Medal" if i == 2 else str(i + 1)
                )
            )
        return ranks

def test():
    solution = Solution()

    assert solution.findRelativeRanks([5, 4, 3, 2, 1]) == [
        "Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    assert solution.findRelativeRanks([1, 2, 3, 4, 5]) == [
        "5", "4", "Bronze Medal", "Silver Medal", "Gold Medal"]

    print("self test passed")

if __name__ == '__main__':
    test()
