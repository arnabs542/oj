# -*- coding:utf-8 -*-

'''
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?

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

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # return self.preorderTraversalRecursive(root)
        return self.preorderTraversalStack(root)

    def preorderTraversalRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is not None:
            self.visit.append(root.val)
            if root.left is not None:
                self.preorderTraversal(root.left)
            if root.right is not None:
                self.preorderTraversal(root.right)

        return self.visit

    # TODO: iterative solution
    def preorderTraversalStack(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        vertices = []
        stack = [root] if root else []
        while stack:
            vertex = stack.pop()
            vertices.append(vertex.val)
            for child in (vertex.right, vertex.left):
                if child:
                    stack.append(child)

        return vertices

def test():

    from _tree import Codec

    solution = Solution()

    root = Codec.deserialize("[]", int)
    assert solution.preorderTraversal(root) == []

    root = Codec.deserialize("[-3]", int)
    assert solution.preorderTraversal(root) == [-3]

    root = Codec.deserialize("[1,null,2,3]", int)
    assert solution.preorderTraversal(root) == [1, 2, 3]

    root = Codec.deserialize("[1,2,null,3,null,4,null,5]", int)
    assert solution.preorderTraversal(root) == [1, 2, 3, 4, 5]

    root = Codec.deserialize("[1,null,2,null,3,null,4,null,5]", int)
    assert solution.preorderTraversal(root) == [1, 2, 3, 4, 5]

    root = Codec.deserialize('[3,5,1,6,2,0,8,null,null,7,4]', int)
    assert solution.preorderTraversal(root)

    print('self test passed')

if __name__ == '__main__':
    test()
