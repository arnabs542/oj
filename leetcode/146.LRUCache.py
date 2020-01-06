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

1. Naive solution - single hash table: add another state - time stamp
Use a hash table to enable O(1) time complexity of get and set.
Should keep the value stored with time stamp when it's used.

Complexity: To invalidate least recently used item, it takes O(n) time complexity.
O(1) for other operations.

2. Single array/list

Of course, it's bad idea.

--------------------------------------------------------------------------------
AUGMENT DATA STRUCTURES.

Naive augmented data structures.
--------------------------------------------------------------------------------

3. Array and a hash table - bad idea!
An array to maintain the least recently used property(least recently used is
at the end of list) with a HASH TABLE to store <key, item> for O(1) get operation.

Complexity:
get - O(n)
set - O(n)
invalidate - O(n)

4. Self balancing binary search tree implemented key value data structure
Time complexity for all operations are: O(logN)

--------------------------------------------------------------------------------
More efficient augmented data structure

Requirements
------------
Key idea: O(1) insert/query for all elements, O(1) delete for a specific element.

Related basic data structure: hash table, ordered data structure.

To achieve O(1) complexity insert/search/delete operation, a HASH TABLE will do.

Problem
-------
To DELETE an item with certain QUERY condition - least recently used in O(1).

Naive augmentation: add another state
-------------------
Adding a STATE time stamp to the hash table items will solve the problem,
with O(n) time for LINEAR SEARCH.

Better augmentation: combine hash table with linked list
------------
One intuition to avoid linear search is to keep the data ORDERED, making it possible
to utilize more efficient searching algorithms:
    binary search for any item, O(1) search for extrema item.

To maintain an ORDERED relation, we brainstorm data structures:
    array, linked list, queue/stack, set, hash table, heap, tree, graph, ...

The problem with array is that it takes O(n) to insert/delete.
And a tree usually has amortized O(logn) complexity for insert/search/delete.
Among all these data structures, linked list supports insert and delete in O(1).

Augment hash table with linked list:
    supports O(1) insert/delete/query for all elements.

See below.
--------------------------------------------------------------------------------

5. Ordered key value data structure by HASH TABLE AND LINKED LIST

Implicit representation of least recently used
-------------------------------------
A least recently used item can't be directly tracked(not accessed at all),
but its COMPLEMENT can be tracked easily:
    it's easy to track which items are used recently!

The idea is, every time an item is used, move it to one end of linked list.

Under such algorithm, the data is ordered by recently used time.

4.1) Doubly linked list
Using doubly linked list, deleting and reordering is of O(1) complexity.

Insert at the end, delete at the beginning of the linked list.

To support O(1) query operation, use the hash table the maintain the mapping from
key to the corresponding linked list node.

Complexity: O(1), O(1)

4.2) Singly linked list with a hash table

Using a singly linked list involves two more problems than doubly linked list.
1) How to delete any node in O(1) time complexity
Copy and replace with next node!
Remember the edge case: moving the tail node to tail.

2) Where to put the least recently used pair?

Put/sink LRU item at the head, not the tail.
Because it's not possible to delete tail element in O(1) while updating the tail node pointer.

Complexity: O(1) in both get and put

Representation
--------------
Hash table: key to linked list node

Linked list: each node must have linked list pointers plus key and value.
Storing key in node is to retrieve corresponding hash table key when deleting
element from the end of the linked list.

4.3) use builtin ordered hash table implementation: OrderedDict.

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


# DONE: implement hash table + circular doubly linked list
# refer to functools.lru_cache for hash table + circular doubly linked list implementation

_PREV, _NEXT, _KEY, _VALUE = 0, 1, 2, 3   # names for the link fields
class LRUCacheDoublyLinkedListAndHashTable:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        head = [] # circular doubly linked list head
        head[:] = [head, head, None, None] # self referencing: previous, next, key, value
        self._head = head
        assert id(self._head) == id(head)
        self._map = {} # hash table

        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self._map:
            return -1

        p = self._map[key]
        # DONE: delete and insert
        self._delete(key)
        self.put(key, p[_VALUE])

        return p[_VALUE]

    def _delete(self, key):
        if key is None: # empty yet
            return
        p = self._map[key]
        # delete in linked list
        p[_PREV][_NEXT] = p[_NEXT]
        p[_NEXT][_PREV] = p[_PREV]
        # delete in hash table
        del self._map[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self._map:
            # DONE: already exist, update: delete & insert later
            self._delete(key)
        elif len(self._map) >= self.capacity:
            # DONE: delete the beginning element
            self._delete(self._head[_NEXT][_KEY])

        # DONE: insert at end of linked list
        node = [self._head[_PREV], self._head, key, value]
        # print(self._head, node)
        self._head[_PREV] = node
        node[_PREV][_NEXT] = node
        self._map[key] = node

from _type import CircularDoublyLinkedList, DoublyLinkedListNode
class LRUCacheDoublyLinkedListAndHashTableOpt:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._map = {}
        self._list = CircularDoublyLinkedList()
        self.capacity = capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self._map:
            return -1
        print(self._list)
        p = self._map[key]
        self._list.delete(p)
        self._list.insertAfter(self._list.head, p)

        return p.data[1]


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self._map:
            p = self._map[key]
            p.data[1] = value
            self._list.delete(p)
            self._list.insertAfter(self._list.head, p)
            return
        elif max(1, self.capacity) <= len(self._map):
            p = self._list.head.prev
            self._list.delete(p)
            del self._map[p.data[0]]

        if len(self._map) + 1 > self.capacity:
            return

        p = DoublyLinkedListNode([key, value])
        self._map[key] = p
        self._list.insertAfter(self._list.head, p)


if __name__ == "__main__":

    # LRUCache = LRUCacheArrayList
    # LRUCache = LRUCacheLinkedListAndHashTable
    # LRUCache = LRUCacheSinglyLinkedListAndHashTable
    # LRUCache = LRUCacheDoublyLinkedListAndHashTable
    LRUCache = LRUCacheDoublyLinkedListAndHashTableOpt

    c = LRUCache(1)
    c.put(2, 1)
    assert c.get(2) == 1
    c.put(3, 2)
    assert (c.get(2)) == -1
    assert (c.get(3)) == 2
    assert (c.get(2)) == -1

    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)
    # assert len(c._map) == 2
    assert c.get(2) == -1
    c.put(4, 4)
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4

    c = LRUCache(2)
    assert c.get(2) == -1
    c.put(2, 6)
    assert c.get(1) == -1
    c.put(1, 5)
    c.put(1, 2)
    # print(c.get(1))
    assert c.get(1) == 2
    # print('\nmap: ', c._map)
    assert c.get(2) == 6
# ["LRUCache","get","put","get","put","put","get","get"]
# [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
# [null,-1,null,-1,null,null,2,6]

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
