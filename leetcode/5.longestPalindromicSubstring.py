#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
5. Longest Palindromic Substring

Total Accepted: 161701
Total Submissions: 660420
Difficulty: Medium
Contributors: Admin

Given a string s, find the longest palindromic substring in s. You may assume that
the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"

==============================================================================================
SOLUTION

1. Brute-force.

Exhaust all cases and verify.

Time complexity: O(n^3)

2. Dynamic programming

Define state: dp[i][j].
dp[i][j] == 1: s[i:j+1] is palindrome. 0: s[i:j+1] is not palindrome.

Recurrence relation:
    dp[i][i] = 1
    dp[i][j] = 1 <=> dp[i+1][j-1] == 1 && s[i] == s[j]

Complexity
Time: O(N²), space: O(N²)

3. Two pointers: check by scanning from center to two sides

Perform a “center expansion” among all possible centers of the palindrome.

Let N = len(S). There are 2N-1 possible centers for the palindrome:
  we could have a center at S[0], between S[0] and S[1], at S[1], between S[1] and S[2], at S[2], etc.

To iterate over each of the 2N-1 centers, we will move the left pointer every 2 times, and the right pointer every 2 times starting with the second (index 1).
After writing some case, it's easy to derive the left and right indices formula.
Hence, left = center / 2 - (center + 1)%2, right = center / 2 + 1.

From here, finding every palindrome starting with that center is straightforward: while the ends are valid and have equal characters, record the answer and expand.

Complexity: O(N²), O(1)

4. Manacher's algorithm

I have no idea...

5. Suffix array?

Complexity: O(nlogn)?

'''

from _decorators import timeit

class Solution(object):

    @timeit
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # result = self._longestPalindromeDP(s)
        # result = self._longestPalindromeDPOpt(s)
        result = self._longestPalindromeCenterExpand(s)
        print(result)

        return result

    def _longestPalindromeDP(self, s):
        # if not s: return ''

        # TODO: this is a O(N²) solution, always Time limit exceed with Python

        # optimization for two dimensional array initialization
        n = len(s)
        dp = [[1  if i == j or i + 1 == j and s[i] == s[j] else 0
               for j in range(n)] for i in range(n)]

        # initialization
        begin, end = 0, min(1, len(s))

        # state transition
        for l in range(2, n + 1, 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] == s[j] and (l == 2 or dp[i + 1][j - 1]):
                    dp[i][j] = 1
                    # optimization to reduce time complexity constant
                    begin = i
                    end = j + 1

        return s[begin:end]

    def _longestPalindromeDPOpt(self, s):
        '''
        Just using builtin string compare!

        When you increase s by 1 character, you could only increase
        maxPalindromeLen by 2 at most, and that new maxPalindrome includes this
        new character.

        Proof: if on adding 1 character, maxPalindromeLen increased by 3 or
        more, say the new maxPalindromeLen is Q, and the old maxPalindromeLen
        is P, then Q>=P+3. Then it would mean, even without this new character,
        there would be a palindromic substring ending in the last character,
        whose length is at least Q-2. Since Q-2 would be >P, this contradicts
        the condition that P is the maxPalindromeLen without the additional
        character.

        Scan from beginning to the end, adding one character at a time, keeping
        track of maxPalindromeLen, and for each added character, you check if
        the substrings ending with this new character, with length P+1 or P+2,
        are palindromes, and update accordingly.

        Optimization  utilizing built in string compare implementation
        '''
        if s == s[::-1]:
            return s
        maxlen = 1
        start = 0
        for i in range(1, len(s)):
            increment = 2
            start_new = i - (maxlen + increment - 1)
            if start_new >= 0 and \
               s[start_new:i + 1] == s[start_new:i + 1][::-1]:
                maxlen += increment
                start = start_new
            else:
                increment = 1
                start_new = i - (maxlen + increment - 1)
                if start_new >= 0 and s[start_new:i + 1] == s[start_new:i + 1][::-1]:
                    maxlen += increment
                    start = start_new

        return s[start:start + maxlen]

    # DONE: expand around the center, O(N²)
    def _longestPalindromeCenterExpand(self, s):
        n = len(s) # 2, "aa"
        result = ""
        for center in range(2 * n - 1): # 1
            d, r = divmod(center, 2) # 0, 1
            right = (center // 2) + 1 # 1
            left = (right - 1) if r else right - 2 # 0
            l = not r # 0
            while 0 <= left < right < n and s[left] == s[right]:
                l += 2 # 2
                left -= 1 # -1
                right += 1 # 2
            if l > len(result):
                result = s[left + 1:right] # s[0:2]
        return result

    # TODO: Manacher's linear time complexity solution, O(n)

    # TODO: SUFFIX ARRAY implementation, O(n*logn)


def test():
    solution = Solution()
    assert (solution.longestPalindrome("") == "")
    assert (solution.longestPalindrome("a") == "a")
    assert solution.longestPalindrome("aa") == "aa"
    assert solution.longestPalindrome("ccd") == "cc"
    assert solution.longestPalindrome("cbbd") in ["bb", ]
    assert (solution.longestPalindrome("abb") == "bb")
    assert (solution.longestPalindrome("ukxidnpsdfwieixhjnannbmtppviyppjgbsludrzdleeiydzawnfmiiztsjqqqnthwinsqnrhfjxtklvbozkaeetmblqbxbugxycrlzizthtuwxlmgfjokhqjyukrftvfwikxlptydybmmzdhworzlaeztwsjyqnshggxdsjrzazphugckgykzhqkdrleaueuajjdpgagwtueoyybzanrvrgevolwssvqimgzpkxehnunycmlnetfaflhusauopyizbcpntywntadciopanyjoamoyexaxulzrktneytynmheigspgyhkelxgwplizyszcwdixzgxzgxiawstbnpjezxinyowmqsysazgwxpthloegxvezsxcvorzquzdtfcvckjpewowazuaynfpxsxrihsfswrmuvluwbdazmcealapulnahgdxxycizeqelesvshkgpavihywwlhdfopmmbwegibxhluantulnccqieyrbjjqtlgkpfezpxmlwpyohdyftzgbeoioquxpnrwrgzlhtlgyfwxtqcgkzcuuwagmlvgiwrhnredtulxudrmepbunyamssrfwyvgabbcfzzjayccvvwxzbfgeglqmuogqmhkjebehtwnmxotjwjszvrvpfpafwomlyqsgnysydfdlbbltlwugtapwgfnsiqxcnmdlrxoodkhaaaiioqglgeyuxqefdxbqbgbltrxcnihfwnzevvtkkvtejtecqyhqwjnnwfrzptzhdnmvsjnnsnixovnotugpzuymkjplctzqbfkdbeinvtgdpcbvzrmxdqthgorpaimpsaenmnyuyoqjqqrtcwiejutafyqmfauufwripmpcoknzyphratopyuadgsfrsrqkfwkdlvuzyepsiolpxkbijqw") == "aueua")

    import yaml
    with open("./longestPalindromicSubstring.json", "r") as f:
        data = yaml.load(f)

    for r in data:
        assert solution.longestPalindrome(r['input']) == r['output']


    print("self test passed!")


if __name__ == "__main__":
    test()
