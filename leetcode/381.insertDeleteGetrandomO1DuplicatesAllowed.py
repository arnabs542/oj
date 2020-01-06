#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

381. Insert Delete GetRandom O(1) - Duplicates allowed

Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. The probability of
each element being returned is linearly related to the number of same value the collection contains.

Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection
// now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();

==============================================================================================
SOLUTION

This is a follow up with duplicates allowed.

1) Inverted index

For RANDOM ACCESS, we still need a data LIST to store the actual elements, same as before.

For INSERT AND DELETE in O(1) time complexity, use a HASH TABLE to maintain the mapping
relation from value to its locations within the data list(a.k.a inverted index). Because a
value may be stored in multiple locations, we will map the value to a collection of indices
where the same values are located in the data list.

To remove a value, we have to avoid the O(N) list pop operation. And, instead, replace that
value with the tail value and remove the tail node of the list in O(1) time complexity.

Since we move the last value to a new location, we need to update its corresponding inverted
indices in hash table. Then to retrieve that index must be O(1) time complexity. Given this,
a location set instead of location list will give solve the index retrieval complexity problem.

To sum it up, we have to data structures:
    1) data list: dataList
    2) data hash table (dictionary): dataDict

The key of dataDict is the val, the value of dataDict is the set of indices of where val appears
in dataList. Each element of dataList is the val.

2) Improved inverted index: double/bidirectional indexing
Above solution uses a set as indices collection. We can improve its performance by using a list.

There are two data structures:
    1) a vector nums
    2) an unordered_map m

The key of m is the val, the value of m is a vector contains indices where the val appears in nums.
Each element of nums is a pair, the first element of the pair is val itself, the second element
of the pair is an index into m[val].

There is a relationship between nums and m:
    m[nums[i].first][nums[i].second] == i;

'''

import random


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dataList = []
        self.dataDict = {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already
        contain the specified element.

        :type val: int
        :rtype: bool
        """
        exist = True
        if not (val in self.dataDict and self.dataDict[val]):
            self.dataDict.setdefault(val, set())
            exist = False
        self.dataDict[val].add(len(self.dataList))
        self.dataList.append(val)
        return not exist

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained
        the specified element.

        :type val: int
        :rtype: bool
        """
        # no such key or empty location set
        if not (val in self.dataDict and self.dataDict[val]):
            return False
        # print(self.dataDict, self.dataList)
        idx = self.dataDict[val].pop()
        tail = len(self.dataList) - 1

        # move the deleted element to the rear of data list, and pop it out
        # XXX: corner case when idx == tail
        if tail != idx:
            self.dataDict[self.dataList[tail]].remove(tail)
            self.dataDict[self.dataList[tail]].add(idx)

            self.dataList[idx], self.dataList[
                tail] = self.dataList[tail], self.dataList[idx]
        self.dataList.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        if not self.dataList:
            return None
        idx = random.randint(0, len(self.dataList) - 1)
        return self.dataList[idx]

# TODO: indices list instead of set, with bidirectional indexing

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

def test():

    # Init an empty collection.
    collection: RandomizedCollection = RandomizedCollection()

    # Inserts 1 to the collection. Returns true as the collection did not
    # contain 1.
    assert collection.insert(1)

    # Inserts another 1 to the collection. Returns false as the collection contained 1. Collection
    # now contains [1,1].
    assert collection.insert(1) is False

    # Inserts 2 to the collection, returns true. Collection now contains
    # [1,1,2].
    assert collection.insert(2)

    # getRandom should return 1 with the probability 2/3, and returns 2 with
    # the probability 1/3.
    assert collection.getRandom() in (1, 2)

    # Removes 1 from the collection, returns true. Collection now contains
    # [1,2].
    assert collection.remove(1)

    # getRandom should return 1 and 2 both equally likely.
    assert collection.getRandom() in (1, 2)

    ################ case 2
    collection = RandomizedCollection()
    assert collection.insert(1)
    assert collection.remove(1)
    assert collection.insert(1)


    ################ case 3
    collection = RandomizedCollection()

    assert collection.remove(9) is False

    assert collection.insert(0)
    assert collection.remove(0)
    assert collection.insert(-1)
    assert collection.remove(0) is False
    assert collection.getRandom() == -1
    assert collection.getRandom() == -1
    assert collection.getRandom() == -1
    assert collection.getRandom() == -1
    assert collection.getRandom() == -1
    assert collection.remove(-1)
    assert collection.getRandom() is None
    assert collection.insert(0)

    print("self test passed")

if __name__ == '__main__':
    test()
