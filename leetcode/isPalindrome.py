'''
Valid Palindrome

Given a string, determine if it is a palindrome, considering only
alnumnumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
    Have you consider that the string might be empty?
    This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''


class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
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

if __name__=="__main__":
    print Solution().isPalindrome("A man, a plan, a canal: Panama")
    print Solution().isPalindrome("race a car")
    print Solution().isPalindrome("")
    print Solution().isPalindrome("1a2")
