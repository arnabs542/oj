#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
306. Additive Number

Total Accepted: 17849
Total Submissions: 66351
Difficulty: Medium
Contributors: Admin

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers,
each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3
is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive
number.

Follow up:
How would you handle overflow for very large input integers?
'''

class Solution(object):

    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        return self.isAdditiveNumberDFS(num)

    def isAdditiveNumberDFS(self, num, prev=''):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3:
            return False
        n = len(num)
        for i in range(n // 2):
            # length j - i <= n - 1 - j
            for j in range(i + 1, (n + i - 1) // 2 + 1):
                result = self.check(num[:i + 1], num[i + 1:j + 1], num[j + 1:])
                if result:
                    return True

        return False

    def check(self, num1, num2, num):
        print('checking', num1, num2, num)
        if num1.startswith('0') and num1 != '0' or \
           num2.startswith('0') and num2 != '0':
            return False
        if not num:
            return True
        num3 = self.add(num1, num2)
        if num.startswith(num3):
            return self.check(num2, num3, num[len(num3):])
        return False

    def add(self, num1, num2):
        '''
        string addition
        '''
        m, n = len(num1), len(num2)
        num3 = []
        carry = 0
        for i in range(max(m, n)):
            digit1 = int(num1[m - 1 - i]) if i < m else 0
            digit2 = int(num2[n - 1 - i]) if i < n else 0
            carry, digit3 = divmod(digit1 + digit2 + carry, 10)
            num3.insert(0, str(digit3))

        if carry:
            num3.insert(0, str(carry))
        num3 = ''.join(num3)

        return num3

def test():
    solution = Solution()
    assert solution.add('1', '199') == '200'
    assert solution.isAdditiveNumber('112358')
    assert solution.isAdditiveNumber('199100199')
    assert solution.isAdditiveNumber("198019823962")
    assert not solution.isAdditiveNumber("19910011992")
    assert solution.isAdditiveNumber("101")
    assert solution.isAdditiveNumber("000")
    print('self test passed')

if __name__ == '__main__':
    test()
