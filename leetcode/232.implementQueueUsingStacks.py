#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
232. Implement Queue using Stacks

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

Notes:
  You must use only standard operations of a stack -- which means only
push to top, peek/pop from top, size, and is empty operations are valid.
  Depending on your language, stack may not be supported natively. You may simulate a
stack by using a list or deque (double-ended queue), as long as you use only standard
operations of a stack.
  You may assume that all operations are valid (for example, no pop or peek operations
will be called on an empty queue).

==============================================================================================
SOLUTION

1. Naive solution
......

2. Two stacks for push and pop
Last in First Out and First in First Out are the only difference between queues and stacks.
And the difference in only kind of reverse process.

Of course, we need a stack 1 to support push method.

A stack reversed is a queue. Then we can use another stack 2 to serve the purpose of
First in First out supporting pop method.

Once we push an element, we just push it to the first stack. And when to pop, we dump
the elements from stack 1 to stack 2, then stack 2 pop() serves the function of queue pop().

Complexity: amortized O(1), O(n)

----------------------------------------------------------------------------------------------
Take away for augmenting data structures:
    1. Analyze the core operations' complexity and behavior of the target data structure
    2. Find corresponding common data structures to those operations with specific complexity
    3. Combine basic data structures!
'''

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_push = []
        self.stack_pop = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack_push.append(x)


    def _dump(self):
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self._dump()
        return self.stack_pop.pop()


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self._dump()
        return self.stack_pop[-1]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not (self.stack_push or self.stack_pop)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

def test():
    q = MyQueue()

    assert q.empty() is True
    q.push(1)
    assert q.peek() == 1
    assert q.empty() is False
    q.push(2)
    q.push(3)
    assert q.pop() == 1
    q.push(4)
    assert q.pop() == 2
    assert q.pop() == 3
    assert q.pop() == 4

    print("self test passed")

if __name__ == '__main__':
    test()
