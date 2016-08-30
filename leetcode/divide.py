# -*- coding:utf-8 -*-

'''

Divide two integers without using multiplication,division and mod operator

SOLUTION:
    division(multiplication) by 2 can be implemented by right(left)
    shifting by 1.

    Any number can be represented 2's power.

'''


class Solution:
    # @return an integer

    def divide(self, dividend, divisor):
        quotient = 0
        a = abs(dividend)
        order = 0
        b = abs(divisor)
        c = b
        sign = (dividend < 0) ^ (divisor < 0)
        # print "sign is :{}".format(sign)
        while a >= b:
            order = 0
            c = b
            while (c << 1) <= a:
                order += 1
                c = c << 1
            a -= c
            quotient += 1 << order

        if sign > 0:
            return -quotient
        else:
            return quotient

if __name__ == "__main__":
    print(Solution().divide(4, -2))
    print(Solution().divide(2147483647, 1))
    print(Solution().divide(4, 3))
    print(Solution().divide(34359738368, 1))
    print(Solution().divide(-1010369383, -2147483648))
