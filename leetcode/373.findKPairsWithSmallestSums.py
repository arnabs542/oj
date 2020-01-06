#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
373. Find K Pairs with Smallest Sums

Total Accepted: 18425
Total Submissions: 62287
Difficulty: Medium
Contributors: Admin

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element
from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]

==============================================================================================
SOLUTION

1. Brute force, generate all pairs, find the smallest. Time and space complexity is O(mn).

2. Smallest k is similar to top k, indicating we can use MAX HEAP. Space complexity can be
reduced to O(k), But time complexity remains the same, maybe because the monotonicity
property is not utilized.

3. BREADTH-FIRST SEARCH with HEAP(min-heap) as search frontier.
At each step of iteration, we pop out the smallest tuple from
the heap into the result list, and push in its adjacent neighbor vertices(states).

However it needs auxiliary data structure to maintain visited vertices to avoid duplicate.
Time complexity is O(KLogK), and space complexity is O(K).

4. The above BFS process can be optimized by narrowing the search frontier.
The candidates can be generated in a greedy way. Maintain a HEAP SEARCH FRONTIER as follows.
    First, we take nums1[0] paired with the first k elements of nums2 as the initial
search frontier, so that we have (0,0), (0,1), (0,2),.....(0,k-1) in the heap. Each time
after we pick the pair with min sum, we put the new pair with the second index +1. ie,
pick (0,0), we put back (1,0). Therefore, the heap alway maintains at most
min(k, len(nums2)) elements.

'''

from typing import List
from heapq import heappush, heappop

class Solution(object):

    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # return self.kSmallestPairsBruteForce(nums1, nums2, k)
        # return self.kSmallestPairsHeap(nums1, nums2, k)
        # return self.kSmallestPairsBFSHeap(nums1, nums2, k)
        return self.kSmallestPairsBFSHeapOpt(nums1, nums2, k)

    def kSmallestPairsBruteForce(self, nums1: list, nums2: list, k: int) -> List[List[int]]:
        # FIXME: memory limit exceeded
        cartesian = [[u, v] for v in nums2 for u in nums1]
        cartesian.sort(key=sum)
        print(cartesian[:k])
        return cartesian[:k]

    def kSmallestPairsHeap(self, nums1: list, nums2: list, k: int) -> List[List[int]]:
        heap = []
        for u in nums1:
            for v in nums2:
                heappush(heap, [-u - v, u, v])
                if len(heap) > k:
                    heappop(heap)
        heap.sort(reverse=True)
        result = list(map(lambda x: x[1:], heap))
        print(result)
        return result

    def kSmallestPairsBFSHeap(self, nums1: list, nums2: list, k: int) -> List[List[int]]:
        '''
        Breadth-first search while heapifying the search frontier
        '''
        if not (nums1 and nums2):
            return []
        heap = [[nums1[0] + nums2[0], 0, 0]] # heap search frontier
        result = []
        visited = {(0, 0)} # filter duplicates
        while heap and len(result) < k:
            _, i, j = heappop(heap)
            result.append([nums1[i], nums2[j]])
            for i1, j1 in ([i + 1, j], [i, j + 1]):
                if i1 < len(nums1) and j1 < len(
                        nums2) and (i1, j1) not in visited:
                    visited.add((i1, j1))
                    heappush(heap, [nums1[i1] + nums2[j1], i1, j1])
                pass
        # result.sort()
        print('result:', result, 'heap:', heap)
        return result

    def kSmallestPairsBFSHeapOpt(self, nums1: list, nums2: list, k: int) -> List[List[int]]:
        '''
        Breadth-first search HEAP SEARCH FRONTIER optimized.
        '''
        # TODO: optimized greedy searching frontier
        if not (nums1 and nums2):
            return []
        heap, result = [], [] # heap search frontier, result
        for i in range(len(nums2)):
            heappush(heap, [nums1[0] + nums2[i], 0, i])
        while heap and len(result) < k:
            _, i, j = heappop(heap)
            result.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1):
                heappush(heap, [nums1[i + 1] + nums2[j], i + 1, j])
        print('result:', result, 'heap:', heap)
        return result

def test():
    solution = Solution()

    assert solution.kSmallestPairs([1, 7, 11], [2, 4, 6], 3) == [
        [1, 2], [1, 4], [1, 6]]
    assert solution.kSmallestPairs([1, 1, 2], [1, 2, 3], 2) == [[1, 1], [1, 1]]
    assert solution.kSmallestPairs([1, 2], [3], 3) == [[1, 3], [2, 3]]
    assert solution.kSmallestPairs([1, 2, 4, 5, 6], [3, 5, 7, 9], 3) == [
        [1, 3], [2, 3], [1, 5]]
    assert solution.kSmallestPairs([1, 1, 2], [1, 2, 3], 10) == [
        [1, 1], [1, 1], [1, 2],
        [1, 2], [2, 1], [1, 3],
        [1, 3], [2, 2], [2, 3]]

    print("self test passed")

if __name__ == '__main__':
    test()
