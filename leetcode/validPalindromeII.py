#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
680. Valid Palindrome II

Easy

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

================================================================================
SOLUTION

1. Brute force - depth first search
For each character, try both removing and not removing it, and check whether it's a palindrome

Complexity: O(N²), O(1)

2. Greedy strategy with Depth first search
Above solution considers too many duplicate or unnecessary computations.

If there is no need to delete a character, then the string itself is a palindrome, simple case.
If deleting a character makes it palindrome, then, what kind of character will be deleted?

If we set up two pointers i and j, scanning from both ends to middle, and if s[i] == s[j],
shall anyone of them be deleted?

Intuitive tells us not to delete any of them.

For example, if deleting any of them makes it a palindrome, then string s must be like "aabba".
Here, deleting the first 'a' makes it palindrome.
But actually, we can leave 'a' on both ends, then we have "abb", now, it's the situation where
we want to delete a.

The point here is, we can always find an alternative character to delete, rather than deleting
a character when two pointers have same character pointed to.


"abca"
"abdca"
"aabba"

Complexity: O(N), O(1)

"""

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = self._validPalindromeGreedy(s)

        print(s, result)

        return result

    def _validPalindromeGreedy(self, s):
        def dfs(low, high, nDelete):
            while low < high:
                if s[low] == s[high]:
                    low += 1
                    high -=1
                else:
                    if not nDelete:
                        return False

                    return any((dfs(low + 1, high, 0), dfs(low, high - 1, 0)))
            return True
        return dfs(0, len(s) - 1, 1)

def test():
    solution = Solution()

    s = ""
    assert solution.validPalindrome(s)

    s = "a"
    assert solution.validPalindrome(s)

    s = "ab"
    assert solution.validPalindrome(s)

    s = "aba"
    assert solution.validPalindrome(s)

    s = "abca"
    assert solution.validPalindrome(s)

    s = "aabba"
    assert solution.validPalindrome(s)

    print("self test passed!")

if __name__ == '__main__':
    test()
