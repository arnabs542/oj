'''
9. Palindrome Number

Total Accepted: 189955
Total Submissions: 553509
Difficulty: Easy
Contributors: Admin

Determine whether an integer is a palindrome. Do this without extra space.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra
space.

You could also try reversing an integer. However, if you have solved the problem "Reverse
Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

==============================================================================================
SOLUTION

1. Naive
Convert the integer into string.
Complexity: O(logn), O(n)

2. Two pointers
Use division arithmetic to compare digit by digit.

Complexity: O(logn), O(1)

3. Reverse part of it to avoid overflow

Complexity: O(logn), O(1)

Particularly, we can reverse half of it. And finding the half can be achieved with
fast and slow pointers in cycle detection algorithm.

'''

class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # return self.isPalindromeTwoPointers(x)
        return self.isPalindromeReverseHalf(x)

    def isPalindromeTwoPointers(self, x):
        if x < 0:
            return False
        div = 1  # divisor to keep track of the leftmost digit
        while x // div >= 10:
            div *= 10

        while x > 0:
            l = x // div
            r = x % 10
            if r != l:
                return False

            x = (x % div) // 10
            div //= 100

        if x == 0:
            return True

    def isPalindromeReverseHalf(self, x):
        # DONE: reverse half of the integer
        if x and x % 10 == 0:
            return False
        left, right = x, 0
        while left > right:
            left, right = left // 10, right * 10 + left % 10
        return left == right or left == right // 10

def test():
    solution = Solution()

    assert not solution.isPalindrome(-1)
    assert not solution.isPalindrome(-12321)
    assert not solution.isPalindrome(10)
    assert solution.isPalindrome(0)
    assert solution.isPalindrome(1001)
    assert solution.isPalindrome(10101)
    assert solution.isPalindrome(1)
    assert solution.isPalindrome(12321)
    assert solution.isPalindrome(1221)
    assert not solution.isPalindrome(12213)

    print('self test passed')

if __name__ == "__main__":
    test()
