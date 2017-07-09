#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
155. Min Stack

Total Accepted: 101060
Total Submissions: 393319
Difficulty: Easy
Contributors: Admin

Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

    push(x) -- Push element x onto stack.

    pop() -- Removes the element on top of the stack.

    top() -- Get the top element.

    getMin() -- Retrieve the minimum element in the stack.

Example:

    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> Returns -3.
    minStack.pop();
    minStack.top();      --> Returns 0.
    minStack.getMin();   --> Returns -2.

==============================================================================================
SOLUTION

1. Use TWO STACKS.

This data structure supports all operations of stack, as well as getMin.
To meet the first requirement, we need a stack to store raw data.

The second requirement still needs the stack's behavior. Meanwhile, it have keep track of
the minimum element in the current frame.

Then we can use another stack, minStack, maintaining the minimum data (index) so far.

    If minStack stores the minimum data itself instead of indices, `minStack` must push the
new element as long as the new one is not smaller than the current minimum. While storing
indices, push into the `minStack` only if the new element is smaller than the current minimum.
'''

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dataStack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.dataStack.append(x)
        if not self.minStack or x < self.dataStack[self.minStack[-1]]:
            self.minStack.append(len(self.dataStack) - 1)

    def pop(self):
        """
        :rtype: void
        """
        if self.minStack[-1] == len(self.dataStack) - 1:
            self.minStack.pop()
        self.dataStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.dataStack[-1] if self.dataStack else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.dataStack[self.minStack[-1]] if self.minStack else None


def test():
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(2)
    obj.push(2)
    obj.pop()
    assert obj.getMin() == 2
    obj.pop()

    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    assert obj.getMin() == -3
    obj.pop()
    assert obj.top() == 0
    assert obj.getMin() == -2

    print('self test passed')

if __name__ == '__main__':
    test()
