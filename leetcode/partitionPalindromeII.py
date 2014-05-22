'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
  '''

'''
Solution:
    @1 Dynamic Programming:
        Use DP to check whether a string is palindromic
        Use DP to decide the min cut of a string by partitioning it,
        with the recurrence similar to the matrix chain order problem

        table[i][j]=
        -1  (initialization)
        0   (palindrome)
        n   (n>0,not palindrome,n is the min cut of palindromic partitioning)

        recurrence:
            1) table[i][j]=(s[i]==s[j] && p[i+1][j-1] == True)
            2) mincuts[i] = min(mincuts[i],mincuts[j-1]+1) if p[i][j] == True
            This is optimized version for :
                mincuts[i][j] = min(mincuts[i][k]+mincuts[k+1][j]+1)
                which reduces the time complexity by n times.


        '''


class Solution:
    # @param s,a string
    # @return an integer

    # @apply dynamic programming.mincuts[i] = min(mincuts[i-j])+1
    # @ j is the length of palindrome string ending with s[i]
    def minCut(self,s):
        import sys
        mincuts = []
        table = Solution.getPalindromes(s)

        for l in xrange(2,len(s) + 1,1):
            for i in xrange(0,len(s) - l + 1,1):
                j = i + l - 1
                if table[i][j] == 0:
                    continue
                else:
                    mincut = l - 1
                    for k in xrange(i,j,1):
                        mincut = min(mincut,table[i][k]+table[k+1][j] + 1)

                    table[i][j] = mincut

            #for i in range(len(s)):
            #print table[i]


        return table[0][len(s)-1]


    @classmethod
    def getPalindromes(cls,s):
        table = [[-1 for x in xrange(len(s))] for x in xrange(len(s))]
        for i in xrange(len(s)):
            table[i][i] = 0

        for i in xrange(len(s) - 1):
            if s[i] == s[i+1]:
                table[i][i+1] = 0

        for l in xrange(3,len(s) + 1):
            for i in xrange(0,len(s)-l + 1):
                j = i + l -1
                if s[i] == s[j] and table[i+1][j-1] == 0:
                    table[i][j] = 0

        return table


if __name__ == "__main__":
    #print Solution().partition("aa")
    #print Solution().partition("aab")
    #print Solution
    #print Solution().getAnchorPalins("aab",2,-1)
    #print Solution().getAnchorPalins("aa",1,-1)
    #s = Solution().partition("aab")
    #print Solution().minCut("aaa")
    #print Solution().minCut("aab")
    #print Solution().minCut("aaaaaaaaaaaaaaaaaa")
    print Solution().minCut("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp")
    #print Solution().minCut("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
