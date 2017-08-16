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

1. Brute force.
Enumerate all windows, and check existence.

Complexity: O(N²).

2. Sliding window

Slide the window, maintain the state transition in dynamic programming approach.

We want find a window/substring that contains target string as a substring.

This is a variant MAXIMUM SUBARRAY SUM problem, which is about to find a required window
along a linear structure.

STATE = (The NUMBER OF CHARACTERS TO MATCH in current window/subarray).

And use TWO POINTERS representing start and end position of the window.

But how to CHECK whether target string t is already matched efficiently?

The technique is sliding window counter.

Maintain a HASH TABLE counter storing how many occurrences each character should be
matched yet, together with a INTEGER `missing` indicating how many characters are
matched against the target string.

Extend the window from right. Encountering a character, decrease its counter value.
And if its Counter value was positive, decrease `missing` by 1. When missing is zero,
we have a match. Once the current window is a match, update the optimal solution so far,
and try to find a better one by shrinking the window from left side.

To shrink the sliding window, we pop out the unnecessary left most characters which have
more occurrences than required. Unnecessary characters are those with negative value in Counter.
Then repeat the extending process.

Complexity: amortized O(N)

----------------------------------------------------------------------------------------------
Similar substring problems:

https://leetcode.com/problems/minimum-window-substring/
https://leetcode.com/problems/longest-substring-without-repeating-characters/
https://leetcode.com/problems/substring-with-concatenation-of-all-words/
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Sliding window technique is the one to rule them all!

Slide a window over the data structure, and apply state transition recurrence relation.

In substring problem, we can maintain a HASH TABLE to store information within the window.
Maybe together with an integer state indicating how many characters need to be matched yet.

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
        '''
        Rewrite the solution
        '''
        counter = Counter(t)
        i, begin, end = 0, 0, 0

        missing = len(t) # STATE: number of chars to match yet

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
