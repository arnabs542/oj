#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
239. Sliding Window Maximum

Total Accepted: 43709
Total Submissions: 141493
Difficulty: Hard
Contributors: Admin

Given an array nums, there is a sliding window of size k which is moving from the very
left of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
    Could you solve it in linear time?

Hint:

    How about using a data structure such as deque (double-ended queue)?
    The queue size need not be the same as the window’s size.
    Remove redundant elements and the queue should store only elements that need to
be considered.

==============================================================================================
SOLUTION:
    This is a mathematical operation MAX POOLING in convolutional neural networks on
one dimension.

    A naive solution would be to find the maximum number in window each time the window
slides. The time complexity is O(NK), space complexity is O(1).

    The sliding window demonstrate characteristics of First In First Out, so QUEUE data
structure could be used.
    And again, this problems involves value COMPARISON, which is naturally related to value
ORDERING or SORTING.

1. Linear time complexity solution: MAX QUEUE using dequeue(double-ended queue) to do this.
A similar data structure is MIN STACK.

The double-ended queue stores the possible maximum candidates while the window slides. And the
queue's front element points to the maximum element in the window. When the window slides, the
window pops out an element and encounters a new element.

1) When the window pops out an element, if the element is the window maximum, the queue pops
out the front element. And the adjacent next element becomes the front element, the new window
maximum. So front element is larger than next element, otherwise, the front element is
not the maximum.
    One way to ensure that is to use max-heap, of which the DELETE time complexity is O(logK).
Another way to achieve that is to make sure the elements in the double-ended queue are of
Descending ORDER (MONOTONIC DECREASING).

2) When the window pushes an element in, it may become the window maximum later, so it will be
appended into the deque. However, to maintain the descending order, the smaller elements in
front of it must be all popped out.

Time Complexity Analysis:

1) The QUERY operation to get the maximum is of O(1)
2) The UPDATE operation to maintain the maximum dequeue is amortized to be O(1). Because the
worst case is when we need to pop all elements in the queue out when an large element is
pushed. But this won't happen all the time. Even if the list if composed of average m
descending subsequences with a maximum at last, like 213,546,768, the time complexity would be
O(complexity to update for each subsequence * number of such subsequences) = O(N/m * m) = O(N).
3) The DELETE operation is of O(1).
4) the CREATE operation is of O(k).
So the overall time complexity is O(k) + O(n - k) = O(n).

'''

from collections import deque

class Solution(object):

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return self.maxSlidingWindowDeque(nums, k)

    def maxSlidingWindowDeque(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        output = []
        maxQ = deque()
        for i, _ in enumerate(nums):
            if i >= k and nums[i - k] == maxQ[0]:
                maxQ.popleft()
            while maxQ and maxQ[-1] < nums[i]:
                maxQ.pop()
            maxQ.append(nums[i])
            if i >= k - 1:
                output.append(maxQ[0])
            pass
        print(output)
        return output

def test():
    solution = Solution()

    assert solution.maxSlidingWindow(
        [1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert solution.maxSlidingWindow(
        [1, 3, -3, -1, -4, 3, 6, 7], 3) == [3, 3, -1, 3, 6, 7]

    print('self test passed')

if __name__ == '__main__':
    test()
