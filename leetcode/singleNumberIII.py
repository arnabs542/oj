#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
260. Single Number III

Total Accepted: 59316
Total Submissions: 119222
Difficulty: Medium
Contributors: Admin

Given an array of numbers nums, in which exactly two elements appear only once and all the
other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
1. The order of the result is not important. So in the above example, [5, 3] is also correct.
2. Your algorithm should run in linear runtime complexity. Could you implement it using only
constant space complexity?

==============================================================================================
SOLUTION

1. Naive occurrence count with hash table. Complexity: O(n), O(n).

2. Separate the two single numbers with their XOR result.
XOR result is composed of bits where two single numbers differ. Then we take any bit with 1
in the XOR result as the AND mask. Use this AND mask to separate the list into two groups,
one of which contains numbers with the mask indicated bit set, and the other one of which with
the bit unset(0). Since the two single numbers differ at this bit, they must be located into
two different groups. And two same numbers will give same result of AND with mask, so in each
group, all elements occur twice except the single one.

'''

class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.singleNumberBit(nums)

    def singleNumberBit(self, nums):
        mask = 0
        for n in nums: mask ^= n # get the XOR result of two single numbers
        mask &= -mask #  clears all but the lowest bit of x

        a = b = 0
        for n in nums:
            if n & mask == mask:
                a ^= n
            else:
                b ^= n
        # print(a, b)
        return [a, b]

def test():
    solution = Solution()

    assert set(solution.singleNumber([])) == {0, 0}
    assert set(solution.singleNumber([1])) == {0, 1}
    assert set(solution.singleNumber([2, 5])) == {2, 5}
    assert set(solution.singleNumber([2, -5])) == {2, -5}
    assert set(solution.singleNumber([1, 1, 2, 5])) == {2, 5}
    assert set(solution.singleNumber([1, 2, 1, 3, 2, 5])) == {3, 5}

    print("self test passed")

if __name__ == '__main__':
    test()
