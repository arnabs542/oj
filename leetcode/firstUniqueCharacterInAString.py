#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
387. First Unique Character in a String

Total Accepted: 46134
Total Submissions: 100628
Difficulty: Easy
Contributors: Admin

Given a string, find the first non-repeating character in it and return it's index. If it
doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.

==============================================================================================
SOLUTION

1. Brute force solution. Check every possible character in string, O(N²).
2. Hashing occurrence count, O(N).

'''

class Solution(object):

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.firstUniqCharSet(s)

    def firstUniqCharSet(self, s):
        counter = {}
        for i, c in enumerate(s):
            counter[c] = counter.get(c, 0) + 1
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i
        return -1

def test():
    solution = Solution()

    assert solution.firstUniqChar("leetcode") == 0
    assert solution.firstUniqChar("loveleetcode") == 2

    print("self test passed")

if __name__ == '__main__':
    test()
