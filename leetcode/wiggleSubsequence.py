#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
376. Wiggle Subsequence

Total Accepted: 15149
Total Submissions: 44295
Difficulty: Medium
Contributors: Admin

A sequence of numbers is called a wiggle sequence if the differences between successive
numbers strictly alternate between positive and negative. The first difference (if one
exists) may be either positive or negative. A sequence with fewer than two elements is
trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3)
are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not
wiggle sequences, the first because its first two differences are positive and the second
because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle
sequence. A subsequence is obtained by deleting some number of elements (eventually, also
zero) from the original sequence, leaving the remaining elements in their original order.

Examples:
Input: [1,7,4,9,2,5]
Output: 6
The entire sequence is a wiggle sequence.

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Input: [1,2,3,4,5,6,7,8,9]
Output: 2

Follow up:
Can you do it in O(n) time?

==============================================================================================
SOLUTION:

1. Subsequence, overlapping and optimal substructure, of course, Dynamic Programming could be
used.
    Define the state f(i) = (wiggle sequence length ending here, last difference sign),
then do the scanning:
    f(i)[0] = max(f(j)[0] + 1) if nums[i] - f[j] and f(j)[1] are of difference signs.
Time complexity is O(N²).

2. Linear Dynamic Programming

Then at each position, we have these scenarios:
    a wiggle sequence is rising with current number,
    a wiggle sequence is falling with current number,
    current number is equal to previous number,

Define state as:

    f(i) = up(i), down(i)
    up(i) = maximum wiggle length ending here, with last direction as up
    down(i) = maximum wiggle length ending here, with last direction as down

Then we have:
    up(i) = down(i - 1) + 1, if nums[i] > nums[i - 1],
    down(i) = up(i - 1) + 1, if nums[i] < nums[i - 1],

3. Greedy substructure.

The GREEDY OPTIMAL SUBSTRUCTURE can be found by drawing some cases to analyze.
"+-+-+-+-+-"
This solution actually is the above dynamic programming solution with only one state.

Define state:
    f(i) = (wiggle sequence length in subarray from [0, i]),
    last element `last`,
    last difference sign.

Greedy strategy is

if (nums[i] - last) * sign < 0:
    f(i + 1) = f(i) + 1
    sign *= -1
else:
    f(i + 1) = f(i)
last = nums[i]

Even the current number doesn't increase the wiggle sequence's length, we still
update the last element to nums[i], because this will increase the chance that the
following number would contribute to the current wiggle sequence since last element's
covering range have been extended by updating to a further value nums[i].

Take [1, 17, 5, 10, 15, 10] for example, at 15, wiggle sequence length is 4, and 15 doesn't
contribute to the sequence, but we set last element from 10 to 15, so that the following 10 will
contribute.

The greedy strategy indicates that we always use the current number, even if if doesn't
increase the wiggle subsequence.


O(N).
'''

class Solution(object):

    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.wiggleMaxLengthDP(nums)
        # return self.wiggleMaxLengthGreedy(nums)

    def wiggleMaxLengthDP(self, nums: list) -> int:
        '''
        Space optimized linear dynamic programming solution with two states:
            (
                max rising length ending here,
                max falling length ending here,
            )
        '''
        if len(nums) <= 1:
            return len(nums)
        up = down = 1
        for i in range(2, len(nums) + 1):
            if nums[i - 1] > nums[i - 2]:
                up = down + 1
            elif nums[i - 1] < nums[i - 2]:
                down = up + 1
            pass
        return max(up, down)

    def wiggleMaxLengthGreedy(self, nums):
        max_len = 0
        last, sign = None, None
        for i, _ in enumerate(nums):
            # print(i, nums[i], last, sign, 'nums', nums)
            if last is None or \
               (sign is None and nums[i] != last) or \
               (sign and (nums[i] - last) * sign < 0):
                max_len += 1
                if last is not None:
                    sign = nums[i] - last
            last = nums[i]
        return max_len


def test():
    solution = Solution()

    assert solution.wiggleMaxLength([]) == 0
    assert solution.wiggleMaxLength([1]) == 1
    assert solution.wiggleMaxLength([1, 3]) == 2
    assert solution.wiggleMaxLength([1, 1]) == 1
    assert solution.wiggleMaxLength([1, 7, 4, 9, 2, 5]) == 6
    assert solution.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]) == 7
    assert solution.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, ]) == 6
    assert solution.wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2

    print('self test passed')

if __name__ == '__main__':
    test()
