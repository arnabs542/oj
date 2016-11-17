#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
89. Gray Code

Total Accepted: 75230
Total Submissions: 193653
Difficulty: Medium
Contributors: Admin

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the
sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

==============================================================================================
SOLUTION:
    Treat this problem as a GRAPH problem, then each number is a VERTEX, and EDGES are the
difference by only one bit(power of 2). And the graph is undirected.

    For 1-bit numbers, 0 and 1 are mutually connected(differs in only one bit), by induction, we
see any n-bit numbers are STRONGLY CONNECTED COMPONENT.

n = 3:
    000 - 001 - 011 - 010
     |     |     |     |
    100 - 101 - 111 - 110

    or

    000 - 001
     |     |
    010 - 011
     |     |
    110 - 111
     |     |
    100 - 101

Each vertex is connected with n neighbors, n for each bit. Thus, we have n branches to explore
for each number. Get the neighbor vertex by bit flip manipulation.

'''

class Solution(object):

    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return self.grayCodeDFS(n)

    def grayCodeDFS(self, n: int) -> int:
        '''
        depth-first search solution
        '''
        visited = {0}
        seq = [0]
        for _ in range(1, 1 << n):
            val = seq[-1]
            for i in range(n):
                # mask = 1 << i
                # neighbor = val ^ mask
                neighbor = val ^ (i << i)
                if neighbor not in visited:
                    seq.append(neighbor)
                    visited.add(neighbor)
                    break
        print(seq)
        return seq

    def grayCodeBit(self, n: int) ->int:
        '''
        Generate gray code one by one with bit manipulation
        '''
        # TODO: bit manipulation solution

def test():
    solution = Solution()

    assert solution.grayCode(0) == [0]
    assert solution.grayCode(1) == [0, 1]
    assert solution.grayCode(2)
    assert solution.grayCode(3)

    print('self test passed')

if __name__ == '__main__':
    test()
