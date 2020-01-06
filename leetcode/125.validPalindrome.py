#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

==============================================================================
SOLUTION

1. Two pointers
Scan from both ends to middle

'''


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # result = self._isPalindromeTwoPointersUgly(s)
        result = self._isPalindromeTwoPointers(s)
        print(s, result)
        return result

    def _isPalindromeTwoPointersUgly(self, s):
        n = len(s)
        if n == 0:
            return True
        i = 0
        j = n - 1
        for i in range(n):
            # print "i:%d "%i,s[i].lower(),",",s[j].lower()
            if i >= j:
                return True
            if s[i].isalnum():
                while not s[j].isalnum():
                    j = j - 1

                if s[i].lower() != s[j].lower():
                    return False
                else:
                    j = j - 1
                    pass

            else:
                pass

    def _isPalindromeTwoPointers(self, s: str):
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].upper() != s[j].upper():
                return False
            else:
                i += 1
                j -= 1
            pass
        return i >= j

def test():
    assert (Solution().isPalindrome(""))
    assert (Solution().isPalindrome("A man, a plan, a canal: Panama"))
    assert not (Solution().isPalindrome("race a car"))
    assert not Solution().isPalindrome("1a2")

    print("self test passed")

if __name__ == "__main__":
    test()

