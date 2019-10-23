#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
421. Maximum XOR of Two Numbers in an Array

Total Accepted: 8291
Total Submissions: 19023
Difficulty: Medium
Contributors: shen5630

Given a non-empty array of numbers, a₀, a₁, a₂, … , aₙ-1, where 0 ≤ aᵢ < 2^31.

Find the maximum result of aᵢ XOR aⱼ, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.

================================================================================
SOLUTION

1. Naive solution - element-wise

Compute pair-wise XOR result, take the maximum.

Complexity: O(N²), O(1).

================================================================================
Bitwise perspective

00000011 = 3
00001010 = 10
00000101 = 5
00011001 = 25
00000010 = 2
00001000 = 8

Maximum is:

00000101 = 5
00011001 = 25
----------------
5 ^ 25 = 00011100 = 28

00000101 = 5
00001011 = 11
00011001 = 25
00010101 = 17
----------------
Maximum is 00011110 = 30

It's not necessary to find such two numbers, just giving the result would be enough.

Inspect the problem in a bitwise way. Constructing a maximum number can be done in a
greedy strategy: put 1s at significant bits.

Given
00000101 = 5
00001011 = 11
00011001 = 25
00010101 = 17

Step 1,
Group by first significant bit:
00000101 = 5
00001011 = 11
-------------
00011001 = 25
00010101 = 17

The first set contains candidates for the small number, the second for larger number to
do XOR arithmetic.

Step 2,
group by next significant bit:

......
How to represent the idea???
================================================================================

3. Bitwise prefix tree - trie - bitwise greedy search

The brute force solution is O(N²), because for each number in the array,
we have to match it against every other number in the array, which is O(N).

The maximum integer can be constructed in a bitwise greedy strategy manner:
    construct the number from most significant bit to least significant bit.

Is there a data structure to reduce this O(N) complexity?
Represent the number list with a bitwise TRIE - storing binary representation!
Yes, the key is still representation.

For each number try to find the largest XOR while searching on the tree
with greedy choice.

For each number n in nums, we want to find the other number giving largest XOR.
To achieve so, for each bit b in n, we choose the other number with that bit of ~b,
if we can.


00000011 = 3
00001010 = 10
00000101 = 5
00011001 = 25
00000010 = 2
00001000 = 8

00000010 = 2
00000011 = 3
00000101 = 5
00001000 = 8
00001010 = 10
00011001 = 25

Complexity
O(32N)=O(N), O(1) ~ O(N)

4. Another bitwise - GREEDY VERIFY - prefix mask testing & HASH set

Objective: find c such that c = argmax_{a,b}(a ^ b), where a and b are in input.

To solve the problem, one approach is to EXHAUST ALL PAIRS of (a, b),
another approach is to EXHAUST ALL TARGET VALUES c and VERIFY and problem.
The first approach has an optimal solution with bitwise trie.

XOR has identities:
    If x ^ a = b, then x ^ b = a.
For any number x, whether x can be obtained with XOR of two numbers in array
can be verified in O(N) time with HASH set.

But target XOR value has a SEARCH SPACE of O(2^logM), i.e. O(M), M is maximum integer.
Fortunately, such numerical problem has BITWISE GREEDY property:
    Target value can be generated in a bitwise greedy way, thus PRUNING THE SEARCH TREE.
Then the search process is reduced from O(2^logM) to O(logM)=O(32).


--------------------------------------------------------------------------------
Maximum prefix state transition

To put it simply, at each time, we have an optimal prefix so far, and the
next optimal prefix with 1 more bit can only be obtained by appending 0 or 1.
Then check whether the prefix appended with 1 can be found with XOR.

The recurrence relation is:
    prefix(k) = prefix(k - 1) | (1 << (31-k)), if such prefix can be obtained with XOR,
    else prefix(k - 1).

Complexity
O(NlogM) where M is pow(2,32), O(1) ~ O(N)

Bit manipulation
================

Set a bit
x |= (1 << n)

Clear a bit
x &= ~(1 << n)

Toggle a bit
x ^= (1 << n)

Test a bit
x & (1 << n)

Get rightmost set bit
x & (~x + 1)
x & -x

Unset rightmost set bit
x & (x-1)


Reference: https://en.wikipedia.org/wiki/Bit_manipulation


FOLLOW UP
================================================================================
1. Maximum and of two numbers in an array.


'''

class Solution(object):

    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # result = self._findMaximumXORNaive(nums)
        # result = self._findMaximumXORTrie(nums)
        result = self._findMaximumXORSet(nums)

        print(nums, result)

        return result

    def _findMaximumXORNaive(self, nums):
        # FIXME: TLE(time limit exceeded)
        xor_max = 0
        for i, n in enumerate(nums):
            for j in range(i + 1, len(nums)):
                xor_max = max(xor_max, nums[i] ^ nums[j])
        print(xor_max)
        return xor_max

    def _findMaximumXORTrie(self, nums):
        # build trie
        trie = {}
        for num in nums:
            p = trie
            mask = 1 << 31
            for i in range(31, -1, -1):
                c = (mask & num) >> i
                if c not in p: p[c] = {}

                p = p[c]
                mask >>= 1
            # p['#'] = True

        # find maximum XOR
        xor_max = 0
        for num in nums:
            xor = 0
            p = trie
            mask = 1 << 31
            for i in range(31, -1, -1):
                c = (mask & num) >> i
                b = not c
                if b in p: # greedily trying to obtain bit of 1
                    xor |= mask
                    p = p[b]
                else:
                    p = p[c]
                mask >>= 1
            xor_max = max(xor_max, xor)
            pass

        return xor_max

    # TODO: another bitwise solution without trie
    def _findMaximumXORSet(self, nums):
        xor_max = 0
        mask = 0
        for i in range(31, -1, -1):
            mask |= (1 << i) # adding a bit of 1
            prefixes = {mask & num for num in nums}

            xor_ending_with_1 = xor_max | (1 << i) # adding 1 or 0 to local optimal?
            for prefix in prefixes:
                if prefix ^ xor_ending_with_1 in prefixes: # obtainable
                    xor_max = xor_ending_with_1
                    break

        return xor_max

def test():
    solution = Solution()

    assert solution.findMaximumXOR([]) == 0
    assert solution.findMaximumXOR([1]) == 0
    assert solution.findMaximumXOR([1, 2]) == 3
    assert solution.findMaximumXOR([3, 10, 5, 25, 2, 8]) == 28

    print("self test passed")

if __name__ == '__main__':
    test()
