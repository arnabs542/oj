#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
383. Ransom Note

Given an arbitrary ransom note string and another string containing letters from all the
magazines, write a function that will return true if the ransom note can be constructed
from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

==============================================================================================
SOLUTION

Each letter can only be used once: letter counting!

'''

class Solution(object):

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return self._canConstructCount(ransomNote, magazine)

    def _canConstructCount(self, ransomNote, magazine):
        count1, count2 = {}, {}
        for c in ransomNote:
            count1[c] = count1.get(c, 0) + 1
        for c in magazine:
            count2[c] = count2.get(c, 0) + 1
        for c in count1:
            if count1[c] > count2.get(c, 0):
                return False
        return True

    # TODO: we can also do this in two passes: 1 pass adding count, 1 pass to subtract the count

def test():
    solution = Solution()

    assert solution.canConstruct("", "") == True
    assert solution.canConstruct("", "asfsdf") == True
    assert not solution.canConstruct("a", "b")
    assert not solution.canConstruct("aa", "ab")
    assert solution.canConstruct("aa", "aab") == True

    print("self test passed")


if __name__ == '__main__':
    test()
