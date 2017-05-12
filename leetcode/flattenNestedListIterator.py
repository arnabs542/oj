#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
341. Flatten Nested List Iterator

Total Accepted: 34053
Total Submissions: 84320
Difficulty: Medium
Contributor: LeetCode

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers
or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned
by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned
by next should be: [1,4,6].


==============================================================================================
SOLUTION

1. Nested means RECURSION, while recursion is naturally bounded with STACK data structure.

Keep pushing the first element of the current list into the stack while current element is
a list. If it's not, pop out the first element of current list in the stack.

Because the problem is to implement an iterator, so we must have full control over the
searching process. Thus, we cannot use recursion. Instead, we have to implement the
algorithm with iteration by emulating recursion with stack.

'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):

    def __init__(self):
        self._number = None
        self._list = None

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = nestedList
        self.stack = None
        self.cache = None

    def next(self):
        """
        :rtype: int
        """
        cache = self.cache if self.cache is not None else self._next()
        self.cache = None
        return cache

    def hasNext(self):
        """
        :rtype: bool
        """
        self.cache = self.cache or self._next()
        return self.cache is not None

    def _next(self):
        self.cache = None
        # return self._nextNaive()
        return self._nextOpt()

    def _nextNaive(self):
        '''
        Naive implementation using list.pop(0), which is of O(N) time complexity.
        '''
        if not (self.nestedList or self.stack):
            return None
        # push
        self.stack = self.stack or [self.nestedList.pop(0)]
        while self.stack and isinstance(
                self.stack[-1], list) and self.stack[-1]:
            self.stack.append(self.stack[-1].pop(0))
        self.cache = self.stack[-1] if self.stack and isinstance(self.stack[-1], int) else None
        # pop
        self.stack.pop()
        while self.stack and isinstance(
                self.stack[-1], list) and not self.stack[-1]:
            self.stack.pop()

        if self.cache is None:
            self.cache = self._next()

        return self.cache

    def _nextOpt(self):
        '''
        Avoid using list.pop(0) by adding index to the stack frame state.

        Define state as a tuple:
            (nested element, iterating index of the nested list element)
        '''
        if not (self.nestedList or self.stack):
            return
        self.stack = self.stack or [(self.nestedList, 0)]
        # push
        while self.stack and isinstance(self.stack[-1][0], list):
            ele, index = self.stack.pop()
            if index >= len(ele):
                continue
            self.stack.append((ele, index + 1))
            self.stack.append((ele[index], 0))

        if self.stack:
            ele, index = self.stack.pop()
            self.cache = ele

        return self.cache

    def _nextNaiveSubmit(self):
        if not (self.nestedList or self.stack):
            return None
        # push
        self.stack = self.stack or [self.nestedList.pop(0)]
        while self.stack and not self.stack[-1].isInteger() and self.stack[-1].getList():
            self.stack.append(self.stack[-1].getList().pop(0))
        self.cache = self.stack[-1].getInteger() if self.stack and self.stack[-1].isInteger() else None
        # pop
        self.stack.pop()
        while self.stack and not self.stack[-1].isInteger() and not self.stack[-1].getList():
            self.stack.pop()

        if self.cache is None:
            self.cache = self._next()

        return self.cache

    def _nextOptSubmit(self):
        '''
        Avoid using list.pop(0) by adding index to the stack frame state.

        Define state as a tuple:
            (nested element, iterating index of the nested list element)
        '''
        if not (self.nestedList or self.stack):
            return
        self.stack = self.stack or [(self.nestedList, 0)]
        # push
        while self.stack and isinstance(self.stack[-1][0], list):
            ele, index = self.stack.pop()
            if index >= len(ele):
                continue
            self.stack.append((ele, index + 1))
            self.stack.append((ele[index] if ele[index].isInteger() else ele[index].getList(), 0))

        if self.stack:
            ele, index = self.stack.pop()
            self.cache = ele.getInteger()

        return self.cache


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

def test():
    # empty list
    nestedList = []
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())
    print(v)
    assert v == []

    nestedList = [0]
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())
    print(v)
    assert v == [0]

    nestedList = [0, 1]
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())
    print(v)
    assert v == [0, 1]

    # empty nested list
    nestedList = [[[]]]
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())
    print(v)
    assert v == []

    # nested empty, non-empty
    nestedList = [[[]], [1]]
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())
    print(v)
    assert v == [1]

    nestedList = [[1, 1], 2, [1, 1]]
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())
    print(v)
    assert v == [1, 1, 2, 1, 1]

    nestedList = [1, [4, [6]]]
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())
    print(v)
    assert v == [1, 4, 6]

    nestedList = [1, [[[]]], [2, [3]], [[4], 5, [[6], 7]], [[[]]], [8]]
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())
    print(v)
    assert v == [1, 2, 3, 4, 5, 6, 7, 8]

    print("All tests passed")

if __name__ == '__main__':
    test()
