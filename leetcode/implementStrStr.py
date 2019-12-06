#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
28. Implement strStr()

Total Accepted: 141704
Total Submissions: 532861
Difficulty: Easy
Contributors: Admin
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.

SOLUTION
================================================================================
1. Brute force

O(mn)

2. KMP string matching algorithm - state machine with respect to max matched ending here

    The LPS(longest prefix that is also suffix) construction process is of amortized O(N) time
complexity.

Complexity: O(N)

'''

class Solution(object):

    def strStr(self, haystack: str, needle: str) -> int:
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # return self.strStrBuiltIn(haystack, needle)
        return self.strStrKMP(haystack, needle)

    def strStrBuiltIn(self, haystack: str, needle: str) -> int:
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

    def strStrKMP(self, haystack: str, needle: str) -> int:
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def preprocess(pattern):
            lps = [0] * len(pattern)
            q = 0
            for i in range(1, len(pattern)):
                while q and pattern[q] != pattern[i]:
                    q = lps[q - 1]
                if pattern[q] == pattern[i]:
                    q += 1
                lps[i] = q
            print(lps)
            return lps

        lps = preprocess(needle)
        q = 0
        if q == len(needle):
            return 0
        for i, _ in enumerate(haystack):
            while q and haystack[i] != needle[q]:
                q = lps[q - 1]
            if haystack[i] == needle[q]:
                q += 1

            if q == len(needle):
                return i - len(needle) + 1

        return -1

def test():
    solution = Solution()

    assert solution.strStr("bbaa", "aab") == -1
    assert solution.strStr('', '') == 0
    assert solution.strStr('hello', '') == 0
    assert solution.strStr('', 'hello') == -1
    assert solution.strStr('hello', 'lo') == 3
    assert solution.strStr("mississippi", "issip") == 4
    print('self test passed')

if __name__ == '__main__':
    test()
