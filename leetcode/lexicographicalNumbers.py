#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
386. Lexicographical Numbers

Total Accepted: 8915
Total Submissions: 23787
Difficulty: Medium
Contributors: Admin

Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be
as large as 5,000,000.
===============================================================================================
SOLUTION:
    1. The order of numbers of same count of digits is consistent with their lexicographical numbers
    2. Lexicographical order are compared from the beginning of two strings, and empty character is
smaller than any other characters.
    3. Generate from the most significant starting with 1, add trailing zeros where we can. When
we can't append zeroes any more, increase the current number until there is carry. Then backtrack
to the numbers with fewer count of digits by removing trailing zeroes.
    4. At each pass of iteration, determine whether to add a trailing zero or increase the
number by 1.
'''

class Solution(object):

    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = self.lexicalOrderDFS(n)
        return result

    def lexicalOrderSort(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # FIXME: memory limit exceeded with stringify and sort
        result = sorted([i for i in range(1, n + 1)], key=str)
        return result

    def lexicalOrderDFS(self, n):
        """
        :type n: int
        :rtype: List[int]

        DEPTH-FIRST SEARCH algorithm

        If we look at the order we can find out we just keep adding digit from
        0 to 9 to every digit and make it a tree.
        Then we visit every node in pre-order.
               1   -    2    -   3  - ...
              /\        /\       /\
           10 ...19  20...29  30...39   ....
           /
        100...
        """
        result = []
        i = 1
        while len(result) < n:
            result.append(i)
            # exploring neighbors
            if i * 10 <= n:
                i *= 10
                continue
            elif i + 1 > n:
                i //= 10
            pass
            # increase the number by 1
            i += 1
            # until carry occurs, remove trailing zeroes
            while i % 10 == 0:
                i //= 10

        return result

def test():
    solution = Solution()

    assert solution.lexicalOrder(13) == [
        1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
    assert solution.lexicalOrder(113) == solution.lexicalOrder(113)
    assert solution.lexicalOrder(234) == solution.lexicalOrder(234)
    assert solution.lexicalOrder(14959) == solution.lexicalOrderSort(14959)
    assert solution.lexicalOrder(49999) == solution.lexicalOrderSort(49999)
    print('self test passed')

if __name__ == '__main__':
    test()
