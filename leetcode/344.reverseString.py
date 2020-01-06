#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
344. Reverse String

Total Accepted: 110895
Total Submissions: 193287
Difficulty: Easy
Contributors: Admin

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

==============================================================================================
SOLUTION:
    1. recursion
    2. stack
    3. two pointers
'''

class Solution(object):

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return self.reverseStringBuiltIn(s)
        return self.reverseStringTwoPointers(s)

    def reverseStringBuiltIn(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

    def reverseStringTwoPointers(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        i, j = 0, len(l) - 1
        while i < j:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
            pass
        return ''.join(l)

def test():
    solution = Solution()

    assert solution.reverseString("hello") == "olleh"

    print('self test passed')

if __name__ == '__main__':
    test()
