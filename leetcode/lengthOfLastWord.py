#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
58. Length of Last Word

Total Accepted: 143198
Total Submissions: 452436
Difficulty: Easy
Contributor: LeetCode

Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.

==============================================================================================
SOLUTION

'''

class Solution(object):

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.lengthOfLastWordSplit(s)

    def lengthOfLastWordSplit(self, s):
        a = s.split()
        return (a and len(a[-1])) or 0


def test():
    solution = Solution()

    assert solution.lengthOfLastWord("") == 0
    assert solution.lengthOfLastWord("       ") == 0
    assert solution.lengthOfLastWord("world") == 5
    assert solution.lengthOfLastWord("hello world") == 5

    print("self test passed")

if __name__ == '__main__':
    test()

