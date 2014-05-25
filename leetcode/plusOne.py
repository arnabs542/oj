'''
Plus One
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.


'''

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        s = digits[len(digits)-1] + 1
        carry = s / 10
        remainder = s % 10
        digits[len(digits)-1] = remainder
        for i in xrange(len(digits) - 2,-1,-1):
            s = digits[i] + carry
            digits[i] = s%10
            carry = s/10

        if carry > 0:
            digits.insert(0,carry)

        return digits

if __name__ == "__main__":
    print Solution().plusOne([9,9,9,9,9])
