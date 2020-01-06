#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
49. Group Anagrams Add to List

Total Accepted: 117200
Total Submissions: 360674
Difficulty: Medium
Contributors: Admin

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.

==============================================================================================
SOLUTION

1. Naive solution. Compare with an element from each group. O(N²M) where M is the string length.

2. Linear scan the list and compute the anagram metric, append it into the corresponding list
with that metric. The lists can be represented with a hash table, where key is the metric, and
value is the anagram group.

'''

class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        return self.groupAnagramsSort(strs)

    def groupAnagramsSort(self, strs):
        dict_group = {}
        for s in strs:
            key = ''.join(sorted(s))
            dict_group.setdefault(key, [])
            dict_group[key].append(s)
        return list(dict_group.values())


def test():
    solution = Solution()

    assert solution.groupAnagrams([]) == []
    assert solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["ate", "eat", "tea"],
        ["nat", "tan"],
        ["bat"]
    ]

    print("self test passed")

if __name__ == '__main__':
    test()
