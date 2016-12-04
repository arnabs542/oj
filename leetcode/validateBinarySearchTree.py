'''
98. Validate Binary Search Tree

Total Accepted: 117953
Total Submissions: 539812
Difficulty: Medium
Contributors: Admin

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

  1. The left subtree of a node contains only nodes with keys less than the node's key.
  2. The right subtree of a node contains only nodes with keys greater than the node's key.
  3. Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
'''

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isValidBST(self, root, low=float('-inf'), high=float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return not root or (low < root.val < high and
                            self.isValidBST(root.left, low=low, high=root.val) and
                            self.isValidBST(root.right, low=root.val, high=high))

from serializeAndDeserializeBinaryTree import Codec, TreeNode

def test():
    solution = Solution()

    assert solution.isValidBST(Codec.deserialize('[2,1,3]', int))

    print('self test passed')

if __name__ == '__main__':
    test()
