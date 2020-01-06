#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
424. Longest Repeating Character Replacement

Given a string that consists of only uppercase English letters, you can replace any letter in
the string with another letter at most k times. Find the length of a longest substring containing
all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 10⁴.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

==============================================================================================
SOLUTION

1. Naive method
The target longest substring may be located in any interval [i, j], i.e., in O(N²) possible
positions.
Then we can traverse the string, for each substring s[i...j], check validity by drawing
statistics with respect to the letter distribution within that substring. The major letter
is the letter with most occurrence count, which other k letters will be replaced with.

Complexity: O(N³).

2. Sliding window
Of course, the substrings are overlapping with each other, giving result of duplicate calculation.
Can we eliminate that by maintaining some running state, such as occurrence statistics?

Use a letter counter hash table, sum of number of letters all letter occurrences. Then the
difference between the sum and the major letter's occurrence count is the number of letters
that need to be replaced with the major letter.

To slide the window means to extend and reduce the window when some condition is met.

Complexity: O(26N) = O(N)

'''

from collections import defaultdict

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        result = self._characterReplacementCounter(s, k)
        print(result)

        return result

    def _characterReplacementCounter(self, s, k):
        maxLength = 0

        counter = defaultdict(int)
        majorLetter = None

        i, j = 0, 0
        while j < len(s):
            # push into the window
            counter[s[j]] += 1
            if counter[s[j]] > counter[majorLetter]: majorLetter = s[j]
            totalCount = j - i + 1

            # pop out of the window
            if totalCount - counter[majorLetter] > k:
                counter[s[i]] -= 1
                for c in counter: # O(26)
                    if counter[majorLetter] < counter[c]:
                        majorLetter = c
                i += 1
                totalCount -= 1

            maxLength = max(maxLength, totalCount)
            j += 1
        return maxLength

def test():
    solution = Solution()

    assert solution.characterReplacement("", 2) == 0
    assert solution.characterReplacement("ABAB", 0) == 1
    assert solution.characterReplacement("ABAB", 2) == 4
    assert solution.characterReplacement("ABAB", 5) == 4
    assert solution.characterReplacement("ABBBA", 2) == 5
    assert solution.characterReplacement("AABBBA", 3) == 6
    assert solution.characterReplacement("AABBBA", 9) == 6
    assert solution.characterReplacement("ABABA", 2) == 5
    assert solution.characterReplacement("ABABA", 1) == 3

    print("self test passed")

if __name__ == '__main__':
    test()
