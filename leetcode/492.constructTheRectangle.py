#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
492. Construct the Rectangle

For a web developer, it is very important to know how to design a web page's size. So,
given a specific rectangular web page’s area, your job by now is to design a rectangular
web page, whose length L and width W satisfy the following requirements:

1. The area of the rectangular web page you designed must equal to the given target area.

2. The width W should not be larger than the length L, which means L >= W.

3. The difference between length L and width W should be as small as possible.

You need to output the length L and the width W of the web page you designed in sequence.

Example:
Input: 4
Output: [2, 2]

Explanation:
The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1].
But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is
not optimal compared to [2,2]. So the length L is 2, and the width W is 2.

Note:
The given area won't exceed 10,000,000 and is a positive integer
The web page's width and length you designed must be positive integers.

==============================================================================================
SOLUTION


1. Brute force

Enumerate from 1 to ceil(sqrt(area)).

Complexity: O(n), O(1)

2. Math solution?

'''

import math

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        result = self._constructRectangleBruteForce(area)
        print(result)
        return result

    def _constructRectangleBruteForce(self, area):
        if area == 0:
            return [0, 0]
        root = int(math.floor(math.sqrt(area))) # for python 2, need int() ?
        l, w = 0, 0
        for i in range(1, root + 1):
            if  area % i == 0:
                w = i
                l = area // i
        return [l, w]

def test():
    solution = Solution()

    assert solution.constructRectangle(0) == [0, 0]
    assert solution.constructRectangle(1) == [1, 1]
    assert solution.constructRectangle(2) == [2, 1]
    assert solution.constructRectangle(3) == [3, 1]
    assert solution.constructRectangle(4) == [2, 2]
    assert solution.constructRectangle(5) == [5, 1]
    assert solution.constructRectangle(6) == [3, 2]
    assert solution.constructRectangle(7) == [7, 1]
    assert solution.constructRectangle(8) == [4, 2]
    assert solution.constructRectangle(9) == [3, 3]
    assert solution.constructRectangle(3456) == [64, 54]
    assert solution.constructRectangle(6666) == [101, 66]

    print("self test passed")

if __name__ == '__main__':
    test()
