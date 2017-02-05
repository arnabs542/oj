#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
274. H-Index

Total Accepted: 57830
Total Submissions: 181558
Difficulty: Medium
Contributors: Admin

Given an array of citations (each citation is a non-negative integer) of a researcher,
write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of
his/her N papers have at least h citations each, and the other N − h papers have no more
than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in
total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher
has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations
each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.

Hint:

1. An easy approach is to sort the array first.
2. What are the possible values of h-index?
3. A faster approach is to use extra space.

==============================================================================================
SOLUTION:

1. Sort and do linear search
Sorting takes O(NlogN), and linear search takes O(N) or O(logN), so overall is O(NlogN).

2. Possible values are in range [1, n], UNIFORMLY DISTRIBUTED over a range: BUCKETS!.

Maintain THE NUMBER OF LARGER VALUES with BUCKETS and PREFIX SUM (CUMULATIVE DISTRIBUTION
FUNCTION).

Prefix sum(similar to cumulative distribution function) is equivalent to integral in
continuous domain, gives P(t < x).

We maintain a list of n + 1 buckets, each value represents the number of papers with citation
no less than its index.

But to maintain such inequality relation might involve O(N²) time complexity. To address that,
we can just maintain the count of equal values. Then the count of larger values is represented
by the reversed prefix sum from top down.

The special case is when value is larger than n, where we will increase buckets[n] by 1.

For each value c in citation list:
    if c >= n: buckets[n] += 1
    else: buckets[c] += 1

count(values larger than i) = ∑ count(values equal j) + count(values larger than n),
j in [i, n - 1]

And sweep down to cumulate the reversed prefix sum, representing count of larger values than
current index. Assume at some index i, we have buckets[i] >= i, then h = i.

'''

class Solution(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # return self.hIndexSort(citations)
        return self.hIndexBucket(citations)

    def hIndexSort(self, citations: list) -> int:
        citations.sort()
        h = len(citations)
        while h and citations[len(citations) - h] < h:
            h -= 1
        return h

    def hIndexBucket(self, citations: list) -> int:
        buckets_gt = [0] * (len(citations) + 1)
        for c in citations:
            buckets_gt[min(len(citations), c)] += 1
        sum_gt, h = buckets_gt[-1], len(citations)
        while h and sum_gt < h:
            h -= 1
            sum_gt += buckets_gt[h]
        print(buckets_gt, h)
        return h

def test():
    solution = Solution()

    assert solution.hIndex([]) == 0
    assert solution.hIndex([0, 1]) == 1
    assert solution.hIndex([3, 0, 6, 1, 5]) == 3

    print('self test passed')

if __name__ == '__main__':
    test()
