#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
402. Remove K Digits

Total Accepted: 6539
Total Submissions: 25579
Difficulty: Medium
Contributors: Admin

Given a non-negative integer num represented as a string, remove k digits from the number
so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain
leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
===============================================================================================
SOLUTION:
    Greedy strategy: find first two descending numbers in a row from most to least significant
places until at the end of string.

Implementation:
    1. scan the list
    2. regular expression substitution
'''

class Solution(object):

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        l = list(num)
        i = 0
        while k:
            while i < len(l) - 1 and l[i] <= l[i + 1]:
                i += 1
            l.pop(i)
            i = max(0, i - 1)
            k -= 1
            pass

        print(l)
        return ''.join(l).lstrip('0') or '0'

def test():
    solution = Solution()

    assert solution.removeKdigits("1432219", 3) == '1219'
    assert solution.removeKdigits("10200", 1) == '200'
    assert solution.removeKdigits("10200", 2) == '0'
    assert solution.removeKdigits("10", 2) == '0'
    assert solution.removeKdigits("1294", 2) == '12'
    assert solution.removeKdigits("1234567890", 9) == '0'
    print('self test passed')

if __name__ == '__main__':
    test()
