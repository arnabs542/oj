#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, y):
        # return y.val == self.val and self.left == y.left and self.right == y.right
        return y.val == self.val

    def __lt__(self, y):
        return self.val is None or (not y is None) or self.val < y.val

    def __repr__(self):
        return 'val = {}'.format(self.val)


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '[{}, {}]'.format(self.start, self.end)

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

class DoublyLinkedListNode(object):
    def __init__(self, data):
        self.data = data
        self.prev = self
        self.next = self

    def __repr__(self):
        return str(self.data)

class CircularDoublyLinkedList(object):
    def __init__(self):
        self.head = DoublyLinkedListNode(None)
        self.head.prev = self.head.next = self.head # make circular!

    def insertAfter(self, node: DoublyLinkedListNode, p: DoublyLinkedListNode):
        """
        insert after
        update four pointers
        """
        p.prev = node
        p.next = node.next
        node.next = p
        p.next.prev = p

    def delete(self, p: DoublyLinkedListNode):
        assert p != self.head
        p.prev.next = p.next
        p.next.prev = p.prev

    def append(self, node: DoublyLinkedListNode):
        self.insertAfter(self.head.prev, node)

    def __repr__(self):
        p = self.head.next
        result = []
        while p and p != self.head:
            result.append(p.data)
            p = p.next
        return f'linkedlist{result}'

def testCircularLinkedList():
    container = CircularDoublyLinkedList()
    print(container)
    assert str(container) == 'linkedlist[]'

    container.insertAfter(container.head, DoublyLinkedListNode(1))
    print(container)
    assert str(container) == 'linkedlist[1]'
    container.delete(container.head.next)
    print(container)
    assert str(container) == 'linkedlist[]'

    container.insertAfter(container.head, DoublyLinkedListNode(1))
    container.append(DoublyLinkedListNode(2)) # append
    print(container)
    assert str(container) == 'linkedlist[1, 2]'

def test():
    testCircularLinkedList()

    pass

if __name__ == "__main__":
    test()
