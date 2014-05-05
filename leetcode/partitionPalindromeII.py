'''
Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab"
Return

  [ ["aa","b"], ["a","a","b"] ]
  '''


class Solution:
    # @param s,a string
    # @return an integer
    # @apply dynamic programming.mincuts[i] = min(mincuts[i-j])+1
    # @ j is the length of palindrome string ending with s[i]
    def minCut(self,s):
        mincuts = []
        mincuts.append(0)

        #pls = []
        #pls.append([[s[0]]])

        for i in range(1,len(s),1):
            #pls.append([])
            #palins = []
            palins = Solution.getAnchorPalins(s,i,-1)
            mincut =  None
            for palin in palins:
                j = i - len(palin)
                if j >= 0:
                    if mincut == None:
                        mincut = mincuts[j] + 1
                        #for pl in pls[j]:
                        #newPl = list(pl)
                        #newPl.append(palin)
                        #pls[i].append(newPl)
                    else:
                        if mincut > mincuts[j] + 1:
                            mincut = mincuts[j] + 1
                        else:
                            pass

                else:
                    mincut = 0
                    #newPl = [palin]
                    #pls[i].append(newPl)

            mincuts.append(mincut)
            #print mincuts," length is: %d"%len(mincuts)

        #return pls[len(s)-1]
        return mincuts[len(s)-1]

    # @param s,a string
    # @param index,a integer
    # @param step,1 or -1
    # @return a list of  palindrome strings that start
    #   or end with index
    @classmethod
    def getAnchorPalins(cls,s,index,step):
        pl = []
        for i in xrange(index,index + step*len(s),step):
            if index < i:
                if Solution.isPalindrome(s[index:i]):
                    if s[index:i] != "":
                        pl.append(s[index:i])
                    else:
                        pass
                else:
                    pass

            else:
                if Solution.isPalindrome(s[i:index+1]):
                    if s[i:index+1] != "":
                        pl.append(s[i:index+1])
                    else:
                        pass

        return pl

    @classmethod
    def isPalindrome(cls,s):
        n = len(s)
        if n == 0:
            return True
        i = 0
        j = n-1
        for i in range(n):
            #print "i:%d "%i,s[i].lower(),",",s[j].lower()
            if i >= j:
                return True
            if s[i].isalnum():
                while not s[j].isalnum():
                    j = j-1

                if s[i].lower() != s[j].lower():
                    return False
                else:
                    j = j - 1
                    pass

            else:
                pass


if __name__ == "__main__":
    #print Solution().partition("aa")
    #print Solution().partition("aab")
    #print Solution
    #print Solution().getAnchorPalins("aab",2,-1)
    #print Solution().getAnchorPalins("aa",1,-1)
    #s = Solution().partition("aab")
    #print Solution().minCut("aaaaaaaaaaaaaaaaaa")
    print Solution().minCut("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
