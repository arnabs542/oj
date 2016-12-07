#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
214. Shortest Palindrome

Total Accepted: 28159
Total Submissions: 128130
Difficulty: Hard
Contributors: Admin

Given a string S, you are allowed to convert it to a palindrome by adding
characters in front of it. Find and return the shortest palindrome you can find
by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".

SOLUTION:
    Find the longest palindrome prefix. Then insert the reverse part of substring
after such palindrome prefix before the original one.
    1. KMP Longest prefix that is also suffix look up table
    If we reverse the string, then the palindrome prefix becomes palindrome postfix,
and they are equal to each other by palindrome's definition. So the problem is now
transformed to find the LPS of `s + reversed(s)`. But the posefix should only be composed substring
of s itself, not any part of the reversed one, so we can add a out of vocabulary symbol between
s and reversed(s). Time Complexity is O(n).

'''

class Solution(object):

    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return self.shortestPalindromeBruteForce(s)
        # return self.shortestPalindromeBruteForce2(s)
        return self.shortestPalindromeKMP(s)

    def shortestPalindromeBruteForce(self, s):
        """
        :type s: str
        :rtype: str
        """
        # This is a brute force O(N²) solution, get Time Limit Exceeded
        mid = (len(s) - 1) // 2
        if s[:mid + 1] == s[mid + 1:][::-1]:
            # even length string, already palindrome
            return s
        # find the longest palindrome prefix
        for i in range(mid, -1, -1):
            if s[:i] == s[i + 1: i + 1 + i][::-1]:
                # s[i] is the center character of the palindrome substring
                s = s[i + 1 + i:][::-1] + s
                break
            elif s[:i] == (s[i: i + i])[::-1]:
                # s[i] is on the right side of the palindrome substring
                s = s[i + i:][::-1] + s
                break
        print(s)
        return s

    def shortestPalindromeBruteForce2(self, s):
        m = len(s)
        idx = 0
        s_reversed = s[::-1]

        # O(n)
        for i in range(m - 1, -1, -1):
            # O(n)
            if s.startswith(s_reversed[m - i - 1:]):
                idx = i
                break
        # O(N²)

        # longest paindrome prefix
        s = s[idx + 1:][::-1] + s
        return s

    def shortestPalindromeKMP(self, s):
        # build up a LPS(Longest Prefix that is also a Suffix) lookup table
        if not s:
            return s
        text = s + '\xff' + s[::-1]
        lps = [0] * len(text)
        q = 0
        for i in range(1, len(text)):
            while q and text[i] != text[q]:
                q = lps[q - 1]
            if text[i] == text[q]:
                q += 1
            lps[i] = q

        length = lps[-1]
        s = s[length:][::-1] + s
        print(lps, text, length)
        print(s)
        return s

    # TODO: ROLLING HASH for longest palindrome prefix


def test():
    solution = Solution()
    assert solution.shortestPalindrome("") == ""
    assert solution.shortestPalindrome("aabba") == "abbaabba"
    assert solution.shortestPalindrome("aacecaaa") == "aaacecaaa"
    assert solution.shortestPalindrome("abcd") == "dcbabcd"
    assert solution.shortestPalindrome("abbacd") == "dcabbacd"
    assert solution.shortestPalindrome("aaaa") == "aaaa"

    print('self test passed')

if __name__ == '__main__':
    test()
