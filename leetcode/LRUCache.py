'''
146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key
exists in the cache, otherwise return -1.

set(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the
least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

==============================================================================================
SOLUTION

To support get, set, delete in O(1), a hash table is the key. But the problem still wants to
delete a least recently used item.

1. Naive solution - with time stamp
Use a hash table to enable O(1) time complexity of get and set.
Should keep the value stored with time stamp when it's used.

Complexity: To invalidate least recently used item, it takes O(n) time complexity.
O(1) for other operations.

2. Ordered map(balancing binary search tree) storing value with time stamp

Time complexity for all operations are: O(logN)

----------------------------------------------------------------------------------------------
AUGMENT DATA STRUCTURES.

3. Array
A LIST to maintain the least recently used property(least recently used is
at the end of list) with a HASH TABLE to store <key, item> for O(1) get operation.

Complexity:
get - O(1)
set - O(1)
invalidate - O(n)

This is still a bad idea

A least recently used item can't be directly tracked, but its complement can be tracked
easily: it's easy to know which items are used recently!

4. Doubly linked list with a hash table
The above problem is still with the delete operation, or invalidate.

A single hash table won't do the job, it needed to be augmented. There aren't many
data structures.

Brainstorm: array, linked list, queue/stack, set, hash table, heap, tree, graph, ...
Among all these data structures, linked list supports insert and delete pretty easy.

The idea is, every time an item is used, we remove it from the linked list, and insert
it at the first position of linked list. Using doubly linked list, this is O(1) complexity.

To support O(1) query operation, use the hash table the maintain the mapping from
key to the corresponding linked list node.


'''

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

class LRUCacheItem(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value

class LRUCacheArrayList(object):

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
            self.put(item.key, item.value)
            return item.value
        else:
            return -1

    def put(self, key, value):
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


# TODO: implement hash table + doubly linked list solution
class LRUCacheLinkedListAndHashTable:

    def __init__(self, capacity):
        """
        :type capacity: int
        """


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

if __name__ == "__main__":

    LRUCache = LRUCacheArrayList
    # LRUCache = LRUCacheLinkedListAndHashTable

    c = LRUCache(1)

    c.put(2, 1)
    print('2', c.get(2))
    c.put(3, 2)
    print('2', c.get(2))
    print('3', c.get(3))
    print('2', c.get(2))

    c = LRUCache(10)

    c.put(10, 13)
    c.put(3, 17)
    c.put(6, 11)
    c.put(10, 5)
    c.put(9, 10)
    c.get(13)
    c.put(2, 19)
    c.get(2)
    c.get(3)
    c.put(5, 25)
    c.get(8)
    c.put(9, 22)
    c.put(5, 5)
    c.put(1, 30)
    c.get(11)
    c.put(9, 12)
    c.get(7)
    c.get(5)
    c.get(8)
    c.get(9)
    c.put(4, 30)
    c.put(9, 3)
    c.get(9)
    c.get(10)
    c.get(10)
    c.put(6, 14)
    c.put(3, 1)
    c.get(3)
    c.put(10, 11)
    c.get(8)
    c.put(2, 14)
    c.get(1)
    c.get(5)
    c.get(4)
    c.put(11, 4)
    c.put(12, 24)
    c.put(5, 18)
    c.get(13)
    c.put(7, 23)
    c.get(8)
    c.get(12)
    c.put(3, 27)
    c.put(2, 12)
    c.get(5)
    c.put(2, 9)
    c.put(13, 4)
    c.put(8, 18)
    c.put(1, 7)
    c.get(6)
    c.put(9, 29)
    c.put(8, 21)
    c.get(5)
    c.put(6, 30)
    c.put(1, 12)
    c.get(10)
    c.put(4, 15)
    c.put(7, 22)
    c.put(11, 26)
    c.put(8, 17)
    c.put(9, 29)
    c.get(5)
    c.put(3, 4)
    c.put(11, 30)
    c.get(12)
    c.put(4, 29)
    c.get(3)
    c.get(9)
    c.get(6)
    c.put(3, 4)
    c.get(1)
    c.get(10)
    c.put(3, 29)
    c.put(10, 28)
    c.put(1, 20)
    c.put(11, 13)
    c.get(3)
    c.put(3, 12)
    c.put(3, 8)
    c.put(10, 9)
    c.put(3, 26)
    c.get(8)
    c.get(7)
    c.get(5)
    c.put(13, 17)
    c.put(2, 27)
    c.put(11, 15)
    c.get(12)
    c.put(9, 19)
    c.put(2, 15)
    c.put(3, 16)
    c.get(1)
    c.put(12, 17)
    c.put(9, 1)
    c.put(6, 19)
    c.get(4)
    c.get(5)
    c.get(5)
    c.put(8, 1)
    c.put(11, 7)
    c.put(5, 2)
    c.put(9, 28)
    c.get(1)
    c.put(2, 2)
    c.put(7, 4)
    c.put(4, 22)
    c.put(7, 24)
    c.put(9, 26)
    c.put(13, 28)
    c.put(11, 26)
    for item in (c.items):
        print(item.key, item.value)
