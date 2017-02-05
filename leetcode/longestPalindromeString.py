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

@1 brute-force.Time complexiyy: O(n^3)
@2 dynamic programming.Time: O(N²),space: O(N²)
Notation: table[i][j] == 1: s[i:j+1] is palindrome,0: not

    Recurrence:
        table[i][i] = 1
        table[i][j] = 1 <=> table[i+1][j-1] == 1 && s[i] == s[j]
@3 Two pointers: check by scanning from center to two sides
@4 Manacher's algorithm

'''

class Solution(object):
    def longestPalindromeDP(self, s):
        if not s:
            return ''
        n = len(s)

        # TODO: this is a O(N²) solution, always Time limit exceed with Python

        # optimization for two dimensional array initialization
        longestPalin = ""
        table = [[0 for _ in range(n)] for x in range(n)]

        # initialization
        table[n - 1][n - 1] = 1
        begin, end = 0, 1
        for i in range(n):
            table[i][i] = 1
            begin, end = i, i + 1

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                table[i][i + 1] = 1
                begin, end = i, i + 2

        # state transition
        for l in range(3, n + 1, 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] == s[j] and s[i + 1] == s[j - 1] and\
                   table[i + 1][j - 1]:
                    table[i][j] = 1
                    # optimization to reduce time complexity constant
                    begin = i
                    end = j + 1

        longestPalin = s[begin:end]

        return longestPalin

    def longestPalindromeDPOpt(self, s):
        '''
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

        Optimized  utilizing built in string compare implementation
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

    # TODO: expand around the center, O(N²)

    # TODO: Manacher's linear time complexity solution, O(n)

    # TODO: SUFFIX ARRAY implementation, O(n*logn)

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return self.longestPalindromeDP(s)
        return self.longestPalindromeDPOpt(s)

def test():
    solution = Solution()
    print(solution.longestPalindrome(""))
    print(solution.longestPalindrome("a"))
    print(solution.longestPalindrome("aa"))
    print(solution.longestPalindrome("ccd"))
    print(solution.longestPalindrome("abb"))
    print(solution.longestPalindrome("ukxidnpsdfwieixhjnannbmtppviyppjgbsludrzdleeiydzawnfmiiztsjqqqnthwinsqnrhfjxtklvbozkaeetmblqbxbugxycrlzizthtuwxlmgfjokhqjyukrftvfwikxlptydybmmzdhworzlaeztwsjyqnshggxdsjrzazphugckgykzhqkdrleaueuajjdpgagwtueoyybzanrvrgevolwssvqimgzpkxehnunycmlnetfaflhusauopyizbcpntywntadciopanyjoamoyexaxulzrktneytynmheigspgyhkelxgwplizyszcwdixzgxzgxiawstbnpjezxinyowmqsysazgwxpthloegxvezsxcvorzquzdtfcvckjpewowazuaynfpxsxrihsfswrmuvluwbdazmcealapulnahgdxxycizeqelesvshkgpavihywwlhdfopmmbwegibxhluantulnccqieyrbjjqtlgkpfezpxmlwpyohdyftzgbeoioquxpnrwrgzlhtlgyfwxtqcgkzcuuwagmlvgiwrhnredtulxudrmepbunyamssrfwyvgabbcfzzjayccvvwxzbfgeglqmuogqmhkjebehtwnmxotjwjszvrvpfpafwomlyqsgnysydfdlbbltlwugtapwgfnsiqxcnmdlrxoodkhaaaiioqglgeyuxqefdxbqbgbltrxcnihfwnzevvtkkvtejtecqyhqwjnnwfrzptzhdnmvsjnnsnixovnotugpzuymkjplctzqbfkdbeinvtgdpcbvzrmxdqthgorpaimpsaenmnyuyoqjqqrtcwiejutafyqmfauufwripmpcoknzyphratopyuadgsfrsrqkfwkdlvuzyepsiolpxkbijqw"))


if __name__ == "__main__":
    test()
