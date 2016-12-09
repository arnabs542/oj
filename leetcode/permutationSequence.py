#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
60. Permutation Sequence

Total Accepted: 70423
Total Submissions: 261991
Difficulty: Medium
Contributors: Admin

The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"

Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

==============================================================================================
SOLUTION:

1. Generate next permutation one by one. Time limit exceeded, O(k).

2. Find the permutation in O(N) time with divide and conquer

Note that the permutations are in order. Ordered list means we can do binary search or random
access in O(1) time.

Denote factorial with f(n), then f(n) = n! = n * (n - 1)! = n * f(n - 1).

Permutations of n number can be divided into n groups of size (n - 1)!. Then we can find the kth
permutation's first number by determining which group is belongs to.

Recurrence relation:
    index = ceil(k / f(n - 1)),
    k' = k - (index - 1) * f(n - 1)
Then the remaining part is the k'th permutation of n numbers starting with index.

Then we use the same recurrence relation to determine the next number. In this way, we generate
the permutation's numbers one by one.
'''

import math

class Solution(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # return self.getPermutationBruteForce(n, k)
        return self.getPermutationOpt(n, k)

    def getPermutationBruteForce(self, n, k):
        p = list(range(1, n + 1))
        for _ in range(k - 1):
            self.nextPermutation(p)
        print(''.join(map(lambda x: str(x), p)))
        return ''.join(map(lambda x: str(x), p))

    def nextPermutation(self, p: list):
        i = len(p) - 1
        while i and p[i] < p[i - 1]:
            i -= 1
        idx = i
        for j in range(i, len(p)):
            if p[idx] > p[j] > p[i - 1]:
                idx = j
        p[i - 1], p[idx] = p[idx], p[i - 1]
        p[i:] = sorted(p[i:])

    def getPermutationOpt(self, n: int, k: int):
        groupSize = 1
        for i in range(1, n + 1): groupSize *= i
        candidates = sorted(map(lambda x: str(x), range(1, n + 1)))
        seq = []
        for i in range(n):
            groupSize //= n - len(seq)
            groupNum = int(math.ceil(k / groupSize))
            seq.append(candidates[groupNum - 1])
            candidates.pop(groupNum - 1)

            k -= (groupNum - 1) * groupSize
        print(''.join(seq))
        return ''.join(seq)

def test():
    solution = Solution()

    assert solution.getPermutation(1, 1) == "1"
    assert solution.getPermutation(3, 1) == "123"
    assert solution.getPermutation(3, 4) == "231"
    assert solution.getPermutation(3, 6) == "321"
    assert solution.getPermutation(9, 171669) == "531679428"

    print('self test passed')

if __name__ == '__main__':
    test()
