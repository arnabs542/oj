#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
524. Longest Word in Dictionary through Deleting
Medium

Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"

Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"

Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.

================================================================================
SOLUTION

1. Brute force
For each word in dictionary, check whether it's valid through two pointers comparison.

Complexity: O((m+l)n), where m is the length of s, n is the size of dictionary,
l is the average length of words in dictionary.

If sorting, the complexity is dominated by O(lmlogm).

2. Trie?
Build a trie from the dictionary.

Then search the trie. For each node in the trie, we have multiple choices.
Try to match every child character through deleting.

Complexity: O(n(l+m)) in worst case, where n is the size of dictionary, l is the average length
of words in dictionary.


"""

class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        result = self._findLongestWordBruteForce(s, d)

        print(s, d, " => ", result)

        return result

    def _findLongestWordBruteForce(self, s, d: list):
        d.sort(key=lambda x: (-len(x), x)) # length, lexical order
        def match(w):
            i, j = 0, 0
            while i < len(s) and j < len(w):
                j += s[i] == w[j]
                i += 1
            return j >= len(w)

        for w in d:
            if match(w): return w

        return ""

def test():
    solution = Solution()

    assert solution.findLongestWord("", []) == ""
    assert solution.findLongestWord("", ["a", "b"]) == ""
    assert solution.findLongestWord("ab", ["a", "b"]) == "a"
    assert solution.findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"]) == "apple"
    assert solution.findLongestWord("abpcplea", ["a", "b", "c"]) == "a"

    print("self test passed!")

if __name__ == '__main__':
    test()
