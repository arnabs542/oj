#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
406. Queue Reconstruction by Height

Total Accepted: 8375
Total Submissions: 15557
Difficulty: Medium
Contributors: Admin

Suppose you have a random list of people standing in a queue. Each person is described
by a pair of integers (h, k), where h is the height of the person and k is the number
of people in front of this person who have a height greater than or equal to h. Write
an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

==============================================================================================
SOLUTION:
    brute-force, greedy.
Hint: sometimes, greedy strategy is closely connected to sort to make local optimal decision.
'''

class Solution(object):

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        return self.reconstructQueueByHeight(people)

    def reconstructQueueNaive(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]

        At each round, find the most front one that can be appended into the queue
        """
        # FIXME: time limit exceeded
        queue = []

        def canInsert(person):
            num_higher = 0
            for front in queue:
                if front[0] >= person[0]:
                    num_higher += 1
            return num_higher == person[1]

        while people:
            print(queue, '<=====', people)
            next_person = None
            for i, person in enumerate(people):
                if canInsert(person) and (
                        next_person is None or person < people[next_person]):
                    next_person = i
                pass
            if next_person is not None:
                queue.append(people.pop(next_person))
            else:
                break

        return queue

    def reconstructQueueByHeight(self, people: list):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]

        Because in tuple (h, k), k is only affected by people in front of him that are of
        greater or equal height, inserting people with smaller height won't interfere its
        validity. Then we can reconstruct the queue in a descending order of height to reduce
        the time complexity when finding the next person to insert.
        """
        queue = []
        people.sort(key=lambda x: (-x[0], x[1]))
        for p in people:
            queue.insert(p[1], p)
        return queue


def test():
    solution = Solution()
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    assert solution.reconstructQueue(people)
    assert solution.reconstructQueue([]) == []

    print('self test passed')

test()