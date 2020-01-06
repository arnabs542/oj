#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
275. H-Index II

Total Accepted: 38346
Total Submissions: 114496
Difficulty: Medium
Contributors: Admin

Follow up for H-Index: What if the citations array is sorted in ascending order? Could you
optimize your algorithm?

Hint:

Expected runtime complexity is in O(log n) and the input is sorted.


==============================================================================================
SOLUTION:

Linear search optimized to binary search!
'''

class Solution(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        low, high = 0, len(citations) - 1
        while low <= high:
            mid = (low + high) >> 1
            if citations[mid] >= len(citations) - mid:
                high = mid - 1
            else:
                low = mid + 1
            pass

        return len(citations) - low

def test():
    solution = Solution()

    assert solution.hIndex([]) == 0
    assert solution.hIndex([0, 1]) == 1
    assert solution.hIndex(sorted([3, 0, 6, 1, 5])) == 3

    print('self test passed')

if __name__ == '__main__':
    test()
