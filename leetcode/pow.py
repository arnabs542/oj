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


class Solution(object):
    # 1.1 using built in pow function
    myPow = pow
    # 1.2
    def myPowBuiltin(self, x, n):
        return x ** n

    # 2 recursive
    def myPowRecursive(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float

        38ms, beats 86.86%, 2016-10-07 10:51
        """
        if not x:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return 1.0 / self.myPowRecursive(x, -n)

        if n % 2 == 1:
            return x * self.myPowRecursive(x, n - 1)
        else:
            # n % 2 == 0
            # XXX: this is actually binary search
            return self.myPowRecursive(x * x, n / 2)

    #3 iterative
    def myPowIterative(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float

        Every number, including n, can be represented by a sum of power of 2. This is the
        concept of binary representation. So the order n can be rewritten, and we have relation
        between x^{2^(k+1)} and x^{2^k} given an integer k:
            x^{2^(k+1)} = x^{2^k * 2} = (x^{2^k})^2
        x ^ n = \prod_{k = 0}^{m-1} x^{a_k 2^k}
        """
        if not x:
            return 0
        if not n:
            return 1
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n:
            if  n & 1:
                result *= x
            x *= x
            n = n >> 1
        return result


    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float

        pow(0, 0) == 1?
        """
        # return self.myPowRecursive(x, n)
        return self.myPowIterative(x, n)
        pass



def test():
    print(Solution().myPow(-4, -1))
    print(Solution().myPow(3, 3))

if __name__ == "__main__":
    test()
