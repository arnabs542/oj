#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
264. Ugly Number II

Total Accepted: 47242
Total Submissions: 151008
Difficulty: Medium
Contributors: Admin

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example,
1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.

Hint:

1. The naive approach is to call isUgly for every number until you reach the nth one. Most
numbers are not ugly. Try to focus your effort on generating only the ugly ones.
2. An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
3. The key is how to maintain the order of the ugly numbers. Try a similar approach of merging
from three sorted lists: L1, L2, and L3.
4. Assume you have U_k, the kth ugly number. Then U_{k+1} must be Min(L1 * 2, L2 * 3, L3 * 5).

==============================================================================================
SOLUTION:
    Generate one by one.
1. Priority queue solution
Time complexity: O(NlogN).
Space complexity: more than O(N).

2.Three pointers?

'''

from queue import PriorityQueue

from heapq import heappush, heappop

class Solution(object):

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return self.nthUglyNumberGenerate(n)
        return self.nthUglyNumberGenerateThreePointers(n)

    def nthUglyNumberGenerate(self, n):
        pq = PriorityQueue()
        pq.put(1)
        prev = ugly = None
        for _ in range(n):
            while ugly == prev:
                ugly = pq.get()
            prev = ugly

            for factor in (2, 3, 5):
                pq.put(ugly * factor)
        print('ugly number:', ugly)
        return ugly

    def nthUglyNumberGenerate2(self, n):
        pq = []
        heappush(pq, 1)
        prev = ugly = None
        for _ in range(n):
            while ugly == prev:
                ugly = heappop(pq)
            prev = ugly

            for factor in (2, 3, 5):
                heappush(pq, ugly * factor)
        return ugly

    def nthUglyNumberGenerateThreePointers(self, n) -> int:
        # TODO: the unthinkable three pointers solution...
        results = [0] * n
        results[0] = 1
        p = q = r = 0
        i = 1
        for i in range(1, n):
            results[i] = min(results[p] * 2, results[q] * 3, results[r] * 5)
            # duplicate will be filtered here, because pointers may be all increased
            if results[i] == results[p] * 2: p += 1
            if results[i] == results[q] * 3: q += 1
            if results[i] == results[r] * 5: r += 1
        return results[n - 1]

def test():
    solution = Solution()

    assert solution.nthUglyNumber(1) == 1
    for i in range(1, 7):
        print(i, 'th ugly number:')
        assert solution.nthUglyNumber(i) == i
    assert solution.nthUglyNumber(7) == 8
    assert solution.nthUglyNumber(8) == 9
    assert solution.nthUglyNumber(1000) == 51200000

    print('self test passed')

if __name__ == '__main__':
    test()
