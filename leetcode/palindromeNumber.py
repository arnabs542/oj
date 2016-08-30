'''
Palindrome Number
Determine whether an integer is a palindrome. Do this without extra space.
Some hints:
    Could negative integers be palindromes? (ie, -1)

    If you are thinking of converting the integer to string, note the restriction of using extra space.

    You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

    There is a more generic way of solving this problem.
    '''

class Solution:
    # @return a boolean
    def isPalindrome(self,x):
        if x < 0:
            return False
        div = 1
        while x/div >= 10:
            div *= 10

        while x > 0:
            r = x % 10
            l = x / div
            if r != l:
                return False

            x = (x % div) / 10
            div /= 100

        if x == 0:
            return True


if __name__ == "__main__":
    print(Solution().isPalindrome(1001))
