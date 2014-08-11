'''
Pow(x,n)
    Implement pow(x,n)
'''

'''
Solution:
    Naive method:
        Simply multiply x n times
    O(logN) method:
        Binary method
'''


class Solution:
    # @param x,a float
    # @param n,a integer
    # @return a float

    def pow(self, x, n):
        pn = abs(n)  # positive n
        if x == 0:
            return 0
        if pn == 0:
            return 1
        k = 1
        result = x
        while 2 * k < pn:
            result *= result
            k *= 2

        remainder = pn - k
        remains = pow(x, remainder)

        result *= remains
        if n < 0:
            return 1.0 / result
        else:
            return result

if __name__ == "__main__":
    print Solution().pow(-4, -1)
