#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
397. Integer Replacement

Total Accepted: 11060
Total Submissions: 38397
Difficulty: Medium
Contributors: Admin

Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1

==============================================================================================
SOLUTION:

3 -> 4 -> 2 -> 1
3 -> 2 -> 1

5 -> 6 -> 3 -> 2 -> 1
5 -> 4 -> 2 -> 1

15 -> 16 -> 8 -> 4 -> 2 -> 1
15 -> 14 -> 7 -> 6 -> 3 -> 2 -> 1

1. For any positive integer, we have multiple choices to make. Then we can treat it as
a graph, integers as state, and arithmetics as edges, find the shortest path!

2. Any greedy strategy to deal with odd integers?
For any odd integers larger than 3, the last two least significant bits can only be:
    ...01
    ...11
If we mutate the odd integer to get more trailing zeroes, we get a better path.
In the '...01' case, we have to decrease it by 1, to get '...00', because it's better
than '...10' case, where we add 1.
In the '...11' case, we increase it by 1, giving '...00', better than '...10'.

To tell the two scenarios apart, we can use and mask of 3.
0b...11 & 0b11 = 0b11 = 3,
0b...01 & 0b11 = 0b1 = 1,

Special case is when 3 = 0b11 because 1 is the only odd integer that we don't need to
process! So we need to decrease 3 by 1 to get 0b10 = 2.

'''

class Solution(object):

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return self.integerReplacementBFS(n)
        return self.integerReplacementGreedy(n)

    def integerReplacementBFS(self, n) -> int:
        frontier, cache = {n}, set()
        steps = 0
        while frontier:
            for i in frontier:
                if i == 1:
                    return steps
                if i % 2:
                    cache.add(i + 1)
                    cache.add(i - 1)
                else:
                    cache.add(i >> 1)
            steps += 1
            frontier, cache = cache, frontier
            cache.clear()

    def integerReplacementGreedy(self, n) -> int:
        steps = 0
        while n != 1:
            if n % 2 == 0:
                n >>= 1
            elif n & 3 == 3 and n > 3:
                n += 1
            else:
                n -= 1
            steps += 1
        return steps

def test():
    solution = Solution()

    assert solution.integerReplacement(1) == 0
    assert solution.integerReplacement(3) == 2
    assert solution.integerReplacement(5) == 3
    assert solution.integerReplacement(8) == 3
    assert solution.integerReplacement(0b111) == 4
    assert solution.integerReplacement(0b1011) == 5
    assert solution.integerReplacement(15) == 5

    print('self test passed')

if __name__ == '__main__':
    test()
