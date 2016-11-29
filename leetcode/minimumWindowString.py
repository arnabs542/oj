#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
76. Minimum Window Substring

Total Accepted: 81013
Total Submissions: 346371
Difficulty: Hard
Contributors: Admin

Given a string S and a string T, find the minimum window in S which will contain all the
characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one
unique minimum window in S.

==============================================================================================
SOLUTION:
    This is apparently a MAXIMUM SUBARRAY SUM' variant, which can be solved with Dynamic
Programming with STATE defined as:

    THE NUMBER OF CHARACTERS TO MATCH with current subarray(substring) ending with current
position. And use TWO POINTERS representing the subarray's start and end position to keep
track of the minimum window(subarray).

But how to CHECK that the TARGET STRING T IS already MATCHED EFFICIENTLY?

    Use a COUNTER RECORDING THE TARGET'S CHARACTERS' OCCURRENCES COUNT. And the number of
characters that need to be matched is the length of target string, denoted by `missing`.
    Scan the source string. Encountering a character, decrease its Counter value. And if its
Counter value was positive, decrease `missing` by 1. When missing is zero, we have a match.
To find the minimum substring, we need to pop out the leftmost that won't make the match
invalid. Such characters are those with negative value in Counter.
'''

from collections import Counter

class Solution(object):

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # return self.minWindowDP(s, t)
        return self.minWindowDP2(s, t)

    def minWindowDP(self, s: str, t: str) -> str:
        counter, missing = Counter(t), len(t)
        begin, end = 0, 0
        i = j = 0
        for j, c in enumerate(s):
            missing -= counter[c] > 0
            counter[c] -= 1
            print(missing, i, j, s[i:j + 1], counter)
            while missing == 0 and i <= j + 1:
                if end == 0 or j - i + 1 < end - begin:
                    begin, end = i, j + 1
                if i > j: break
                counter[s[i]] += 1
                if counter[s[i]] > 0: missing += 1
                i += 1
            pass
        print('result', s[begin:end])
        return s[begin: end]

    def minWindowDP2(self, s: str, t: str) -> str:
        counter = Counter(t)
        i, begin, end = 0, 0, 0

        missing = len(t) # This is our very core STATE: number of chars to match yet

        for j, c in enumerate(s):
            missing -= counter[c] > 0 # state transition
            counter[c] -= 1
            if missing == 0:
                while i <= j and counter[s[i]] < 0:
                    counter[s[i]] += 1
                    i += 1
                if end == 0 or j - i + 1 < end - begin:
                    begin, end = i, j + 1
        print('result', s[begin:end])
        return s[begin: end]

def test():
    solution = Solution()

    assert solution.minWindow("AA", "AA") == "AA"
    assert solution.minWindow("", "") == ""
    assert solution.minWindow("", "A") == ""
    assert solution.minWindow("A", "") == ""
    assert solution.minWindow("ABC", "") == ""
    assert solution.minWindow("ADOBECODEBANC", "ABC") == "BANC"

    print('self test passed')

if __name__ == '__main__':
    test()
