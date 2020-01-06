#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
385. Mini Parser

Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

String is non-empty.
String does not contain white spaces.
String contains only digits 0-9, [, - ,, ].
Example 1:

Given s = "324",

You should return a NestedInteger object which contains a single integer 324.
Example 2:

Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.

==============================================================================================
SOLUTION

From the class methods of NestedInteger, we can see that the data type can only be initialized
when the object is initialized.

This is a typical problem revealing STACK structure, due to the NESTED structure.

1. Stack

2. Recursion

'''

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger(object):
    def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """
       if value is not None:
           self.setInteger(value)
       else:
           self.data = []
           self.dtype = 'list'


    def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """
       return self.dtype == 'int'

    def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """
       self.dtype = 'list'
       self.data.append(elem)

    def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """
       self.dtype = 'int'
       self.data = value

    def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """
       return self.data

    def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """
       return self.data

    def __repr__(self):
        if self.isInteger():
            return str(self.getInteger())
        else:
            childrenStr = []
            for ele in self.getList():
                childrenStr.append(str(ele))
            return '[' + ','.join(childrenStr) +  ']'

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        result = self.deserializeStack(s)
        print('result: ', result)
        return result

    def deserializeStack(self, s: str):
        # DONE: simplify
        stack = []
        result = None

        EOF = '\x00'
        buf = '' # input buffer
        s += EOF # end of line

        for i, c in enumerate(s):
            if '0' <= c <= '9' or c in ['-', '+']: # accumulate buffer
                buf += c
            elif c == '[': # stack PUSH
                newInt = NestedInteger()
                if stack:
                    stack[-1].add(newInt)
                stack.append(newInt)
            elif c in (',', ']', EOF): # stack POP, collect value
                if buf:
                    newInt = NestedInteger(int(buf))
                    if stack:
                        stack[-1].add(newInt)
                    buf = ''
                if c == ']':
                    result = stack and stack.pop()
                else:
                    result = result or newInt
                # print('stack:', stack)
            elif c.isspace():
                pass
            else:
                print("illegal input!")
                return result
            # print(stack, ' <- ', c)
        return result

# TODO: parse the number part of string in an inner loop

# TODO: recursive solution

def test():
    solution = Solution()

    assert str(solution.deserialize("[]")) == "[]"
    assert str(solution.deserialize("324")) == "324"
    assert str(solution.deserialize("[324]")) == "[324]"
    assert str(solution.deserialize("[123,[456,[789]]]")) == "[123,[456,[789]]]"
    assert str(solution.deserialize("[123,[456,[789],999]]")) == "[123,[456,[789],999]]"
    assert str(solution.deserialize("-3")) == "-3"
    assert str(solution.deserialize("[[[[[-3]]]]]")) == "[[[[[-3]]]]]"

    print("self test passed")

if __name__ == '__main__':
    test()
