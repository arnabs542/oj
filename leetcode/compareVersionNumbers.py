#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
165. Compare Version Numbers

Total Accepted: 68644
Total Submissions: 365130
Difficulty: Easy
Contributors: Admin

Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth
second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37

SOLUTION:
    Split version number into list, compare part by part
'''

class Solution(object):

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        t1 = version1.split('.')
        t2 = version2.split('.')
        i, j = 0, 0
        while i < len(t1) and j < len(t2):
            if int(t1[i]) < int(t2[j]):
                return -1
            elif int(t1[i]) == int(t2[j]):
                i += 1
                j += 1
                continue
            else:
                return 1

        if i == len(t1):
            if j < len(t2):
                return 0 if int(''.join(t2[j:])) == 0 else -1
            else:
                return 0

        if j == len(t2):
            if i < len(t1):
                return 0 if int(''.join(t1[j:])) == 0 else 1
            else:
                return 0

def test():
    solution = Solution()
    assert solution.compareVersion('0.1', '1.1') < 0
    assert solution.compareVersion('1.1', '1.2') < 0
    assert solution.compareVersion('1.2', '13.37') < 0
    assert solution.compareVersion('1.0', '1') == 0
    assert solution.compareVersion('0.1', '0.0.1') > 0
    print('self test passed')

if __name__ == '__main__':
    test()
