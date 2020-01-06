#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
225. Implement Stack using Queues

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.

Notes:
  You must use only standard operations of a queue -- which means only
push to back, peek/pop from front, size, and is empty operations are valid.
  Depending on your language, queue may not be supported natively. You may simulate a
queue by using a list or deque (double-ended queue), as long as you use only standard
operations of a queue.
  You may assume that all operations are valid (for example, no pop or top operations
will be called on an empty stack).

==============================================================================================
SOLUTION

1. Naive solution
1) With only one queue, emulate stack pop by popping out all elements except the last one,
and push them into the queue again!
Complexity: O(n) push, O(1) pop
or,
2) With two queues, keep the elements reversed every time a new element is pushed in.

Complexity: O(1) push, O(n) pop

2. Both O(1): nested structure/queue
Take a further thought, to emulate stack push, we push the new element to the front of the queue,
and push other elements after the new one. Copying all the previous elements takes O(N) time
complexity, can we eliminate that?

Why don't we treat all the previous elements as a whole element: a nested element which is a queue
composed of elements and nested structure/queue!

When we push a new element into the target data structure, we setup a new queue, and
push the new element to the front. Then, wrap the previous queue, which is already reversed, as a
nested queue, and push it after the new element.

For example, we push [1, 2, 3, 4, 5], and the data structure contains a queue containing:

    [5, [4, [3, [2, [1]]]]]

Note that stack illustrates nested structure again!

Complexity: O(1) push, O(1) pop
'''

class MyStackNaive(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        queue = []
        queue.append(x)
        while self.queue:
            queue.append(self.queue.pop(0))
        self.queue = queue

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.queue.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.queue


# DONE: faster algorithm
class MyStackNestedStructure(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        queue = []
        queue.append(x)
        queue.append(self._queue)
        self._queue = queue

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        top = self._queue.pop(0)
        self._queue = self._queue.pop() if self._queue else []
        return top

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self._queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self._queue


# MyStack = MyStackNaive
MyStack = MyStackNestedStructure



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

def test():
    stack = MyStack()

    assert stack.empty()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.empty() is False
    assert stack.pop() == 1

    print("self test passed")

if __name__ == '__main__':
    test()
