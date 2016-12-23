'''
Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x.

==============================================================================================
Solution:

1. Binary search for k ,for which k² <= x < (k + 1)².
2. Newton's method (root/zeros finding method for real-valued function).
Find square root of a number `a` is to find the root for function:
    f(x) = x² - a = 0
and:
    f'(x) = 2 * x
The iterative update:
    x[n + 1] = x[n] - f(x[n]) / f'(x[n])
             = x[n] - ½ * (x[n] - a/x[n])
             = (x[n] + a / x[n]) / 2
The vanilla stopping criterion is:
    (x[n + 1] - x[n]) <= 1
But for this problem, we want find root² <= x <= (root + 1)²
'''

class Solution(object):

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # return self.mySqrtBS(x)
        return self.mySqrtNewton(x)

    def mySqrtBS(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            root = (low + high) // 2
            if root * root > x:
                high = root - 1
            elif (root + 1) ** 2 <= x:
                low = root + 1
            else:
                return root
        # return k

    def mySqrtNewton(self, x: int) -> int:
        root = x
        while root * root > x:
            root = (root + x // root) // 2
        print(root)
        return root

def test():
    solution = Solution()
    # assert solution.mySqrt(0) == 0
    assert solution.mySqrt(1) == 1
    assert Solution().mySqrt(9) == 3
    assert Solution().mySqrt(19) == 4
    assert Solution().mySqrt(26) == 5

    print('self test passed')

if __name__ == "__main__":
    test()
