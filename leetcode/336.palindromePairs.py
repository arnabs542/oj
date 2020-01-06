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

================================================================================
SOLUTION

1. Brute force combination

Hash table to store (string, index).

For each word, try to find palindrome pair.

Complexity: O(N²M),
where N is the word list length and M is the average word length.

--------------------------------------------------------------------------------
EXPLOIT THE PREFIX OR SUFFIX STRUCTURE to avoid unnecessary computations

2. Palindrome prefix

Brute force combination is in a word-wise perspective, if the problem is
inspected inside the word's structure: prefix and suffix.

Then, work to reduce the time complexity of O(N²) in a trivial solution.

Each word has a palindrome prefix or suffix.
If two words can form a palindrome string by concatenation, then one must be
reverse of complement of the other one's palindrome prefix or suffix.

It is similar to 'Shortest Palindrome' problem.
Then it's reduced to palindrome prefix problem, which can be solved with
KMP state machine, by computing LPS(longest prefix that's also a suffix) of
concatenation of the word and reverse.

For each string, compute its palindrome prefixes and suffixes. Query whether
the complement of palindrome part exist in the words list(dictionary).

Remember, consider all palindrome prefixes instead of the longest.
Another problem is to avoid duplicate pairs. Duplicate occur, when one is another
one's mirror.

For each word, computing lps is O(m), and there are at most O(m) possible lps.
For each lps, it takes average O(m) complexity to check existence.

Complexity: O(nm²), where n is the size of words list and m is the average word.

3. Trie - match prefix?
Use an augmented prefix tree?

'''
class Solution(object):

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        result = self._palindromePairsKMP(words)

        print(words, '=>', result)

        return result

    def _LPS(self, pattern):
        '''
        s: str
        '''
        lps = [0] * len(pattern)
        q = 0
        for i in range(1, len(pattern)):
            # print(q, pattern[q], pattern[i])
            while q and pattern[q] != pattern[i]:
                q = lps[q - 1]
            if pattern[q] == pattern[i]:
                q += 1
            lps[i] = q
        # print(pattern, lps)
        l = lps[-1]
        while l:
            yield l
            l = lps[l - 1]
        yield l

    def _palindromePairsKMP(self, words: list):
        word2idx = {t[1]: t[0] for t in enumerate(words)}
        pairs = set()
        for j, _ in enumerate(words):
            # find palindrome prefix/suffix of words[j], reverse the remaining part,
            # check its existence in the word2idx
            s = words[j] + '#' + words[j][::-1]
            for prefix_len in self._LPS(s):
                remaining = words[j][prefix_len:][::-1]
                i = word2idx.get(remaining)
                if i is not None and i != j:
                    pairs.add((i, j))

            s = words[j][::-1] + '#' + words[j]
            for suffix_len in self._LPS(s):
                remaining = words[j][:len(words[j]) - suffix_len][::-1]
                i = word2idx.get(remaining)
                if i is not None and i != j:
                    pairs.add((j, i))
        pairs = sorted(map(lambda x: list(x), pairs))
        return pairs

    def palindromePairsTrie(self, words: list):
        # TODO: trie tree based solution
        pass

def test():
    solution = Solution()

    # assert list(solution._LPS('abcd')) == [1, 0]
    # assert list(solution._LPS('lls')) == [2, 1, 0]
    # assert list(solution._LPS('sssll')) == [3, 2, 1, 0]

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
