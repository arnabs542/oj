#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
229. Majority Element II

Total Accepted: 41951
Total Submissions: 153056
Difficulty: Medium
Contributors: Admin

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
The algorithm should run in linear time and in O(1) space.

Hint:

  How many majority elements could it possibly have?


==============================================================================================
SOLUTION

There are three kind of possible values of n:
3m, 3m + 1, 3m + 2.

The majority element must appear more than m times, i.e., at least m + 1 times. So there will
be at most 2 majority elements.

1. Count

Complexity: O(n), O(n)

2. Partition
Partition, and count to verify.

Three way partition the array, then we have three parts:
    smaller parts, equal elements in the middle, greater parts.

1) if middle part has size at least m + 1, then we have one majority number.
2) else if either one of smaller or greater has size at least m + 1, then the majority
elements, maybe 1 or 2, are within that part. Repeat the procedure on this array.
3) Both smaller and greater parts have size at least m + 1, then possible two majority
must be separated in these two parts. Reduce it to "majority element".

Time complexity can be guaranteed to be O(n), but space complexity maybe O(logn),
because of the recursion depth of partition.

3. Voting algorithm

The idea is to keep track of a list of candidates. And scan the array,
cancel candidates' occurrence count against occurrence count of non-candidates.

How to keep track of two candidates? How to update them?

Avoid two majority elements cancelling each other?

Keep a list of k candidates, where k = 2, in this problem.

Scan the array. For each number e,
1) If e is equal to one of the candidates, increment its counter, continue
2) If current candidates size is smaller than k, append, and set current
number's counter to 1.
3) If candidates size is full, and one of them have 0 occurrence counter.
Then e can be a new candidate, don't cancel others' counter!
4) If candidates size is full, and they all have positive candidates.
Then e is equal to none of them, decrement all of the counters.



'''


class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # result = self._majorityElementPartition(nums)
        result = self._majorityElementVote(nums)

        print(nums, " => ", result)

        return result

    def _majorityElementPartition(self, nums):
        # FIXME: tedious to implement, and use O(logn) space
        pass

    def _majorityElementVote(self, nums):
        m = len(nums) // 3
        candidates = [] # keep k candidates
        counter = [] # occurrence counter for k candidates
        k = 2 # k is 2, in this problem

        # first pass, get candidates
        for n in nums:
            i = 0
            fill = -1
            while i < len(candidates):
                # have a match
                if candidates[i] == n:
                    counter[i] += 1
                    break
                if counter[i] == 0 and fill < 0: fill = i # position for new candidate
                i += 1

            if i < len(candidates):
                continue # found a match
            elif len(candidates) < k: # append new candidate
                candidates.append(n)
                counter.append(1)
            elif fill > -1:
                candidates[fill] = n # insert candidate
                counter[fill] = 1 # XXX: candidates don't cancel each other
            else:
                for j, _ in enumerate(counter): counter[j] -= 1 # no match for all candidates

        # 2nd pass, count
        for i in range(min(k, len(counter))):
            counter[i] = 0
            for n in nums: counter[i] += n == candidates[i]

        return [n for i, n in enumerate(candidates) if counter[i] > m]

def test():
    solution = Solution()

    assert solution.majorityElement([]) == []
    assert solution.majorityElement([1]) == [1]
    assert solution.majorityElement([1, 1]) == [1]
    assert solution.majorityElement([1, 2]) == [1, 2]
    assert solution.majorityElement([1, 2, 1]) == [1]
    assert solution.majorityElement([1, 2, 1, 1]) == [1]
    assert solution.majorityElement([1, 2, 1, 2]) == [1, 2]
    assert solution.majorityElement([1, 2, 3, 1, 2]) == [1, 2]
    assert sorted(solution.majorityElement([3, 1, 2, 1, 2])) == sorted([1, 2])
    assert sorted(solution.majorityElement([3, 1, 2, 1, 1])) == sorted([1])
    assert sorted(solution.majorityElement([3, 1, 2, 1, 1])) == sorted([1])
    assert sorted(solution.majorityElement([3, 1, 2, 1, 1])) == sorted([1])
    assert sorted(solution.majorityElement([3, 1, 2, 2, 1])) == sorted([1, 2])
    assert sorted(solution.majorityElement([3, 1, 2, 1])) == sorted([1])
    assert sorted(solution.majorityElement([3, 1, 2, 1, 2])) == sorted([1, 2])
    assert sorted(solution.majorityElement([1, 1, 1, 2, 3, 4, 5, 6])) == sorted([1])
    assert sorted(solution.majorityElement([1, 1, 1, 1, 2, 3, 4, 5, 6, 7])) == sorted([1])

    print("self test passed")

if __name__ == '__main__':
    test()
