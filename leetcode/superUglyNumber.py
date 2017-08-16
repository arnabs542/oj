#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
313. Super Ugly Number

Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list
primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of
the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 10⁶, 0 < primes[i] < 1000.
(4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

==============================================================================================
SOLUTION

An ugly number must be multiplied by any one prime factor given from a smaller ugly number.

1. Brute force
Generate the next super ugly number by multiplying a smaller ugly number with a prime factor
and taking the minimal one among all possible values.

This procedure is CARTESIAN PRODUCT of the primes list and super ugly number list, and of
course, involves lots of DUPLICATE COMPUTATIONS.

Complexity: O(k + k* 2 + ... + k * n ) = O(kn²)

2. Heap optimized
Use heap to optimize the process to obtain the minimal candidate.
Complexity: O(knlogn)

3. ORDERED LINEAR SEARCH FRONTIER: keep track of only eligible search frontiers with k pointers

GRAPH ABSTRACTION
-----------------
Treat this generation process as a graph search process. Each ugly number is an vertex,
and each prime factor is an edge, which can be reused. Each vertex is connected to other
vertices via edges. An edge serve as state transition from one vertex to another vertex.
And only one of the prime factor can be used at each transition.

Where does the duplicate computations come from?
Next super ugly number is generate by multiply an existing one by a prime factor. When we
take that Cartesian product, a pair of prime factor and ugly number may have already been
explored before. This is the root cause for duplicate computations in the brute force solution.

How to optimize?
Eliminate invalid graph search frontiers of generated ugly numbers.

Let's say the generated partial super ugly number list is array `ugly`, of size m. For an
arbitrary prime factor in the prime list, is every Super Ugly Number in `ugly` eligible?

Actually, the ugly numbers that have been multiplied by this prime factor are located
in a front interval in the ugly numbers list. And they are in successive locations. This can
be proved by contradiction, using the condition that the generated ugly numbers list are ordered.

This graph search frontiers are of the same size of prime list size, k. Each one of them is
a division point, where the smaller ugly numbers have already been explored. By explored I
mean they have generated larger ugly number production with corresponding prime factor.

# Reduce it to the simplest situation, where there is only one prime factor.
# Every super ugly number
# When we have already generated a list of super ugly number,
# Time space trade-off ?

TL;DR
Given that, the eligible search frontiers(multiplication pair) are correspondent to the
primes list.
Maintain a list of k pointers, of which the ith pointer points to a super ugly number
that may produce the next super ugly number with ith prime factor.

Complexity: O(kn)

4. Space time trade-off
Avoid duplicate multiplication.

5. Further optimization: heap for getting minimal candidate

'''

class Solution(object):

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        # return self._nthSuperUglyNumberNPointers(n, primes)
        return self._nthSuperUglyNumberNPointersOpt(n, primes)

    def _nthSuperUglyNumberNPointers(self, n, primes):
        '''
        Linear search frontier
        '''
        indices = [0 for _ in enumerate(primes)]
        ugly = [1]
        while len(ugly) < n:
            min_ugly = float('inf')
            for i, _ in enumerate(primes):
                min_ugly = min(min_ugly, ugly[indices[i]] * primes[i])

            ugly.append(min_ugly)
            for i, _ in enumerate(primes):
                if min_ugly == ugly[indices[i]] * primes[i]:
                    indices[i] += 1

        print(ugly)
        return ugly[n - 1]

    def _nthSuperUglyNumberNPointersOpt(self, n, primes):
        indices = [0 for _ in enumerate(primes)]
        # cache = [1 for _ in enumerate(primes)]
        cache = list(primes)
        ugly = [1]
        while len(ugly) < n:
            min_ugly = float('inf')
            for i, _ in enumerate(primes):
                if cache[i] == ugly[-1]:
                    indices[i] += 1
                    cache[i] = ugly[indices[i]] * primes[i]
                min_ugly = min(min_ugly, cache[i])

            ugly.append(min_ugly)

        print(ugly)
        return ugly[n - 1]

    def _nthSuperUglyNumberNPointersHeap(self, n, primes):
        # TODO: heap to get minimal in O(logK) time complexity
        pass

def test():
    import time

    start = time.time()
    solution = Solution()

    assert solution.nthSuperUglyNumber(12, [2, 7, 13, 19]) == 32
    assert solution.nthSuperUglyNumber(1, [2, 3, 5]) == 1
    assert solution.nthSuperUglyNumber(4, [2]) == 8
    # assert solution.nthSuperUglyNumber(9, [1]) == 1

    end = time.time()
    print("self test passed in %f seconds" % (end - start))

if __name__ == '__main__':
    test()
