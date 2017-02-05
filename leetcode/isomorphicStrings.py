#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
205. Isomorphic Strings

Total Accepted: 87524
Total Submissions: 269836
Difficulty: Easy
Contributors: Admin

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving
the order of characters. No two characters may map to the same character but a character
may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

==============================================================================================
SOLUTION

1. Explicit hash table, like in 'Word Pattern'. Map between letters in s and t.

2. Implicit hash table: map the letters to its first occurrence INDEX.

'''

class Solution(object):

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.isIsomorphicFind(s, t)

    def isIsomorphicFind(self, s, t):
        return list(map(s.find, s)) == list(map(t.find, t))


def test():
    solution = Solution()

    assert solution.isIsomorphic("egg", "add")
    assert not solution.isIsomorphic("foo", "bar")
    assert solution.isIsomorphic("paper", "title")

    print("self test passed")

if __name__ == '__main__':
    test()
