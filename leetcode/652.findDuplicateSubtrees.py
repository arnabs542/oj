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

1. Brute force - traverse and verify
Exhaust all subtrees, and check for duplicate.

Complexity: O(N²)

2. Hash count - dfs

Find duplicates? Hash count!

Traverse the tree, hash all subtree serialization. Then we can check duplicate
in one pass.

Use the hash table to store mapping <subtree serialization, root node>

Node:
1) Use 'lnull' and 'rnull' for cases where left or right child is null.
Case: [0,0,null], and [0,null,0] will dfs serialization to same value.

Complexity: O(n²), O(n)

This is still O(n²) because the string comparison is linear O(n)!

3. Unique identifier(uid)
The string comparison involves duplicate calculations, we can utilize the
state transition.

Use the auto increment id in the dictionary as the tree id.

Complexity: O(n), O(n)

"""

from collections import defaultdict, Counter

class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

        # result = self._findDuplicateSubtreesDfsHash(root)
        result = self._findDuplicateSubtreesDfsUid(root)

        print("result: => ", result)

        return result

    def _findDuplicateSubtreesDfsHash(self, root):
        """
        Traverse the tree in postorder fashion.
        """
        count = {}
        def dfs(node):
            if not node: return 'null'
            left = dfs(node.left) if node.left else 'lnull'
            right = dfs(node.right) if node.right else 'rnull'

            subtree = left + '#' + str(node.val) + '#' + right
            if count.get(subtree, 0) == 1: # O(n) complexity for string comparison
                print(node, ', match: ', subtree)
                result.append(node)
            count[subtree] = count.get(subtree, 0) + 1

            return subtree

        result = []
        dfs(root)

        return result

    def _findDuplicateSubtreesDfsUid(self, root):
        result = []
        tree2id = defaultdict() # (left id, current value, right id) => id
        tree2id.default_factory = tree2id.__len__ # auto increment id

        # counter = {} # id or (left id, current value, right id) => count
        counter = Counter() # id or (left id, current value, right id) => count

        def dfs(node):
            if not node: return -1
            left = dfs(node.left)
            right = dfs(node.right)
            key = (left, node.val, right)
            counter[tree2id[key]] = counter.get(tree2id[key], 0) + 1
            if counter[tree2id[key]] == 2:
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
    assert sorted(solution.findDuplicateSubtrees(Codec.deserialize('[1,2,3,4,null,2,4,null,null,4]'))) == sorted([TreeNode(4), TreeNode(2)])
    assert sorted(solution.findDuplicateSubtrees(Codec.deserialize('[0,0,0,0,null,null,0,null,null,null,0]'))) == [TreeNode(0)]

    print("self test passed!")

if __name__ == '__main__':
    test()
