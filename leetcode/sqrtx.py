#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x.


================================================================================
Solution

This is a root-finding problem.

1. Binary search(bisect)

1) Binary search for k ,for which k² <= x < (k + 1)².
2) Binary search for lower bound.

2. Newton's method (root/zeros finding method for real-valued function).

Iteration update:
x_{n+1} = x_n - f(x_n)/f'(x_n)

Geometrically, (x_{n+1}, 0) is the intersection of the x-axis and the tangent of the graph
of f at (x_n, f (x_n)).

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
        # result = self._mySqrtBinarySearch(x)
        result = self._mySqrtBinarySearchBound(x)
        # result = self._mySqrtNewton(x)

        print("square root: ", x, result)

        return result

    def _mySqrtBinarySearch(self, x: int) -> int:
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

    def _mySqrtBinarySearchBound(self, x: int) -> int:
        """
        Binary search for bound: lower bound or upper bound
        """
        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            root = mid ** 2
            if root > x:
                high = mid - 1
            elif root < x:
                low = mid + 1
            else:
                return mid
        return high # high = low - 1, indicating low**2 > x > high**2, return high

    def _mySqrtNewton(self, x: int) -> int:
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
    assert Solution().mySqrt(50) == 7
    assert Solution().mySqrt(100) == 10

    print('self test passed')

if __name__ == "__main__":
    test()
