#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
242. Valid Anagram

Total Accepted: 122936
Total Submissions: 276778
Difficulty: Easy
Contributors: Admin

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

==============================================================================================
SOLUTION:
    1. hash table to record occurrence count
    2. sort and two pointers
'''

class Solution(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return self.isAnagramHash(s, t)
        return self.isAnagramTwoPointers(s, t)

    def isAnagramHash(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # for unicode string: use hash table instead of array emulation
        occurrence = [0] * 26
        for c in s: occurrence[ord(c) - ord('a')] += 1
        for c in t: occurrence[ord(c) - ord('a')] -= 1
        return max(occurrence) == min(occurrence) == 0

    def isAnagramTwoPointers(self, s: str, t: str):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1, l2 = sorted(s), sorted(t)
        if len(l1) != len(l2):
            return False
        i = 0
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False
        return True

def test():
    solution = Solution()
    assert solution.isAnagram('anagram', 'nagaram')
    assert not solution.isAnagram('rat', 'cat')

    print('self test passed')

if __name__ == '__main__':
    test()
