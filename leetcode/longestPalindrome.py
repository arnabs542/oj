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

    '''

class Solution:
    # @return a string
    def longestPalindrome(self,s):
        table = []
        for i in range(len(s)):
            table.append([])
            for j in range(len(s)):
                if i == j :
                    table[i].append(1)
                else:
                    table[i].append(0)

        longestPalin = ""

        for l in range(2,len(s) + 1,1):
            for i in range(len(s) - l + 1):
                #table[i][j] = 0
                j = i + l -1
                if s[i] == s[j] :
                    if i + 1 <= j - 1:
                        if s[i+1] == s[j-1] and table[i+1][j-1] == 1:
                            table[i][j] = 1
                        else:
                            pass

                    else:
                        table[i][j] = 1

                if table[i][j] == 1:
                    print i,j
                    longestPalin = s[i:j+1]

        #for i in range(len(s)):
        #print table[i]

        return longestPalin


if __name__ == "__main__":
    print Solution().longestPalindrome("abcdefgfedcbag")
    pass



