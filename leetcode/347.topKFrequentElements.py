#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
347. Top K Frequent Elements

Total Accepted: 44317
Total Submissions: 96835
Difficulty: Medium
Contributors: Admin

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the
array's size.

================================================================================
SOLUTION

1. Hash to store elements' occurrence frequency. And, for top K problem, use HEAP.

Complexity: O(n + nlogk)

2. Hash and sort according to occurrence count.

Complexity: O(NlogN)

3. Bucket - separate chaining in hash table collision resolution method
The possible values for the occurrence are in range [0, n].
Maintain the occurrence count in the buckets, and get the largest k buckets.

================================================================================
FOLLOW UP
1. Top k frequent elements in data stream?
Solution: separate chaining, like least frequently used cache implementation.
Refer to the cpp implementation.

'''

from collections import Counter

class Solution(object):

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # return self.topKFrequentHeap(nums, k)
        return self.topKFrequentBucket(nums, k)

    def topKFrequentHeap(self, nums, k):
        # TODO: my implementation
        pass

    def topKFrequentHeapBuiltin(self, nums, k):
        '''
        Using builtin Counter data structure
        '''
        counter = Counter(nums)
        return list(map(lambda x: x[0], counter.most_common(k)))

    def topKFrequentBucket(self, nums, k) -> list:
        result = []
        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, c in counter.items():
            buckets[c].append(n)
        c = len(nums)
        for c in range(len(nums), -1, -1):
            if len(result) >= k: break
            result.extend(buckets[c])
        print(buckets, result)
        return result

def test():
    solution = Solution()

    assert solution.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]

    print("self test passed")

if __name__ == '__main__':
    test()
