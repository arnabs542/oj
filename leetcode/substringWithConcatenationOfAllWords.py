#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
30. Substring with Concatenation of All Words

Total Accepted: 65972
Total Submissions: 307130
Difficulty: Hard
Contributors: Admin

You are given a string, s, and a list of words, words, that are all of the same length. Find
all starting indices of substring(s) in s that is a concatenation of each word in words
exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).


================================================================================
SOLUTION

1. Brute force - combination C(n, 1)

Exhaust all possible string of length as the sum of given givens words, and verify.

Complexity: O((n - ml + 1)ml) where n is the length of given string s, m is the
number of given words, l is the length of given word.

One problem is that the given words may have common prefixes, resulting in
multiple search branches when matching the substring against the words list.

Then, the complexity will be matching concatenation. And there are multiple
duplicate computations.

2. Sliding window

The real problem of brute force combination solution is that it involves lots
duplicate computations. Because substring windows are overlapping! So, it's
tempting to use sliding window technique.

Similar question is minimum window string, where we're dealing with characters
not words.

Find the minimum string containing all of the words, and check the length
equal to total words length.

One problem here is that, when there is a mismatch, how to slide the window?
In another word, what the window SLIDE STRIDE?

Slide the window by one character?
If so, we need to compute words occurrences again, not much improvement.
Can we slide the window by one word?
If so, the word occurrence counts has a state transition recurrence relation.

If we slide it over the current word w, then how about c + w[:3] is in words?
The given words are of same length, so the word length can be thought as a
stride.

The trick is to change the SLIDING WINDOW OFFSET!
Exhaust all offsets in range [0, wordlen - 1], then we can slide the window
confidently since all words have same length!

Complexity: O(n)



'''

from _decorators import timeit

from collections import Counter, defaultdict

class Solution(object):

    @timeit
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # result = self._findSubstringBruteForceCombination(s, words)
        result = self._findSubstringSlidingWindow(s, words)

        print(s[:100], words[:50], result)

        return result

    def _findSubstringBruteForceCombination(self, s, words):
        result = []

        nWords = len(words)
        wordLen = len(words[0]) if words else 0
        totalLen = wordLen * nWords

        counter = Counter(words) # leave it immutable/intact, since we're finding all solutions
        i = 0
        while i + totalLen <= len(s):
            # For each i, determine if s[i:i+totalLen] is valid
            seen = defaultdict(int) # defaultdict is faster than Counter
            for j in range(i, i + totalLen, wordLen):
                word = s[j:j+wordLen]
                if word not in counter: break
                else: seen[word] += 1
                if seen[word] > counter[word]: break
            if counter == seen:
                result.append(i) # match
            i += 1

        return result

    def _findSubstringSlidingWindow(self, s, words):
        if not s or not words or not words[0]:
            return []

        def slideWindow(l, r):
            """
            Slide the window with stride as wordLen, find all valid windows.
            """
            seen = {}
            while r + wordLen <= n:
                w = s[r:r + wordLen]
                r += wordLen # expand the window
                if w not in counter:
                    l = r # skip
                    seen.clear()
                else:
                    seen[w] = seen[w] + 1 if w in seen else 1 # more occurrence, keep removing!
                    while seen[w] > counter[w]:
                        seen[s[l:l + wordLen]] -= 1 # left shrink the window
                        l += wordLen
                    if r - l == totalLen:
                        result.append(l)

        n = len(s)
        wordLen = len(words[0])
        totalLen = len(words) * wordLen
        counter = Counter(words)
        result = []
        for i in range(min(wordLen, n - totalLen + 1)):
            slideWindow(i, i)
        return result

def test():
    solution = Solution()
    assert solution.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",
                                  ["fooo", "barr", "wing", "ding", "wing"]) == [13]
    assert solution.findSubstring(
        "barfoothefoobarman",
        ["foo", "bar"]) == [0, 9]
    assert solution.findSubstring(
        "wordgoodgoodgoodbestword",
        ["word", "good", "best", "good"]) == [8]
    assert solution.findSubstring(
        "aaaaa", ["a","a","a","a","a", "a"]
    ) == []

    assert solution.findSubstring("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab",
["ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba"]) == []

    print('self test passed')

if __name__ == '__main__':
    test()
