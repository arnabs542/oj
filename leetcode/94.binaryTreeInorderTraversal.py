#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
94. Binary Tree Inorder Traversal

Total Accepted: 162943
Total Submissions: 377316
Difficulty: Medium
Contributors: Admin

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

==============================================================================================
SOLUTION:
    INORDER is different than PREORDER and POSTORDER in a way how we deal with GRAY VERTICES.
For inorder or postorder, just visit them before or after its descendants.

The real trouble with implementation is when to PUSH the right child.
Immediately when the root is discovered or when the POPPING and visiting the root vertex?
Both will do, just difference details.

1. Recursive solution

Complexity Analysis

Time complexity : O(n). The time complexity is O(n) because the recursive function is T(n) = 2*T(n/2)+1.

Space complexity : The worst case space required is O(n), and in the average case it's O(log(n)) where n is number of nodes.

2. Iterative solution with STACK
Same complexity.

3. Morris Traversal

'''

# Definition for a  binary tree node
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.visit = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # result =  self.inorderTraversalRecursive(root)
        # result =  self.inorderTraversalStackFrame(root)
        # result = self.inorderTraversalStack(root)
        # result = self.inorderTraversalStack2(root)
        result = self.inorderTraversalStackFrameSimplified(root)

        print(root, result)
        return result

    def inorderTraversalRecursive(self, root):
        """
        :type root: treenode
        :rtype: list[int]
        """
        visited = []
        def dfs(node):
            if not node: return
            dfs(node.left) # call, return address 1
            visited.append(node.val)
            dfs(node.right) # return address 2, not needed, current stack frame cleared

        dfs(root)

        return visited

    def inorderTraversalStackFrame(self, root):
        """
        :type root: treenode
        :rtype: list[int]

        Emulate the stack frame with explicit return address
        """
        visited = [] # return result
        stack = [(root, 0)] if root else []
        while stack:
            v, address = stack.pop()
            if not v: continue
            if address == 0:
                stack.append((v, address + 1)) # update RETURN ADDRESS
                if v.left: stack.append((v.left, 0)) # keep PUSHING stack
            elif address == 1: # POP. Trigger condition: above v.left is NULL
                visited.append(v.val)
                if v.right: stack.append((v.right, 0))
            # elif address == 2: pass
        return visited

    def inorderTraversalStackFrameSimplified(self, root):
        """
        :type root: treenode
        :rtype: list[int]

        Based on the stack frame implementation, the iterative procedure can be
        simplified to following implementations, according to the comments.

        Emulate the stack frame with implicit return address
        """
        visited = [] # return result
        # stack = [(root)] if root else []
        stack = []
        while stack or root:
            # root = stack.pop()
            while root:
                stack.append(root)
                root = root.left # have to push NULL nodes into stack, implicitly indicating return address
            if stack: # trigger condition: found a NULL v.left, return address 1
               root = stack.pop()
               visited.append(root.val)
               root = root.right

        return visited


    def inorderTraversalStack(self, root):
       """
       :type root: treenode
        :rtype: list[int]

        PUSH the right child when root is popped and visited.
       """
       visited = []
       stack = [root] if root else []
       while stack:
          vertex = stack.pop()
          # XXX: avoid duplicate PUSHING the same node, giving infinite loop
          if vertex:
             stack.append(vertex)
             stack.append(vertex.left) # keep pushing left child
          elif stack: # trigger condition: found a NULL v.left, return address 1
             # POP root vertex, because there is no left adjacent visited anymore
             vertex = stack.pop()
             visited.append(vertex.val)
             # XXX: and PUSH right visited AFTER finishing EXPLORING ROOT
             stack.append(vertex.right)

       return visited

    def inorderTraversalStack2(self, root):
        """
        :type root: treenode
        :rtype: list[int]

        PUSH the right child immediately when root is discovered.

        PUSH where we can, POP when there is no more to explore
        """
        visited = []
        stack = [root] if root else []
        while stack:
           vertex = stack.pop()
           if vertex:
               stack.append(vertex.right)
               stack.append(vertex)
               # PUSH left adjacent vertex
               stack.append(vertex.left)
           elif stack:
               # POP root vertex, because there is no left adjacent visited anymore
               vertex = stack.pop()
               visited.append(vertex.val)

        return visited

def test():

    # from _tree import Codec
    from _tree import Codec

    solution = Solution()

    root = Codec.deserialize("[]", int)
    assert solution.inorderTraversal(root) == []

    root = Codec.deserialize("[-3]", int)
    assert solution.inorderTraversal(root) == [-3]

    root = Codec.deserialize("[1,null,2,3]", int)
    assert solution.inorderTraversal(root) == [1, 3, 2]

    root = Codec.deserialize("[1,null,2,null,3,null,4,null,5]", int)
    assert solution.inorderTraversal(root) == [1, 2, 3, 4, 5]

    root = Codec.deserialize("[1,null,2,null,3,null,4,null,5]", int)
    assert solution.inorderTraversal(root) == [1, 2, 3, 4, 5]

    root = Codec.deserialize('[3,5,1,6,2,0,8,null,null,7,4]', int)
    assert solution.inorderTraversal(root) == [6, 5, 7, 2, 4, 3, 0, 1, 8]

    print('self test passed')

if __name__ == '__main__':
    test()
