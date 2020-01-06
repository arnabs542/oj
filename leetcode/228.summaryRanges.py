#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
228. Summary Ranges

Total Accepted: 61382
Total Submissions: 226333
Difficulty: Medium
Contributors: Admin

Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
'''

class Solution(object):

    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        if not nums:
            return ranges
        i = 0
        left = right = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == right + 1:
                right += 1
            else:
                # insert into ranges list and reset left, right
                ranges.append('{}->{}'.format(left, right)
                              if left < right else str(left))
                left = right = nums[i]

        ranges.append('{}->{}'.format(left, right)
                      if left < right else str(left))
        print(ranges)
        return ranges

def test():
    solution = Solution()
    assert solution.summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]

    print('self test passed')

if __name__ == '__main__':
    test()
