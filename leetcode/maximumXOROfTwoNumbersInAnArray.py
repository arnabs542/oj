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

3. Bitwise prefix tree - trie

The brute force solution is O(N²), because for each number in the array, we have to
match it against every other number in the array, which is O(N).

Is there a data structure to reduce this O(N) complexity?
Well, the numbers in the array can be treated as words in dictionary, and we want to
match a number against the dictionary.

By matching, I mean constructing the maximum XOR result.
The maximum integer can be constructed in a greedy strategy manner:
    choose the maximum significant bits first.

In this situation, apparently, it is a prefix problem in a bitwise perspective:
    construct the result from most significant bit to least significant bit.

Build a TRIE - PREFIX TREE storing binary representation of all numbers.
For each number try to find the largest XOR while searching on the tree
with elaborated matching.

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

4. Another bitwise solution without trie - prefix state transition & set

Based on above reasoning, the key to the solution is to construct a maximal prefix.
And a prefix problem can be solved with trie, in a bitwise perspective.

Note that there are only two digits: 0 and 1, in finite constant space!
Then it's possible to EXHAUSTED SEARCH for whether the next possible maximal prefix
"x...x1" can be obtained, with XOR regarding to each of the given numbers.

--------------------------------------------------------------------------------
Maximum prefix state transition

To put it simply, at each time, we have an optimal prefix so far, and the
next optimal prefix with 1 more bit can only be obtained by appending 0 or 1.
Then check whether the prefix appended with 1 can be found with XOR.

The recurrence relation is:
    prefix(k) = prefix(k - 1) | (1 << k), if such prefix can be obtained with XOR,
    else prefix(k - 1).

This means that if prefix(k - 1) | (1 << k) can be found with XOR, then current
maximum prefix is obtained by setting current bit to 1.

If a ^ b = c, then c ^ a = b.

Complexity
O(N), O(1) ~ O(N)


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
