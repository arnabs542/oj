#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
318. Maximum Product of Word Lengths

Total Accepted: 43628
Total Submissions: 102247
Difficulty: Medium
Contributors: Admin

Given a string array words, find the maximum value of length(word[i]) * length(word[j])
where the two words do not share common letters. You may assume that each word will contain
only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.

==============================================================================================
SOLUTION

To check whether two words contain common letters, we can preprocess features:
    1) Represent words by letter set
    2) Encode with bit representation: since there are only 26 letters, 36 < #(integer bits)

----------------------------------------------------------------------------------------------
1. Brute force.
Search in all the pairs, check condition with set operation
Complexity: O(N²).

2. Encode with bit representation
Encode the information what kind of letters compose of a word with bit representation. Since
there are only 26 letters, we can literally use an integer, 26 bits of which correspond to
26 letters from 'a' to 'z'.

Complexity: O(N²)

3. Optimize with greedy strategy
For two words with same encoding, the longer one is preferred, apparently!

'''

class Solution(object):

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # return self._maxProductNaive(words)
        # return self._maxProductBit(words)
        return self._maxProductBitOpt(words)

    def _maxProductNaive(self, words):
        max_product = 0
        word2set = {}
        for word in words:
            word2set[word] = set(word)
        for i, w in enumerate(words):
            for j in range(i + 1, len(words)):
                if word2set[w].intersection(word2set[words[j]]):
                    continue
                product = len(w) * len(words[j])
                max_product = max(max_product, product)
        return max_product

    def _maxProductBit(self, words):
        max_product = 0
        word2vector = {}
        def encode(w):
            n = 0
            for c in w:
                n |= (0x1 << (ord(c) - ord('a')))
            return n

        for word in words:
            word2vector[word] = encode(word)
        for i, w in enumerate(words):
            for j in range(i + 1, len(words)):
                if word2vector[w] & word2vector[words[j]]:
                    continue
                product = len(w) * len(words[j])
                max_product = max(max_product, product)
        return max_product

    def _maxProductBitOpt(self, words):
        # DONE: faster algorithm with help of greedy strategy
        bit2len = {}
        for word in words:
            mask = 0
            for c in word:
                mask |= (0x1 << (ord(c) - ord('a')))
            bit2len[mask] = max(bit2len.get(mask, 0), len(word))
        max_product = max([bit2len[x] * bit2len[y]
                           for y in bit2len
                           for x in bit2len if not x & y] or [0])
        return max_product

def test():
    solution = Solution()

    assert solution.maxProduct([]) == 0
    assert solution.maxProduct(["a", "b"]) == 1
    assert solution.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) == 16
    assert solution.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]) == 4
    assert solution.maxProduct(["a", "aa", "aaa", "aaaa"]) == 0

    print("self test passed")

if __name__ == '__main__':
    test()
