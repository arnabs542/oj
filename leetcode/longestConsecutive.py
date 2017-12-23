#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
128. Longest Consecutive Sequence

Total Accepted: 82393
Total Submissions: 238614
Difficulty: Hard
Contributors: Admin

Given an unsorted array of integers, find the length of the longest consecutive
elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

==============================================================================================
SOLUTION

1. Sort

Complexity: O(NlogN), O(N)

2. Depth first search with hash table

Complexity: O(N), O(N)


'''

class Solution(object):

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        """
        return self.longestConsecutiveDFS(nums)

    def longestConsecutiveDFS(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        depth-first search strategy
        """
        table = set(nums)
        length_max = 1

        for n in nums:
            if n not in table:
                continue
            length = 1
            left, right = n - 1, n + 1
            while left in table:
                length += 1
                table.remove(left)
                left -= 1
            while right in table:
                length += 1
                table.remove(right)
                right += 1
            table.remove(n)
            length_max = max(length, length_max)

        return length_max

    def longestConsecutiveUnionFind(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Union find
        """
        # TODO: union find algorithm

def test():
    solution = Solution()
    assert solution.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert solution.longestConsecutive([100, 4, 200, 1, 3, 2, 5]) == 5

    print('self test passed')

if __name__ == '__main__':
    test()
