#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
242. Valid Anagram

Total Accepted: 122936
Total Submissions: 276778
Difficulty: Easy
Contributors: Admin

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

================================================================================
SOLUTION

1. Hash count

Complexity: O(26)

Adversarial approach:
    In one pass increase the count, in the other one pass decrease the count.

2. sort and compare, O(nlogn + n)

3. Hashing.
prime factors = [
2, 3, 5, 7, 11,
13, 17, 19, 23, 29,
31, 37, 41, 43, 47,
53, 59, 61, 67, 71,
73, 79, 83, 89, 97,
101, 107]

1) Use product of prime factors to as the hash code.
    But there is a potential risk of overflowing. Taking logarithm of the hash code will
reduce the precision.
2) Use occurrence count weighted (co)prime numbers as hash code.
    Wrong! Because the coefficient may not be coprime with those prime numbers. Their might
be hash collision.

3. Optimized counting sort to reduce the sorting complexity to O(n).

'''

class Solution(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return self.isAnagramHash(s, t)
        return self.isAnagramTwoPointers(s, t)

    def isAnagramHash(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # for unicode string: use hash table instead of array emulation
        occurrence = [0] * 26
        for c in s: occurrence[ord(c) - ord('a')] += 1
        for c in t: occurrence[ord(c) - ord('a')] -= 1
        return max(occurrence) == min(occurrence) == 0

    def isAnagramTwoPointers(self, s: str, t: str):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1, l2 = sorted(s), sorted(t)
        if len(l1) != len(l2):
            return False
        i = 0
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False
        return True

def test():
    solution = Solution()
    assert solution.isAnagram('anagram', 'nagaram')
    assert not solution.isAnagram('rat', 'cat')

    print('self test passed')

if __name__ == '__main__':
    test()
