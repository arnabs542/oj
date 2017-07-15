#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
380. Insert Delete GetRandom O(1)

Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the
same probability of being returned.

Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();

==============================================================================================
SOLUTION

1) Inverted index

To insert and delete in O(1) time complexity, a hash table will do. But, to achieve random
access in O(1) time, a linear array is best. So, maybe there is a way to combine these two
data structures together, just like 'minStack.py' problem.

Use a list to store the actual data, and use a hash table to store the inverted indices --
mapping from content to its locations.

This idea is similar to inverted index(https://en.wikipedia.org/wiki/Inverted_index)

'''

# TODO: follow up for supporting duplicate numbers?

import random


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dataList = []
        self.dataDict = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the
        specified element.

        :type val: int
        :rtype: bool
        """
        if val not in self.dataDict:
            if len(self.dataList) > len(self.dataDict):
                self.dataList[len(self.dataDict)] = val
                self.dataDict[val] = len(self.dataDict)
            else:
                self.dataList.append(val)
                self.dataDict[val] = len(self.dataList) - 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dataDict:
            tail = len(self.dataDict) - 1
            idx = self.dataDict[val]
            # self.dataList[idx] = float('-inf')
            # XXX: remove element by swapping it to the rear of the list
            # XXX: update the position mapping
            self.dataDict[self.dataList[tail]] = idx
            self.dataList[idx], self.dataList[
                tail] = self.dataList[tail], self.dataList[idx]
            del self.dataDict[val]
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.dataDict:
            idx = random.randint(0, len(self.dataDict) - 1)
            return self.dataList[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

def test():
    randomSet = RandomizedSet()
    # Inserts 1 to the set. Returns true as 1 was inserted successfully.
    assert randomSet.insert(1)

    # Returns false as 2 does not exist in the set.
    assert not randomSet.remove(2)

    # Inserts 2 to the set, returns true. Set now contains [1,2].
    assert randomSet.insert(2)

    # getRandom should return either 1 or 2 randomly.
    assert randomSet.getRandom() in (1, 2)

    # Removes 1 from the set, returns true. Set now contains [2].
    assert randomSet.remove(1)

    # 2 was already in the set, so return false.
    assert not randomSet.insert(2)

    # Since 2 is the only number in the set, getRandom always return 2.
    assert randomSet.getRandom() == 2

    # case 2
    randomSet = RandomizedSet()
    assert randomSet.insert(0)
    assert randomSet.insert(1)
    assert randomSet.remove(0)
    assert randomSet.insert(2)
    assert randomSet.remove(1)
    assert randomSet.getRandom() == 2

    print("self self test passed")


if __name__ == '__main__':
    test()
