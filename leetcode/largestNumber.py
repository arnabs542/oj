#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
179. Largest Number

Total Accepted: 58297
Total Submissions: 279382
Difficulty: Medium
Contributors: Admin

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of
an integer.

SOLUTION:
    Lexicographical order.
    The Lexicographical order of two number x, y is considered with respect to
their catenations' order:
    def cmp(x, y):
        return str(x) + str(y) > str(y) + str(x)
'''


class Solution:
    # @param {integer[]} nums
    # @return {string}
    @classmethod
    def largestNumber(cls, nums):
        def cmp(x, y):
            return str(x) + str(y) < str(y) + str(x)
        def cmp2key(mycmp):
            class K(object):
                def __init__(self, obj, *args):
                    self.obj = obj
                def __lt__(self, other):
                    return mycmp(self.obj, other.obj)
            return K
        nums.sort(key=cmp2key(cmp), reverse=True)
        while len(nums) >= 2 and nums[0] == 0:
            nums.pop(0)
        print(nums)
        return ''.join(map(lambda x: str(x), nums))

def test():
    assert Solution.largestNumber([3, 30, 34, 5, 9]) == '9534330'
    assert Solution.largestNumber([0, 0]) == '0'
    assert Solution.largestNumber([0, 1, 0]) == '100'
    print('self test passed')

if __name__  == '__main__':
    test()

