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

1. brute-force combinations

Enumerate all possible combinations, then patch the smallest missing number. The combinations
can be constructed by adding one number each time. Time complexity is huge, and space
complexity is O(N).

2. Greedy strategy

Define STATE AS THE COVERED RANGE.

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

'''

from collections import defaultdict

class Solution(object):

    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        # return self.minPatchesCombination(nums, n)
        # return self.minPatchesCombinationOpt(nums, n)
        return self.minPatchesGreedyRange(nums, n)

    def minPatchesCombination(self, nums, n):
        '''
        Greedily patch the smallest missing one
        '''
        # FIXME: storing combinations will exceed the time limit
        nums.sort()
        n_patches = 0
        combinations = defaultdict(list)
        combinations[0].append([])
        for i, num in enumerate(nums):
            self.patch(combinations, num, n, dup=i and num == nums[i - 1])

        while True:
            # find missing
            j = 0
            while j <= n and j in combinations:
                j += 1

            if j <= n:
                print('patch', j)
                self.patch(combinations, j, n)
                n_patches += 1
            else:
                break

        tmp = []
        for v in combinations.values():
            tmp.extend(v)
        print(tmp, '\n')
        return n_patches

    def patch(self, combinations: dict, num: int, n, dup: bool=False):
        new = defaultdict(list)
        for k, l in combinations.items():
            s = k + num  # sum
            if s > n:
                continue
            for c in l:
                if dup and not (c and c[-1] == num):
                    continue
                # print(c, num, dup)
                new[s].append(c + [num])
        for k, c in new.items():
            combinations[k].extend(c)
        pass

    def minPatchesCombinationOpt(self, nums, n):
        # FIXME: storing combinations will exceed the time limit
        n_patches = 0
        covered = {0}

        def patch(i):
            print('patch', i, nums, n)
            new = set()
            for j in covered:
                if i + j <= n:
                    new.add(i + j)
            return new

        for i in nums:
            covered |= patch(i)

        while len(covered) != n + 1:
            j = 0
            while j <= n and j in covered:
                j += 1
            if j <= n:
                n_patches += 1
                covered |= patch(j)
            pass
        return n_patches

    def minPatchesGreedyRange(self, nums, n):
        '''
        Scan from 1 to n, maintainer covered range.
        '''
        patches = 0
        covered, i = 0, 0
        while covered < n:
            if i < len(nums) and nums[i] <= covered + 1:
                covered += nums[i]
                i += 1
            else:
                covered += covered + 1
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
