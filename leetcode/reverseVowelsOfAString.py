#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
345. Reverse Vowels of a String

Total Accepted: 55060
Total Submissions: 149123
Difficulty: Easy
Contributors: Admin

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
'''

class Solution(object):

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.reverseVowelsTwoPointers(s)

    def reverseVowelsTwoPointers(self, s: str):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and l[i].lower() not in ('a', 'o', 'e', 'i', 'u'):
                i += 1
            while i < j and l[j].lower() not in ('a', 'o', 'e', 'i', 'u'):
                j -= 1
            if i < j:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
        return ''.join(l)

def test():
    solution = Solution()

    assert solution.reverseVowels("hello") == "holle"
    assert solution.reverseVowels("leetcode") == "leotcede"

    print('self test passed')

if __name__ == '__main__':
    test()
