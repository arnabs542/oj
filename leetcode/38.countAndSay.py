#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
38. Count and Say Add to List

Total Accepted: 122232
Total Submissions: 368762
Difficulty: Easy
Contributors: Admin

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

==============================================================================================
SOLUTION

1. Straightforward computing.

'''

class Solution(object):

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return self.countAndSay1(n)

    def countAndSay1(self, n):
        prev = "1"
        for _ in range(1, n):
            curr = ''
            digit, count = prev[0], 0
            for c in prev:
                if c == digit:
                    count += 1
                else:
                    curr += str(count) + digit
                    digit, count = c, 1
            # string end
            prev = curr + str(count) + digit
        return prev

def test():
    solution = Solution()

    assert solution.countAndSay(1) == "1"
    assert solution.countAndSay(2) == "11"
    assert solution.countAndSay(3) == "21"
    assert solution.countAndSay(9) == "31131211131221"

    print("self test passed")

if __name__ == '__main__':
    test()
