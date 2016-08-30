'''
Longest Palindrome Substring
Given a string S,find longest palindromic substring in S.You may assume that
the maximum length of S is 1000,and there exists one unique longest palindromic
substring
'''

'''
Solution:
    @1 brute-force.Time complexiyy: O(n^3)
    @2 dynamic programming.Time: O(n^2),space: O(n^2)
    Notation: table[i][j] == 1: s[i:j+1] is palindrome,0: not

        Recurrence:
            table[i][i] = 1
            table[i][j] = 1 => table[i+1][j-1] == 1 && s[i] == s[j]
            @3 Simple method:check from center to
            @4 Manacher's algorithm

    '''


class Solution:
    # @return a string

    def longestPalindrome(self, s):
        table = []

        # time complexity
        # for i in range(len(s)):
        # table.append([])
        # for j in range(len(s)):
        # if i == j :
        # table[i].append(1)
        # else:
        # table[i].append(0)

        # optimization for two dimensional array initialization
        table = [[0 for x in range(len(s))] for x in range(len(s))]

        longestPalin = ""
        begin = end = 0

        for i in range(len(s)):
            table[i][i] = 1

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                table[i][i + 1] = 1
                begin = i
                end = i + 1
                # longestPalin = s[i:i+2]

        for l in range(3, len(s) + 1, 1):
            for i in range(len(s) - l + 1):
                # table[i][j] = 0
                j = i + l - 1
                if s[i] == s[j]:
                    if s[i + 1] == s[j - 1] and table[i + 1][j - 1] == 1:
                        table[i][j] = 1
                        # optimization to reduce time complexity constant
                        begin = i
                        end = j + 1
                        # longestPalin = s[i:j+1]

                # if table[i][j] == 1:
                # print i,j
                # longestPalin = s[i:j+1]

        # for i in range(len(s)):
        # print table[i]

        longestPalin = s[begin:end]

        return longestPalin


if __name__ == "__main__":
    print(Solution().longestPalindrome("ukxidnpsdfwieixhjnannbmtppviyppjgbsludrzdleeiydzawnfmiiztsjqqqnthwinsqnrhfjxtklvbozkaeetmblqbxbugxycrlzizthtuwxlmgfjokhqjyukrftvfwikxlptydybmmzdhworzlaeztwsjyqnshggxdsjrzazphugckgykzhqkdrleaueuajjdpgagwtueoyybzanrvrgevolwssvqimgzpkxehnunycmlnetfaflhusauopyizbcpntywntadciopanyjoamoyexaxulzrktneytynmheigspgyhkelxgwplizyszcwdixzgxzgxiawstbnpjezxinyowmqsysazgwxpthloegxvezsxcvorzquzdtfcvckjpewowazuaynfpxsxrihsfswrmuvluwbdazmcealapulnahgdxxycizeqelesvshkgpavihywwlhdfopmmbwegibxhluantulnccqieyrbjjqtlgkpfezpxmlwpyohdyftzgbeoioquxpnrwrgzlhtlgyfwxtqcgkzcuuwagmlvgiwrhnredtulxudrmepbunyamssrfwyvgabbcfzzjayccvvwxzbfgeglqmuogqmhkjebehtwnmxotjwjszvrvpfpafwomlyqsgnysydfdlbbltlwugtapwgfnsiqxcnmdlrxoodkhaaaiioqglgeyuxqefdxbqbgbltrxcnihfwnzevvtkkvtejtecqyhqwjnnwfrzptzhdnmvsjnnsnixovnotugpzuymkjplctzqbfkdbeinvtgdpcbvzrmxdqthgorpaimpsaenmnyuyoqjqqrtcwiejutafyqmfauufwripmpcoknzyphratopyuadgsfrsrqkfwkdlvuzyepsiolpxkbijqw"))
    pass
