'''
LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key
exists in the cache, otherwise return -1.

set(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the
least recently used item before inserting a new item.

SOLUTION:
    1. A LIST to maintain the least recently used property(least recently used is
at the end of list) with a HASH TABLE to store <key, item> for O(1) get operation.
    2. Builtin OrderedDict in Python.
'''

class LRUCacheItem(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.items = []
        self.table = dict()
        self.capacity = capacity

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.table:
            item = self.table[key]
            self.set(item.key, item.value)
            return item.value
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.table:
            # update value
            item = self.table[key]
            self.items.remove(item)
            item.value = value
        elif len(self.items) == self.capacity:
            # pop out and reuse the last item object
            item = self.items.pop()
            self.table.pop(item.key)
            item.key = key
            item.value = value
        else:
            # instanialize a new Item object
            item = LRUCacheItem(key, value)

        self.table[key] = item
        # insert at 0
        self.items.insert(0, item)


if __name__ == "__main__":
    c = LRUCache(1)
    c.set(2, 1)
    print('2', c.get(2))
    c.set(3, 2)
    print('2', c.get(2))
    print('3', c.get(3))
    print('2', c.get(2))

    c = LRUCache(10)

    c.set(10, 13)
    c.set(3, 17)
    c.set(6, 11)
    c.set(10, 5)
    c.set(9, 10)
    c.get(13)
    c.set(2, 19)
    c.get(2)
    c.get(3)
    c.set(5, 25)
    c.get(8)
    c.set(9, 22)
    c.set(5, 5)
    c.set(1, 30)
    c.get(11)
    c.set(9, 12)
    c.get(7)
    c.get(5)
    c.get(8)
    c.get(9)
    c.set(4, 30)
    c.set(9, 3)
    c.get(9)
    c.get(10)
    c.get(10)
    c.set(6, 14)
    c.set(3, 1)
    c.get(3)
    c.set(10, 11)
    c.get(8)
    c.set(2, 14)
    c.get(1)
    c.get(5)
    c.get(4)
    c.set(11, 4)
    c.set(12, 24)
    c.set(5, 18)
    c.get(13)
    c.set(7, 23)
    c.get(8)
    c.get(12)
    c.set(3, 27)
    c.set(2, 12)
    c.get(5)
    c.set(2, 9)
    c.set(13, 4)
    c.set(8, 18)
    c.set(1, 7)
    c.get(6)
    c.set(9, 29)
    c.set(8, 21)
    c.get(5)
    c.set(6, 30)
    c.set(1, 12)
    c.get(10)
    c.set(4, 15)
    c.set(7, 22)
    c.set(11, 26)
    c.set(8, 17)
    c.set(9, 29)
    c.get(5)
    c.set(3, 4)
    c.set(11, 30)
    c.get(12)
    c.set(4, 29)
    c.get(3)
    c.get(9)
    c.get(6)
    c.set(3, 4)
    c.get(1)
    c.get(10)
    c.set(3, 29)
    c.set(10, 28)
    c.set(1, 20)
    c.set(11, 13)
    c.get(3)
    c.set(3, 12)
    c.set(3, 8)
    c.set(10, 9)
    c.set(3, 26)
    c.get(8)
    c.get(7)
    c.get(5)
    c.set(13, 17)
    c.set(2, 27)
    c.set(11, 15)
    c.get(12)
    c.set(9, 19)
    c.set(2, 15)
    c.set(3, 16)
    c.get(1)
    c.set(12, 17)
    c.set(9, 1)
    c.set(6, 19)
    c.get(4)
    c.get(5)
    c.get(5)
    c.set(8, 1)
    c.set(11, 7)
    c.set(5, 2)
    c.set(9, 28)
    c.get(1)
    c.set(2, 2)
    c.set(7, 4)
    c.set(4, 22)
    c.set(7, 24)
    c.set(9, 26)
    c.set(13, 28)
    c.set(11, 26)
    for item in (c.items):
        print(item.key, item.value)
