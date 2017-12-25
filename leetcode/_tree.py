#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Tree data structure implementations.

A tree is a recursive, or hierarchical data structure, a graph without back edges.

"""
import math

# TODO: representation of segment tree to make the interface simpler, maybe?
class SegmentTree(object):
    """
    A segment tree is a tree data structure used for storing information about
    intervals, or segments.

    It allows querying which of the stored segments contain a given point. It is, in principle,
    a static structure; that is, it's a structure that cannot be modified once it's built.

    Each node holds information within a specific range(interval, segment). And its children
    store information within the split space of parent's interval.

    Representation of Segment trees
    ----------------------------------------
    1. Leaf Nodes are the elements of the input array.
    2. Each internal node represents some merging of the children nodes. The merging may be
    different for different problems. For range sum query, merging is sum of leaves under a
    node. And for range minimum query, merging is minimum of children/leaves under a node.

    An array representation of tree is used to represent Segment Trees.
    For each node at index i, the left child is at index 2*i+1, right child at 2*i+2 and
    the parent is at floor((i - 1) / 2).

    Height of the segment tree will be h = ceil(log₂n). Since the tree is represented using
    array and relation between parent and child indexes must be maintained, size of memory
    allocated for segment tree will be 2^{h+1} - 1.

    Construction
    ------------
    The tree can be constructed in a divide and conquer approach.

    Query
    -----

    Update
    ------

    Time Complexity:
    ----------------
    Time Complexity for tree construction is O(n). There are total 2n-1 nodes, and value of
    every node is calculated only once in tree construction.
    T(n) = 2T(n/2) + 1 = O(n)

    Time complexity to query is O(Logn). To query a sum, we process at most four nodes at
    every level and number of levels is O(Logn).
    T(n) = T(n/2) + 1 = O(logn)

    The time complexity of update is also O(Logn). To update a leaf value, we process one
    node at every level and number of levels is O(Logn).
    T(n) = T(n/2) + 1 = O(logn)

    """

    def __init__(self, nums, purpose='rsq'):
        """
        Input
        -----
        nums: input array
        query: range minimum query(rmq), or range sum query(rsq)

        Returns
        -------

        """
        self._nums = nums
        self.size = len(nums)
        self._purpose = purpose
        if purpose == 'rsq':
            self._combine = sum # range sum query
            self._getLeaf = lambda i: self._nums[i]
        elif purpose == 'rmq':
            # return indices, instead of actual number
            def argmin(iterable):
                x, y = iterable
                if not 0 <= x < self.size:
                    return y
                if not 0 <= y < self.size:
                    return x
                z = x
                if self._nums[x] <= self._nums[y]: z = x
                else: z = y
                return z
            self._combine = argmin # range minimum query
            self._getLeaf = lambda i: i

        if not nums:
            self._height = 0
        else:
            self._height = math.ceil(math.log2(len(nums)))
            # full binary tree, using array representation
            self._tree = [0] * int(pow(2, self._height + 1) - 1)
            self._construct(0, 0, len(nums) - 1)
        pass

    def _construct(self, idx: int, left: int, right: int):
        '''
        idx: tree node index in array representation
        left, right: segment range indexes, starting from 0
        '''
        if left == right:
            self._tree[idx] = self._getLeaf(left)
        elif left < right:
            mid = (left + right) >> 1
            self._tree[idx] = self._combine((
                self._construct(2 * idx + 1, left, mid),
                self._construct(2 * idx + 2, mid + 1, right),
            ))
        else:
            print("ILLEGAL INPUT!")
        return self._tree[idx]

    def query(self, i, j, index=False):
        """
        Inputs
        ------
        index: whether return the index of minimal element


        """
        result = self._query(0, 0, self.size - 1, i, j)
        # print("query: ", i, j, result)
        if self._purpose == 'rmq':
            if not index and 0 <= result < self.size: return self._nums[result]
        return result


    def update(self, i, val):
        '''
        update element at index i to value val
        '''
        if not 0 <= i <= len(self._nums) - 1:
            return
        if self._purpose == 'rsq':
            diff = val - self._nums[i]
            self._nums[i] = val
            self._updateSumDfs(0, 0, len(self._nums) - 1, i, diff)
        elif self._purpose == 'rmq':
            self._nums[i] = val
            self._updateMinDfs(0, 0, len(self._nums) - 1, i)
        else:
            raise NotImplementedError("only supports range minimum query or range sum query")


    def _query(self, idx, left, right, i, j):
        '''
        idx: tree node index in array representation
        left, right: segment range

        Query interval is [i, j], and current node's interval is [left, right].
        If two intervals don't overlap with each other, then the search shall not be
        carried on this node.

        '''
        if not 0 <= i <= j < len(self._nums):
            # invalid query
            return 0 if self._purpose == 'rsq' else -1 # for rmq, returning the index
        if (i > j) or j < left or i > right:
            # query interval not overlapping with current node's interval
            # return 0
            return 0 if self._purpose == 'rsq' else -1 # for rmq, returning the index
        elif i <= left and right <= j: # contain relation, return the full range
            return self._tree[idx]
        else:
            mid = (left + right) >> 1
            return self._combine((
                self._query(2 * idx + 1, left, mid, i, j),
                self._query(2 * idx + 2, mid + 1, right, i, j)
            ))

    def _updateSumDfs(self, idx, left, right, i, diff):
        '''
        idx: tree node index in array representation
        left, right: segment range

        Add difference to update instead of pure set operation.
        '''
        if not left <= i <= right: return

        self._tree[idx] += diff
        if left < right:
            mid = (left + right) >> 1
            # NOTE: only one branch will execute recursively
            self._updateSumDfs(2 * idx + 1, left, mid, i, diff)
            self._updateSumDfs(2 * idx + 2, mid + 1, right, i, diff)
        pass

    def _updateMinDfs(self, idx, left, right, i):
        """
        idx: tree node index in array representation
        left, right: segment range
        i: update element at index i

        Add difference to update instead of pure set operation.
        """
        if not left <= i <= right: return -1
        if left < right:
            mid = (left + right) >> 1
            # NOTE: only one branch will execute recursively
            self._tree[idx] = self._combine((
                self._updateMinDfs(2*idx + 1, left, mid, i),
                self._updateMinDfs(2*idx + 2, mid + 1, right, i),
            ))
        else:
            self._tree[idx] = self._getLeaf(i)
        return self._tree[idx]


class BinaryIndexedTree(object):
    # TODO: binary indexed tree

    def __init__(self, nums):
        pass

    def update(self):
        pass

    def query(self):
        pass

def testSegmentTree():
    # Your SegmentTree object will be instantiated and called as such:
    nums = []
    segmentTree = SegmentTree(nums)
    assert segmentTree.query(0, 2) == 0

    nums = [-1]
    segmentTree = SegmentTree(nums)
    assert segmentTree.query(0, 0) == -1
    segmentTree.update(0, 1)
    segmentTree.query(0, 0)

    nums = [1, 3, 5, 7, 9, 11]
    segmentTree = SegmentTree(nums)
    assert segmentTree.query(1, 3) == 15
    segmentTree.update(1, 10)
    assert segmentTree.query(1, 3) == 22

    nums = [1, 3, 5]
    segmentTree = SegmentTree(nums)
    assert segmentTree.query(0, 2) == 9
    segmentTree.update(1, 2)
    assert segmentTree.query(0, 2) == 8

    nums = [7, 2, 7, 2, 0]
    segmentTree = SegmentTree(nums)
    assert segmentTree.query(0, 0) == 7
    assert segmentTree.query(4, 4) == 0
    segmentTree.update(4, 6)
    segmentTree.update(0, 2)
    segmentTree.update(0, 9)
    assert segmentTree.query(4, 4) == 6
    segmentTree.update(3, 8)
    assert segmentTree.query(0, 4) == 32

    print("segment tree for range sum query passed!")

    nums = []
    tree = SegmentTree(nums)
    assert tree.query(0, 0)  == 0

    nums = [7, 2, 3, 0, 5, 10, 3, 12, 18] # size = 9
    tree = SegmentTree(nums, 'rmq')

    print(tree._tree)
    assert tree.query(0, 0) == 7
    assert tree.query(0, 4) == 0
    assert tree.query(4, 7) == 3
    assert tree.query(7, 7) == 12
    assert tree.query(7, 8) == 12
    tree.update(0, 1)
    assert tree.query(0, 0) == 1
    assert tree.query(0, 2) == 1
    assert tree.query(1, 5) == 0

    print("segment tree for range minimum query passed")

def test():
    testSegmentTree()

    print("self test passed!")

if __name__ == '__main__':
    test()
