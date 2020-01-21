#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
652. Find Duplicate Subtrees
Medium

Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:
      2
     /
    4
and
    4
Therefore, you need to return above trees' root in the form of a list.

================================================================================
SOLUTION

The problem is how to represent a tree for identification uniquely?
SERIALIZE the tree to string representation or integer id! This is like hashing.
What kind of traversal order should we utilize to serialize tree?

In order solution will fail for the following:

0
/
0
and
0
\
0

as both will be treated as #0#0#.
Then we can differentiate left and right NULL nodes:
- Use different tokens to differentiate left and right NULL nodes respectively: '(0)0)' vs '(0(0)'
- Wrap in parentheses to conclude a subtree: "(left,root,right)"
- Append separator: "left,root,right,"

1. Brute force - traverse and verify - check subtree is identical to another tree
Exhaust all subtrees, and check for duplicate.

Complexity: O(N³)

2. Hash count - dfs - direct string serialization of tree

Find duplicates? Hash count!

Traverse the tree, hash all subtree serialization. Then we can check duplicate
in one pass.

Use the hash table to store mapping <subtree serialization, root node>

Recurrence relation:
    define f(node) as serialized string of a tree,
    f(node) = f(node.left) + '#'+node.val+'#' + f(node.right)

Node:
1) Use 'lnull' and 'rnull' for cases where left or right child is null.
Case: [0,0,null], and [0,null,0] will dfs serialization to same value.

Complexity: O(n²), O(n)

This is still O(n²) because the string comparison is linear O(n)!

3. Unique identifier(uid) - topological RECURSIVE SERIALIZATION ID

Define recursive id, recurrence relation:
    root key = (left id, root value, right id)
If key already exists, then root id = keyToId[key],
else root id = keyToId[key] = ++ID, where ID is globally auto incremental id.

Use the auto increment id in the dictionary as the tree id.

Complexity: O(n), O(n)

================================================================================
SIMILAR QUESTIONS
Serialize and deserialize binary tree.

"""

from collections import defaultdict, Counter

class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

        result = self.findDuplicateSubtreesDfsSerialization(root)
        # result = self.findDuplicateSubtreesRecursiveSerializationId(root)

        print("result: => ", result)

        return result

    def findDuplicateSubtreesDfsSerialization(self, root):
        """
        Traverse the tree in postorder fashion.
        """
        count = {}
        def inorderLeftRightNULL(node):
            if not node: return '#'
            left = dfs(node.left) if node.left else '<' # to differentia left and right NULL
            right = dfs(node.right) if node.right else '>'
            # inorder = left + ',' + str(node.val) + ',' + right
            inorder = left + str(node.val) + right
            return inorder

        def inorderParenthese(node):
            if not node: return '' # return '#' will do, of course
            left = dfs(node.left) # to differentia left and right NULL
            right = dfs(node.right)
            # inorder = left + ',' + str(node.val) + ',' + right # XXX: wrong
            # inorder = left + str(node.val) + right + ',' # good
            inorder = '(' +left + str(node.val) + right + ')' # good, differentiate left and right
            return inorder

        def dfs(node):
            inorder = inorderLeftRightNULL(node)
            # inorder = inorderParenthese(node)

            if inorder and count.get(inorder, 0) == 1: # O(n) complexity for string comparison
                print(node, ', match: ', inorder)
                result.append(node)
            count[inorder] = count.get(inorder, 0) + 1

            return inorder

        result = []
        dfs(root)

        return result

    def findDuplicateSubtreesRecursiveSerializationId(self, root):
        """
        Use recursive serialization id as unique id of subtrees.
        """
        result = []
        tree2id = defaultdict() # (left id, current value, right id) => id
        tree2id.default_factory = tree2id.__len__ # auto increment id

        # counter = {} # id or (left id, current value, right id) => count
        counter = Counter() # id or (left id, current value, right id) => count

        def dfs(node):
            if not node: return -1 # auto increment id, -1 for initial value
            left = dfs(node.left)
            right = dfs(node.right)
            key = (left, node.val, right)
            counter[tree2id[key]] = counter.get(tree2id[key], 0) + 1
            if counter[tree2id[key]] == 2: # filter duplicate by counting
                # print(node, ', match: ', key)
                result.append(node)

            return tree2id[key]

        result = []
        dfs(root)

        return result

def test():
    from _tree import Codec, TreeNode

    solution = Solution()

    assert solution.findDuplicateSubtrees(Codec.deserialize('')) == []
    assert solution.findDuplicateSubtrees(Codec.deserialize('[]')) == []
    assert solution.findDuplicateSubtrees(Codec.deserialize('[1]')) == []
    assert solution.findDuplicateSubtrees(Codec.deserialize('[1,1]')) == []
    assert solution.findDuplicateSubtrees(Codec.deserialize('[1,1,1]')) == [TreeNode(1)]
    assert solution.findDuplicateSubtrees(Codec.deserialize('[1,0,0,#,0,0,#]')) == [TreeNode(0)]
    assert sorted(solution.findDuplicateSubtrees(Codec.deserialize('[1,2,3,4,null,2,4,null,null,4]'))) == sorted([TreeNode(4), TreeNode(2)])
    assert sorted(solution.findDuplicateSubtrees(Codec.deserialize('[0,0,0,0,null,null,0,null,null,null,0]'))) == [TreeNode(0)]

    print("self test passed!")

if __name__ == '__main__':
    test()
