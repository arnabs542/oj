#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
414. Third Maximum Number

Total Accepted: 4982
Total Submissions: 18840
Difficulty: Easy
Contributors: ZengRed , 1337c0d3r

Given a non-empty array of integers, return the third maximum number in this array.
If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''

class Solution(object):

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        heap_min = [float('-inf')] * 3
        for n in nums:
            if n > heap_min[0] and n not in heap_min:
                heap_min[0] = n
                # heapify
                if heap_min[1] < heap_min[0]:
                    heap_min[1], heap_min[0] = heap_min[0], heap_min[1]
                if heap_min[2] < heap_min[0]:
                    heap_min[2], heap_min[0] = heap_min[0], heap_min[2]

        return heap_min[0] if heap_min[0] != float('-inf') else max(heap_min)

def test():
    solution = Solution()

    assert solution.thirdMax([3, 2, 1]) == 1
    assert solution.thirdMax([1, 2]) == 2
    assert solution.thirdMax([2, 2, 3, 1]) == 1
    print('self test passed')

if __name__ == '__main__':
    test()
