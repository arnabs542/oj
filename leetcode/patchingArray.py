#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
330. Patching Array

Total Accepted: 17309
Total Submissions: 55488
Difficulty: Hard
Contributors: Admin

Given a sorted positive integer array nums and an integer n, add/patch elements to the
array such that any number in range [1, n] inclusive can be formed by the sum of some
elements in the array. Return the minimum number of patches required.

Example 1:
nums = [1, 3], n = 6
Return 1.

Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are:
    [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:
nums = [1, 5, 10], n = 20
Return 2.
The two patches can be [2, 4].

Example 3:
nums = [1, 2, 2], n = 5
Return 0.

==============================================================================================
SOLUTION:

1. Brute-force combinations

Enumerate all possible combinations, then patch the smallest missing number.
The combinations subsets is updated incrementally.

Define state = (
i: integer in range [1, n],
subsets
)

Time complexity is exponential O(2ⁿ), and space complexity is O(2ⁿ).

2. Brute force combinations optimized

Tracking combination subsets sums, instead of the subsets.

Define state as a tuple of
(
i: integer in range [1, n],
subsets sums
)

Complexity: O(N²), O(N)

3. Combination state to RANGE state

The combination sums must form a interval, why not track the range state covered?

The COVERED RANGE can be represented by interval [0, high].

Define the state as a tuple of
(
i: index of the sorted array,
high: interval upper bound,
)

Then extend the range by adding a number from the array. The eligible number must not be
greater than the range's right end plus 1. Let's say the covered range's right end is `high`,
the for m <= high + 1, we have:

    m + 0<= high + 1,
    m + high <= high + 1 + high = 2 * high + 1,

Then adding m will make [m, high + m] covered. Together with [1, high], m can
extend the range from [1, high] to [1, high + m].

If no eligible number exists in the array, we will have to patch high + 1, covering new range
[1, high + high + 1].

This is similar with 'Jump game' problem.

Time complexity: O(M + logN), where M is the array size, N is target number n.
Space complexity: O(1)

'''

from collections import defaultdict

class Solution(object):

    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        # return self.__minPatchesBruteForceCombination(nums, n)
        # return self._minPatchesCombinationOpt(nums, n)
        return self._minPatchesGreedyRange(nums, n)

    def _minPatchesBruteForceCombination(self, nums, n):
        '''
        Greedily patch the smallest missing one
        '''

        def patch(combinations: dict, num: int, n, dup: bool=False):
            """
            Generate new combination subsets with new element,
            in a dynamic programming approach

            """
            new = defaultdict(list)
            for s, subsets in combinations.items():
                newSum = s + num  # sum
                if newSum > n:
                    continue
                for c in subsets:
                    if dup and not (c and c[-1] == num):
                        continue
                    # print(c, num, dup)
                    new[newSum].append(c + [num])
            for s, c in new.items():
                combinations[s].extend(c)
            pass

        # FIXME: storing combinations will exceed the time limit
        nums.sort()
        n_patches = 0
        combinations = defaultdict(list)
        combinations[0].append([]) # subset sum -> subsets
        for i, num in enumerate(nums):
            patch(combinations, num, n, dup=i and num == nums[i - 1])

        while True:
            # find missing
            j = 0
            while j <= n and j in combinations:
                j += 1

            if j <= n:
                print('patch', j)
                patch(combinations, j, n)
                n_patches += 1
            else:
                break

        tmp = []
        for v in combinations.values():
            tmp.extend(v)
        print(tmp, '\n')
        return n_patches


    def _minPatchesCombinationOpt(self, nums, n):
        """
        A little optimization, not storing combination subsets, but storing their sums.

        Still, slow and exceeds time limit.
        """
        # FIXME: storing combinations will exceed the time limit
        n_patches = 0
        subsetSums = {0}

        def patch(i):
            print('patch', i, nums, n)
            new = set()
            for j in subsetSums:
                if i + j <= n:
                    new.add(i + j)
            return new

        for i in nums:
            subsetSums |= patch(i)

        while len(subsetSums) != n + 1:
            j = 0
            while j <= n and j in subsetSums:
                j += 1
            if j <= n:
                n_patches += 1
                subsetSums |= patch(j)
            pass
        return n_patches

    def _minPatchesGreedyRange(self, nums, n):
        '''
        Scan from 1 to n, maintainer covered range.
        '''
        patches = 0
        covered, i = 0, 0
        while covered < n:
            if i < len(nums) and nums[i] <= covered + 1:
                covered += nums[i] # extend the range seamlessly
                i += 1
            else:
                covered += covered + 1 # there is a gap now
                patches += 1

        return patches

def test():
    solution = Solution()

    assert solution.minPatches([1, 3], 6) == 1
    assert solution.minPatches([1, 5, 10], 20) == 2
    assert solution.minPatches([1, 2, 2], 5) == 0
    assert solution.minPatches([1, 1, 2], 5) == 1
    assert solution.minPatches([], 20) == 5
    assert solution.minPatches([1, 2, 31, 33], 2147483647) == 28

    print ('self test passed')

if __name__ == '__main__':
    test()
