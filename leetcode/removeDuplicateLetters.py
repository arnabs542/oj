#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
316. Remove Duplicate Letters

Total Accepted: 22381
Total Submissions: 79923
Difficulty: Hard
Contributors: Admin

Given a string which contains only lowercase letters, remove duplicate letters so that every
letter appear once and only once. You must make sure your result is the smallest in
lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
==============================================================================================
SOLUTION:
    After analysis, I've observed that we need to
'''
class Solution(object):

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        ch2idx = {}
        for i in range(len(chars) - 1, -1, -1):
            if chars[i] in ch2idx:
                j = ch2idx[chars[i]]
                remove = i if chars[i + 1:j + 1] < chars[i:j] else j
                ch2idx[chars[i]] = remove ^ i ^ j
                chars[remove] = ''
            else:
                ch2idx[chars[i]] = i

        chars1 = chars

        chars = list(s)
        ch2idx = {}
        for i in range(len(chars)):
            if chars[i] in ch2idx:
                j = ch2idx[chars[i]]
                remove = i if ''.join(chars[j:i]) < ''.join(chars[j + 1:i + 1]) else j
                ch2idx[chars[i]] = remove ^ i ^ j
                chars[remove] = ''
            else:
                ch2idx[chars[i]] = i

        print(s, chars)
        print(min(''.join(chars1), ''.join(chars)))

        return min(''.join(chars1), ''.join(chars))
        return ''.join(chars)

def test():
    solution = Solution()

    assert solution.removeDuplicateLetters('bcabc') == 'abc'
    assert solution.removeDuplicateLetters('cbacdcbc') == 'acdb'
    assert solution.removeDuplicateLetters('abacb') == 'abc'

    print('self test passed')

test()
