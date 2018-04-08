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

================================================================================
SOLUTION

To support get, set, delete in O(1), a hash table is the key. But the problem
still wants to delete a least recently used item.

1. Naive solution - add another state - time stamp
Use a hash table to enable O(1) time complexity of get and set.
Should keep the value stored with time stamp when it's used.

Complexity: To invalidate least recently used item, it takes O(n) time complexity.
O(1) for other operations.

--------------------------------------------------------------------------------
AUGMENT DATA STRUCTURES.

Key idea: hash table, ordered data structure.

To achieve O(1) complexity insert/search/delete operation, a HASH TABLE will do.

The problem is to delete an item meeting a certain condition: least recently used.

Adding a STATE time stamp to the items will solve the problem, with O(n) time for
LINEAR SEARCH.

One intuition to avoid linear search is to keep the data ORDERED, making it possible
to utilize more efficient searching algorithms:
    binary search for any item, O(1) search for extrema item.

To maintain an ordered relation, we have multiple data structures:
    array, linked list, trees, ...
The problem with array is that it takes O(n) to insert/delete.
And a tree usually has amortized O(logn) complexity for insert/search/delete.

Now, a LINKED LIST comes in handy, supporting O(1) insert/delete.


--------------------------------------------------------------------------------

2. Ordered map storing value with time stamp

- balancing binary search tree
Time complexity for all operations are: O(logN)

- doubly linked list with hash table
Complexity: O(1) for all

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

4. Hash table with a linked list as ordered data structure

The above problem is still with the delete operation, or invalidate.

A single hash table won't do the job, it needed to be augmented.

Brainstorm: array, linked list, queue/stack, set, hash table, heap, tree, graph, ...
Among all these data structures, linked list supports insert and delete pretty easy.

The idea is, every time an item is used, move it to one end of linked list.

Under such algorithm, the data is ordered by recently used time.

4.1) Doubly linked list
Using doubly linked list, deleting and reordering is of O(1) complexity.

To support O(1) query operation, use the hash table the maintain the mapping from
key to the corresponding linked list node.

Complexity: O(1), O(1)

4.2) Singly linked list with a hash table

Using a singly linked list involves two more problems than doubly linked list.
1) How to delete any node in O(1) time complexity
Copy and replace with next node!
Remember the edge case: moving the tail node to tail.

2) Where to put the least recently used pair?
Put/sink LRU item at the head, not the tail. Because it's not possible to delete tail element in O(1)
while updating the tail node pointer.

Complexity: O(1) in both get and put

'''

from _type import ListNode
from collections import OrderedDict
# from _utils import tolist

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        raise Exception("Not implemented")


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        raise Exception("Not implemented")


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        raise Exception("Not implemented")

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

class LRUCacheSinglyLinkedListAndHashTable():
    # DONE: test it
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

        self.listHead = ListNode(0) # node val: (key, value)
        self.listTail = self.listHead
        self.map = {} # key to linked list node

    def _move2Tail(self, node: ListNode) -> ListNode:
        if not node or node == self.listTail: return node
        p = node.next
        # print("head: ", self.listHead)
        # print('move to tail: ', node, p, self.listTail)
        # print("before moving: ", "map: ", self.map)

        nodeCopy = ListNode(node.val) # copy current value
        # copy next value to current node
        node.val = p.val
        # delete next node
        node.next = p.next

        # update references to next node
        self.map[p.val[0]] = node
        # update tail pointer
        if self.listTail == p:
            self.listTail = node

        # append to tail
        self.listTail.next = nodeCopy
        self.listTail = nodeCopy

        self.map[nodeCopy.val[0]] = nodeCopy

        # print('after moving: ', tolist(self.listHead), 'map: ',
              # self.map)

        return nodeCopy

    def _deleteHead(self):
        # print("deleting the first node, a.k.a least recently used item", self.listHead.next)
        # delete map k
        p = self.listHead.next
        if p:
            del self.map[p.val[0]]
        else:
            return

        # delete the node in linked list
        self.listHead.next = p.next
        p.next = None

        if p == self.listTail:
            self.listTail = self.listHead

    def put(self, k, v):
        """
        :type key: int
        :rtype: int
        """
        # print("put: ", k, v)
        if k in self.map:
            # print("updating existing key to value: ", k, v)
            self.map[k].val = (k, v)
            # self.map[k] = self._move2Tail(self.map[k])
            self._move2Tail(self.map[k])
        else:
            if len(self.map) >= self.capacity:
                self._deleteHead()
            self.map[k] = ListNode((k, v))

            # append to tail
            self.listTail.next = self.map[k]
            # update tail
            self.listTail = self.map[k]

        # print('data: ', tolist(self.listHead), 'new: ', k, v,
              # 'map: ', self.map)

    def get(self, k):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # print("get: ", k)
        if k not in self.map:
            return -1
        v = self.map[k].val[1]

        # refresh cache
        # self.map[k] = self._move2Tail(self.map[k])
        self._move2Tail(self.map[k])
        # print('data: ', tolist(self.listHead), 'new: ',
              # 'map: ', self.map)

        return v


# TODO: implement hash table + doubly linked list solution
# refer to functools.lru_cache for hash table + circular doubly linked list implementation
class LRUCacheDoublyLinkedListAndHashTable:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.orderedDict = OrderedDict()


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

    # LRUCache = LRUCacheArrayList
    # LRUCache = LRUCacheLinkedListAndHashTable
    LRUCache = LRUCacheSinglyLinkedListAndHashTable

    c = LRUCache(1)

    c.put(2, 1)
    assert c.get(2) == 1
    c.put(3, 2)
    assert (c.get(2)) == -1
    assert (c.get(3)) == 2
    assert (c.get(2)) == -1


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
    assert c.get(5) == 5
    c.put(1, 30)
    assert c.get(1) == 30
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
    # for item in (c.items):
        # print(item.key, item.value)

    print("self test passed!")
