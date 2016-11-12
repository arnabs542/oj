#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
43. Multiply Strings

Total Accepted: 77905
Total Submissions: 308980
Difficulty: Medium
Contributors: Admin

Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:
The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.

================================================================================================
SOLUTION:
    Start from right to left, perform multiplication on every pair of digits, and add them together.
 `num1[i] * num2[j]` will be placed at indices `[i + j`, `i + j + 1]`

'''
class Solution(object):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        result = [0 for i in range(m + n + 1)]
        # i, j the index counting from the end of string, and starting with 0
        for i in range(m):
            for j in range(n):
                product = int(num1[m - 1 - i]) * int(num2[n - 1 - j])
                p = (m + n) - (i + j)
                # print(i, j, p, 'product', num1[m - 1 - i], num2[n - 1 - j], product)
                s = product + result[p]
                result[p] = s % 10
                result[p - 1] += s // 10

        # print(result)
        result_str = ''.join(map(lambda x: str(x), result)).lstrip('0')
        if not result_str:
            result_str = '0'
        return result_str

def test():
    solution = Solution()
    assert solution.multiply('0', '0') == '0'
    assert solution.multiply('1234', '0') == '0'
    assert solution.multiply('5', '2') == '10'
    assert solution.multiply('5', '21') == '105'
    assert solution.multiply('25', '25') == '625'
    assert solution.multiply('1234', '8765') == '10816010'
    assert solution.multiply("401716832807512840963",
                             "167141802233061013023557397451289113296441069")
    print('self test passed')

if __name__ == '__main__':
    test()
