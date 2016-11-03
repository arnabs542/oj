#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
202. Happy Number

Total Accepted: 95894
Total Submissions: 248237
Difficulty: Easy
Contributors: Admin

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any
positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1. Those numbers for which
this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
'''

class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = {n}
        while n != 1:
            n = int(sum(map(lambda x: int(x) ** 2, str(n))))
            if n in visited:
                return False
            else:
                visited.add(n)

        print(n, 'is a happy number')
        return True

    def isHappyFloydCycleDetection(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # TODO: floyd cycle detection algorithm


def test():
    solution = Solution()

    assert solution.isHappy(19)

if __name__ == '__main__':
    test()
