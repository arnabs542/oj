#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
258. Add Digits

Total Accepted: 140988
Total Submissions: 281622
Difficulty: Easy
Contributors: Admin

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Hint:

1. A naive implementation of the above process is trivial. Could you come up with other methods?
2. What are all the possible results?
3. How do they occur, periodically or randomly?
4. You may find this Wikipedia(https://en.wikipedia.org/wiki/Digital_root) article useful.


==============================================================================================
SOLUTION

By writing the cases down, we can easily find the pattern behind this:
    The result occurs periodically with 9.

'''

class Solution(object):

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num % 9 if num == 0 or num % 9 else 9


def test():
    solution = Solution()

    assert solution.addDigits(0) == 0
    assert solution.addDigits(1) == 1
    assert solution.addDigits(9) == 9

    assert solution.addDigits(10) == 1
    assert solution.addDigits(11) == 2
    assert solution.addDigits(12) == 3
    assert solution.addDigits(18) == 9

    assert solution.addDigits(19) == 1
    assert solution.addDigits(20) == 2
    assert solution.addDigits(21) == 3
    assert solution.addDigits(27) == 9

    assert solution.addDigits(28) == 1
    assert solution.addDigits(38) == 2

    print("self test passed")

if __name__ == '__main__':
    test()
