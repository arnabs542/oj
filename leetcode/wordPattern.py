#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
290. Word Pattern

Total Accepted: 62434
Total Submissions: 195261
Difficulty: Easy
Contributors: Admin

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in
pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase
letters separated by a single space.

==============================================================================================
SOLUTION

1. Hash table.

'''

class Solution(object):

    def wordPattern(self, pattern, s):
        """
        :type pattern: s
        :type str: s
        :rtype: bool
        """
        return self.wordPatternHash(pattern, s)

    def wordPatternHash(self, pattern, s):
        words = s.split()
        if len(words) != len(pattern):
            return False
        word2ch, ch2word = {}, {}
        for i in range(len(pattern)):
            if words[i] not in word2ch and pattern[i] not in ch2word:
                word2ch[words[i]] = pattern[i]
                ch2word[pattern[i]] = words[i]
            else:
                if word2ch.get(words[i], '#') != pattern[i]:
                    return False
        return True

def test():
    solution = Solution()

    assert solution.wordPattern("abba", "dog cat cat dog")
    assert not solution.wordPattern("abba", "dog cat cat fish")
    assert not solution.wordPattern("aaaa", "dog cat cat dog")
    assert not solution.wordPattern("abba", "dog dog dog dog")

    print("self test passed")

if __name__ == '__main__':
    test()
