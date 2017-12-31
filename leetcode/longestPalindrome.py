#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
409. Longest Palindrome

Total Accepted: 21959
Total Submissions: 49455
Difficulty: Easy
Contributors: Admin

Given a string which consists of lowercase or uppercase letters, find the length of
the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

================================================================================
SOLUTION

1. Brute force

Exhaust all substring, and verify.
Complexity: O(2ⁿ).

2. Construction - Count
Use a look up table to store occurrence count of all characters.
For a palindrome string, there will be at most one character that appears odd times(once).

Complexity: O(N), O(1)

3. ?
Denote the number of letters that occur odd times by count_odd, then the longest
palindrome length is len(s) - (count_odd - 1)

Then we setup two sets containing letters with odd and even occurrence respectively. While
the sweep the string, the occurrence state transits. Finally, the size of odd set is the number
of odd letters.

Complexity: O(n), O(1?).


'''

from collections import Counter

class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = self._longestPalindromeCount(s)
        # result = self._longestPalindromeSet(s)

        print(s, result)

        return result

    def _longestPalindromeCount(self, s):
        counter = Counter(s)
        odd = 0
        result = 0
        # print(s, counter)
        for c in counter:
            if counter[c] % 2:
                result += (counter[c] - 1)
                odd = 1
            else:
                result += counter[c]
            # print(c, counter[c], result)
            pass
        return result + 1 if odd else result

    def _longestPalindromeSet(self, s):
        # TODO: explain this idea?
        odd, even = set(), set()
        for c in s:
            if c not in odd and c not in even:
                odd.add(c)
            elif c in odd:
                odd.remove(c)
                even.add(c)
            else:
                even.remove(c)
                odd.add(c)
        return len(s) - len(odd) + 1 if odd else len(s)


def test():
    solution = Solution()

    assert solution.longestPalindrome("") == 0
    assert solution.longestPalindrome("ccccdd") == 6
    assert solution.longestPalindrome("abccccdd") == 7
    assert solution.longestPalindrome("abccccdd") == 7

    print("self test passed")


if __name__ == '__main__':
    test()
