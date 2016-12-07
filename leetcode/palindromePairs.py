#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
336. Palindrome Pairs

Total Accepted: 14567
Total Submissions: 62637
Difficulty: Hard
Contributors: Admin

Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list,
so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]

Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
==============================================================================================
SOLUTION:
    Hash table to store (string, index).
    Then, work to reduce the time complexity of O(N²) in a trivial solution.

    There is concatenation operation to get the palindrome string. Then there would be a
PALINDROME PREFIX/SUFFIX problem involved, which is similar to 'Shortest Palindrome' problem.
Given a string words[j], if we want to prepend words[i] in front of it to get a palindrome, then
words[i] must be a palindrome prefix of words[j] or words[j] is the palindrome suffix of words[i].
If the concatenation is (words[j]+words[i]), we can apply the same procedure to words[i]. Then we
can do this is O(m*n) time complexity, where n is the size of words list and m is the average word
length.

We have to consider all palindrome prefixes instead of the longest. And the palindrome prefixes
can be solved with the LPS(longest prefix that is also a suffix) construction algorithm in KMP.
'''
class Solution(object):

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        return self.palindromePairsKMP(words)

    def _LPS(self, s):
        '''
        s: str
        '''
        # compute LPS
        s_reversed = s[::-1]
        s_cat = s + '#' + s_reversed
        # auxiliary LPS array
        lps = [0] * len(s_cat)
        q = 0
        for i in range(1, len(s_cat)):
            # print(q, s_cat[q], s_cat[i])
            while q and s_cat[q] != s_cat[i]:
                q = lps[q - 1]
            if s_cat[q] == s_cat[i]:
                q += 1
            lps[i] = q
        # print(s_cat, lps)
        l = lps[-1]
        while l:
            yield l
            l = lps[l - 1]
        yield l

    def palindromePairsKMP(self, words: list):
        word2idx = {t[1]: t[0] for t in enumerate(words)}
        pairs = set()
        for j, _ in enumerate(words):
            # find palindrome prefix/suffix of words[j], reverse the remaining part,
            # check its existence in the word2idx
            for prefix_len in self._LPS(words[j]):
                remaining = words[j][prefix_len:][::-1]
                i = word2idx.get(remaining)
                if i is not None and i != j:
                    pairs.add((i, j))

            for prefix_len in self._LPS(words[j][::-1]):
                remaining = words[j][:len(words[j]) - prefix_len][::-1]
                i = word2idx.get(remaining)
                if i is not None and i != j:
                    pairs.add((j, i))
        pairs = sorted(map(lambda x: list(x), pairs))
        print(pairs)
        return pairs

    def palindromePairsTrie(self, words: list):
        # TODO: trie tree based solution
        pass

def test():
    solution = Solution()

    assert list(solution._LPS('abcd')) == [1, 0]
    assert list(solution._LPS('lls')) == [2, 1, 0]
    assert list(solution._LPS('sssll')) == [3, 2, 1, 0]

    assert solution.palindromePairs(["a", "abc", "aba", ""]) == [
        [0, 3], [2, 3], [3, 0], [3, 2]]

    assert solution.palindromePairs(["bat", "tab", "cat"]) == [[0, 1], [1, 0]]
    assert solution.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]) == [
        [0, 1], [1, 0], [2, 4], [3, 2]]
    assert solution.palindromePairs(["b", ""]) == [[0, 1], [1, 0]]
    assert solution.palindromePairs(["a", "b", "c", "ab", "ac", "aa"]) == [
        [0, 5], [1, 3], [2, 4], [3, 0], [4, 0], [5, 0]]
    print('self test passed')

if __name__ == '__main__':
    test()
