'''
166. Fraction to Recurring Decimal

Total Accepted: 39921
Total Submissions: 243698
Difficulty: Medium
Contributors: Admin

Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
'''

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        quotients = []
        remainders = []

        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)

        # retrieve the integer part, harnessing the built-in division arithmetic
        quotient, remainder = divmod(abs(numerator), abs(denominator))
        quotients.append(str(quotient) + '.')

        # deal with remainders
        while remainder and remainder not in remainders:
            remainders.append(remainder)
            quotient, remainder = divmod(remainder * 10, denominator)
            quotients.append(str(quotient))

        # print(remainders)
        if remainder:
            i = remainders.index(remainder) + 1
            quotients.insert(i, '(')
            quotients.append(')')

        result = sign + ''.join(quotients).rstrip('.')
        print(result)

        return result

def test():
    solution = Solution()
    assert solution.fractionToDecimal(0, 3) == '0'
    assert solution.fractionToDecimal(-50, 8) == '-6.25'
    assert solution.fractionToDecimal(1, 2) == '0.5'
    assert solution.fractionToDecimal(2, 2) == '1'
    assert solution.fractionToDecimal(2, 3) == '0.(6)'
    assert solution.fractionToDecimal(4, 7) == '0.(571428)'
    assert solution.fractionToDecimal(4, 70) == '0.0(571428)'
    assert solution.fractionToDecimal(7, 12) == '0.58(3)'
    assert solution.fractionToDecimal(7, -12) == '-0.58(3)'
    assert solution.fractionToDecimal(22, 7) == '3.(142857)'
    assert solution.fractionToDecimal(-22, -2) == '11'
    print('self test passed')

if __name__ == '__main__':
    test()
