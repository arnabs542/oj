#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
451. Sort Characters By Frequency

Total Accepted: 11450
Total Submissions: 22546
Difficulty: Medium
Contributors: stickypens

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

==============================================================================================
SOLUTION

Similar problem to Top K Frequent Elements.

1. HASH and HEAP

2. Bucket
Since there are only 26 letters, which is a finite set, then we can use buckets to store
corresponding value.

'''

from collections import Counter

class Solution(object):

    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.frequencySortHeap(s)

    def frequencySortHeap(self, s):
        counter = Counter(s)
        result = ''
        for k, v in counter.most_common():
            result += k * v
        print(result)
        return result

    # TODO: bucket

def test():
    solution = Solution()

    assert solution.frequencySort("tree") in ["eetr", "eert"]
    assert solution.frequencySort("cccaaa") in ["cccaaa", "aaaccc"]
    assert solution.frequencySort("Aabb") in ["bbAa", "bbaA"]

    print("self test passed")

if __name__ == '__main__':
    test()
