'''
415. Add Strings

Total Accepted: 6067
Total Submissions: 14337
Difficulty: Easy
Contributors: Admin

Given two non-negative numbers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i, j = len(num1) - 1, len(num2) - 1
        num3 = ''
        carry = 0
        while i >= 0 or j >= 0:
            d1 = int(num1[i]) if i >= 0 else 0
            d2 = int(num2[j]) if j >= 0 else 0
            carry, s = divmod(d1 + d2 + carry, 10)
            num3 = str(s) + num3
            i -= 1
            j -= 1

        if carry:
            num3 = str(carry) + num3
        print(num3)
        return num3

def test():
    solution = Solution()
    assert solution.addStrings('0', '0') == '0'
    assert solution.addStrings('1234', '5678') == '6912'
    assert solution.addStrings('1234', '9678') == '10912'
    assert solution.addStrings('923', '8') == '931'
    print('self test passed')

if __name__ == '__main__':
    test()


