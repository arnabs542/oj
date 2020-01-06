#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
434. Number of Segments in a String

Count the number of segments in a string, where a segment is defined to be a contiguous
sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5

==============================================================================================
SOLUTION


'''

class Solution(object):

    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self._countSegmentsSplit(s)

    def _countSegmentsSplit(self, s:str):
        return len(s.split()) if s else 0

def test():
    solution = Solution()

    assert solution.countSegments('') == 0
    assert solution.countSegments('Hello, my name is John') == 5

    print("self test passed")

if __name__ == '__main__':
    test()
