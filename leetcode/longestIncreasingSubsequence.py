#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
300. Longest Increasing Subsequence

Total Accepted: 56604
Total Submissions: 152709
Difficulty: Medium
Contributors: Admin

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note
that there may be more than one LIS combination, it is only necessary for you to return
the length.

Your algorithm should run in O(n²) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

==============================================================================================
SOLUTION:

1. Brute-force
If we maintain all LIS subset, then we can literally find all LIS, and take the longest one.
Time complexity: O(exponential).

2. Dynamic Programming
The brute force solution involves lots of duplicate computation, which can be addressed
utilizing the recurrence relation/state transition function.

In a TYPICAL SUBSEQUENCE PROBLEM, a general approach to construct the recurrence relation
is to define such STATE f such that f(i) indicates a quantity of a subsequence ENDING HERE,
at ith index.

----------------------------------------------------------------------------------------------
In a perspective of LIS length, define state:
    f(i) = length of longest increasing subsequence ending here.
Then, we have:
f(i) = max(f(j) + 1), where nums[i] > nums[j], j = 1, ..., i - 1.

Time complexity: O(N²).

3. Logarithmic optimization keeping track of tail element of increasing sequence.

The number of subsequences is the number of subsets, which is exponential. It helps to
eliminate some unnecessary candidates.

Lemma 1:
    Regard to the set of increasing sequences, assume two subsequences, say s1, s2, share
same length, and s1[-1] < s2[-1]. Then, any number that extends s2 extends s1 too. In
other words, the set of numbers that extend s2 is a subset of the set of s1.

Proof:
    S1 = {a|a extends s1}, S2 = {a| a extends s2}
    ∀a ∈ s2, ∃ relation s1[-1] < s2[-1] < a. In this sense, a ∈ s1. So S2 ⊂ S1.

Then, to extend to potential larger from current ones, the s1 would have more chances.
It's safe to eliminate s2 now to reduce complexity.

Define the state[i] as the smallest tail element for all increasing subsequences.

Lemma 2:
    Smallest end element array is monotonic increasing.

Proof by contradiction.:
    Given two increasing subsequence s1 and s2, and len(s1) + 1 = len(s2), assume
sl[-1] + 1 = s2[-1].
    Then we have s2[-1] > s2[-2], by increasing sequence's property.
So s1[-1] > s2[-1] > s2[-1]. Because len(s2[:-1]) = len(s2) - 1 = len(s1). Then the
smallest end element of increasing sequence of length len(s1) is s2[-2], which is smaller
than s1[-1]. Apparently, this is contradiction to the definition.
    So the assumption won't hold!

----------------------------------------------------------------------------------------------
Algorithm:
Iterate the list, when a new element shows up, there are only two scenarios:
1) current element extend some LIS by appending it to the end of the sequence
2) current element could be a potential head of LIS
3) current element make the end element of a LIS smaller by taking its place.
Actually, 2) and 3) are the same.

But we only care about the LIS length, so just to keep track of the tail element
instead of the whole sequence will suffice.

In a perspective of LIS tail element, define state:
    f(i) as the smallest integer that ends an increasing subsequence of length i+1.

Then we can construct the state transition function based on the following strategy.
Iterate through every integer X of the input set and do the following:
1) If X > last element in S, then append X to the end of S. This essentially means we have
found a new largest LIS.
2) Otherwise find the smallest element in S, which is >= than X, and change it to X.

Because S is sorted at any time, the element can be found using binary search in log(N).
Total runtime - N integers and a binary search for each of them - N * log(N) = O(N log N)

'''

class Solution(object):

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self.lengthOfLISDP(nums)
        return self.lengthOfLISDPTailElement(nums)

    def lengthOfLISDP(self, nums: list) -> int:
        f = [1] * (len(nums) + 1)
        f[0] = 0
        len_lis = 0
        for i in range(1, len(nums) + 1):
            for j in range(1, i):
                # if statement here will be faster than logic expression
                if nums[i - 1] > nums[j - 1]:
                    f[i] = max(f[i], f[j] + 1)
            len_lis = max(len_lis, f[i])

        # print(f, len_lis)
        return len_lis

    def lengthOfLISDPTailElement(self, nums: list) -> int:
        '''
        Dynamic programming solution of logarithmic time complexity.
        '''
        # DONE: optimized dynamic programming solution
        f = [-1] * (len(nums) + 1)
        size = 0
        for i, _ in enumerate(nums):
            low, high = 0, size - 1
            while low <= high:
                mid = (low + high) >> 1
                if f[mid] < nums[i]: low = mid + 1
                else: high = mid - 1
            # replace or extend
            f[low] = nums[i]
            size = max(size, low + 1)
        return size

def test():
    solution = Solution()

    assert solution.lengthOfLIS([]) == 0
    assert solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert solution.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6

    print('self test passed')

if __name__ == '__main__':
    test()
