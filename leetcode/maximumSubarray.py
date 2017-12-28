#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
53. Maximum Subarray

Total Accepted: 147195
Total Submissions: 384375
Difficulty: Medium
Contributors: Admin

Find the contiguous subarray within an array (containing at least one number) which
has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide
and conquer approach, which is more subtle.

===============================================================================================
SOLUTION

1) Brute force

Complexity: O(N³) or O(N²) if calculating sum incrementally.

2) Dynamic Programming.

A subarray window must end somewhere, assuming position i.
Kadane's algorithm begins with a simple INDUCTIVE question:
  If we know the maximum subarray sum ENDING AT POSITION i, what is the maximum subarray
sum ending at position  i+1? The answer turns out to be relatively straightforward:
either the maximum subarray sum ending at position  i+1 includes the maximum subarray sum
ending at position i as a prefix, or it doesn't. Thus, we can compute the maximum subarray
sum ending at position  i for all positions i by iterating once over the array. As we go,
we simply keep track of the maximum sum we've ever seen.

DEFINE STATE:
    max_ending_here: Maximum subarray sum ending at position i.

STATE TRANSITION:
    Scan through the array values, computing at each position the MAXIMUM (positive sum)
subarray ENDING AT THAT POSITION.
    This CURRENT subarray is either empty (in which case its sum is zero) or consists of one
more element(current element) than the maximum subarray ENDING AT THE PREVIOUS position. (If
no empty subarray is allowed, current subarray consists of either one element or one more
element than the previous maximum subarray.)

Use max_ending_here to denote the SUM OF MAXIMUM SUBARRAY ENDING AT EACH POSITION, then
max_ending_here = max(max_ending_here + nums[i], nums[i])

Time Complexity:
The runtime complexity of Kadane's algorithm is O(n).

Generalization:
    The algorithm can also be easily modified to keep track of the starting and ending(
two pointers) indices of the maximum subarray.

Because of the way this algorithm uses optimal substructures (the MAXIMUM SUBARRAY ENDING
AT EACH POSITION is calculated in a simple way from a related but smaller and overlapping
subproblem: the maximum subarray ending at the previous position) this algorithm can be
viewed as a simple example of DYNAMIC PROGRAMMING.

3) Prefix sum
Subarray sum is range sum query. Prefix sum can be used to compute range sum efficiently.

Calculate the cumulative sum(prefix sum) in a bottom up fashion, then, keep track of the
minimum sum so far.


##############################################################################################
VARIANT

红绿灯数目问题
Q: 给出一个Char Array, 里面只有 R, G. 现在要选择一个范围，使得 R 变成G，G变成R，并使得G的个数－ R的个数最大。输出这个范围并且输出最大结果.

==============================================================================================
SOLUTION

Maximum subarray problem -  COUNTING AS SUMMING

要求的的是一个范围，就是一个subarray。这个subarray的#R - #G 要足够大。

如果令:
R = 1,
G = 0,
那么这个subarray需要满足的条件就是： maximum sum of elements within range.


然后，用DP一遍就可以解决了


'''

class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self._maxSubArrayDP(nums)

    def _maxSubArrayDP(self, nums: list) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = max_ending_here = nums[0]
        for i in range(1, len(nums)):
            max_ending_here = max(nums[i], max_ending_here + nums[i])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    def _maxSubArrayDPAllowZeroLength(self, nums: list) -> int:
        """
        :type nums: List[int]
        :rtype: int

        Allowing zero-length subarray
        """
        max_so_far = max_ending_here = 0
        for i, _ in enumerate(nums):
            max_ending_here = max(0, max_ending_here + nums[i])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    def _maxSubArrayDP2(self, nums: list) -> list:
        """
        :type nums: List[int]
        :rtype: list

        Keep track of two pointers: starting and ending indices of the maximum subarray.
        Returning the corresponding subarray.
        """
        n = len(nums)
        max_so_far, max_ending_here = nums[0], nums[0]
        i, begin, end = 0, 0, 1
        for j in range(1, n):
            if max_ending_here <= 0:
                i = j
                max_ending_here = nums[j]
            else:
                max_ending_here += nums[j]

            if max_ending_here >= max_so_far:
                begin = i
                end = j + 1
                max_so_far = max_ending_here

        print('maximum subarray', nums[begin:end])
        return nums[begin:end]

      def _maxSubArrayPrefixSum(self, nums: list) -> int:
          # TODO: prefix sum solution
          pass

    # TODO: divide and conquer solution

def test():
    solution = Solution()

    assert solution.maxSubArray([1]) == 1
    assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    assert solution.maxSubArrayDP2([1]) == [1]
    assert solution.maxSubArrayDP2(
        [-2, 1, -3, 4, -1, 2, 1, -5, 4]) == [4, -1, 2, 1]

    print('self test passed')

if __name__ == '__main__':
    test()
