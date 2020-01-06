#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
477. Total Hamming Distance

Total Accepted: 7479
Total Submissions: 16326
Difficulty: Medium
Contributors: kevin.xinzhao@gmail.com

The Hamming distance between two integers is the number of positions at which the
corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
    HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

Note:
Elements of the given array are in the range of 0 to 10^9
Length of the array will not exceed 10^4.

==============================================================================================
SOLUTION

1. Brute-force. Compute pairwise distance metrics for O(N²) pairs, time complexity is O(N²).

2.

Denote the distance metric function as f(x, y). Then analyze:

4  = 0100
14 = 1110
2  = 0010

f(4, 14) = 2, f(4, 2) = 2, f(14, 2) = 2
And we have (a ^ b) ^ (a ^ c) = b ^ c

4  = 0100
10 = 1010
5  = 0101
f(4, 10) = 3, f(4, 5) = 1, f(10, 5) = 4, Total = 3 + 1 + 4 = 8

The above calculation is performed in a perspective of pairs.

If we exploit the array in a bitwise way, we can come up with that, for a specific bit,
the total hamming distance is #(numbers with this bit of 1) * #(numbers with this bit of 0).

In this bit-wise approach, we can do this in O(N * #(integer bits)) = O(N).


  10100111001
1110010100011

'''

class Solution(object):

    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = self.totalHammingDistanceBitwise(nums)
        print(count)
        return count

    def totalHammingDistanceBitwise(self, nums):
        count = 0
        mask = 1
        # XXX: log2(10^9) = 29.897, not 10
        for i in range(30):
            c0 = c1 = 0
            for n in nums:
                c1 += (n & mask) >> i
            c0 = len(nums) - c1
            count += c0 * c1

            mask <<= 1
        return count

def test():
    solution = Solution()

    assert solution.totalHammingDistance([4, 14, 2]) == 6
    assert solution.totalHammingDistance([4, 10, 5]) == 8
    # assert solution.totalHammingDistance([-1, 2, 3]) == 60
    assert solution.totalHammingDistance([0b10100111001, 0b1110010100011]) == 7
    assert solution.totalHammingDistance([1337, 7331]) == 7

    print("self test passed")

if __name__ == '__main__':
    test()
