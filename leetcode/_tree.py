#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Tree data structure implementations.

A tree is a recursive, or hierarchical data structure, a graph without back edges.

"""
import math

# class TreeNode(object):
    # def __init__(self, x):
        # self.val = x
        # self.left = None
        # self.right = None

from _type import TreeNode

class Codec:

    debug = False

    @classmethod
    def serialize(cls, root, debug=False):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        cls.debug = debug
        serializedTree = cls._serializeBFS(root)
        if cls.debug:
            print(serializedTree)
        return serializedTree

    @classmethod
    def deserialize(cls, data: str,
                    T: type = int, NodeType: type = TreeNode, debug=False):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        cls.debug = debug
        root = cls._deserializeBFS(data, T, NodeType)
        if debug:
            cls.drawtree(root)
        return root

    @classmethod
    def _serializeBFS(cls, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str

        Breadth-first search.
        """
        data = []
        frontier = [root]
        while frontier:
            vertex = frontier.pop(0)
            data.append(str(vertex.val) if vertex else 'null')
            if vertex:
                frontier.append(vertex.left)
                frontier.append(vertex.right)
            pass

        while data and data[-1] == 'null': data.pop()
        # print('BFS result:', data)
        return '[{}]'.format(','.join(data))

    @classmethod
    def _deserializeBFS(cls, data, T: type=int, NodeType: type=TreeNode):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode

        Breadth-first search.
        """
        # strip the parentheses
        vertices = [NodeType(T(x.strip())) if x not in ('', 'null', ' null', '#', ' #') else None
                    for x in data.strip("[]").split(',')]

        root = vertices.pop(0) if vertices else None
        frontier = [root] if root else []
        while frontier and vertices:
            vertex = frontier.pop(0)
            vertex.left, vertex.right = (vertices.pop(0) if vertices else None,
                                         vertices.pop(0) if vertices else None)
            for child in (vertex.left, vertex.right):
                if child: frontier.append(child)

        return root

    @classmethod
    def _serializeDFS(cls, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # TODO: depth-first solution

    @classmethod
    def _deserializeInorder(cls, root: TreeNode) -> TreeNode:
        # guess at least another traversal sequence is necessary
        pass

    @classmethod
    def _serializeInorder(cls, root):
        pass

    @staticmethod
    def drawtree(root):
        # DONE: visualize tree
        print("visualize tree:")
        # prettyPrintTree(root, "🌲   ")
        prettyPrintTree(root, "")



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

    Range Update
    -------------
    It can be done naively, calling update for every element within range.
    Or it can be done recursively with respect to range overlapping situation.

    Lazy Propagation
    ----------------
    In short, we try to postpone updating descendants of a node, until the descendants
    themselves need to be accessed.
    Use another array lazy[] which is the same size as our segment tree array tree[] to
    represent a lazy node. lazy[i] holds the amount by which the node tree[i] needs to be
    incremented, when that node is finally accessed or queried. When lazy[i] is zero, it
    means that node tree[i] is not lazy and has no pending updates.

    Time Complexity
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

    Reference
    ---------
    https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/
    https://leetcode.com/articles/recursive-approach-segment-trees-range-sum-queries-lazy-propagation/
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

    # TODO: lazy propagation


class BinaryIndexedTree(object):
    # DONE: binary indexed tree
    """
    Binary indexed tree

    A Fenwick tree or binary indexed tree is a data structure that can efficiently
    update elements and calculate PREFIX SUMS in a table of numbers.

    A linear list storing prefix sum takes O(n) time complexity to update.

    Binary indexed tree is a 1 based array, as implicit data structure to represent the BIT.

   -------------------------------------------------------------------------------------------
    The idea

    1) An integer can be represented as a BINARY NUMBER, or in another word, can be written
    as a SUM OF TERMS OF POWERS OF 2.

    And this terms can be interpreted as offset, or range, from previous number.
    Thus, we can construct the tree structure in such way that, each node stores prefix sum
    within range (previous number, current number]. And the range contains number of size of
    power of 2.

    In the same way, cumulative sum can be represented as sum of sets of partial sums.

    2) An (0, n] interval can be  divided into intervals of length of power of 2.

    So the prefix sum over (0, n] can be divided into disjoint ranges of length of power of 2.
    And the prefix sum is computed by summing up the sum over those ranges.

    3) Every node of BI Tree stores sum of n elements where n is a power of 2.
    And n is determined by the last 1 bit: n = i & -i.

    For example:
    idx is some index of BIT. r is a position in idx of the last digit 1 (from left to right)
    in binary notation. tree[idx] is sum of frequencies from index (idx – 2^r + 1) to index idx.

    ------------------------------------------------------------------------------------------
    Nodes relation

    1) Node i and its parent parent(i).
    Isolate the last digit, using bitwise operator AND with num and -num.

    Node i represents sum of range from (parent(i), i], where n = i - parent(i) is power of 2.
    parent(i)  = i - i & (-i)
    And i stores sum of n = i & (-i) elements after parent(i).

    2) Sibling
    Node i and its next adjacent sibling sibling(i).
    sibling(i) represents sum of twice as many elements as i.
    sibling(i)  = i + i & (-i)

    ------------------------------------------------------------------------------------------
    Example

    A range [0, n],  can be grouped into small ranges by integers that are powers of 2.
    That is, n = 2^{floor(log(n))} + m, where m is the offset.
    And m can be written as m = 2^{floor(log(n))} + m’, ...
    This is a recursive process.

    In binary indexed tree, each node stores sum of elements within range length n,
    where n is a power of 2, and it is the offset between it's index and it's parent's index.
    Every node and its parent have same binary number prefix, except the last bit 1.

    Take an example [0, 11], where 11 = 1011.
    8  = 1000_2
    9  = 1001_2
    10 = 1010_2
    11 = 1011_2

    Then (0, 11] can be divided into ranges:
    (0, 8], where 8 = 1000_2,
    (8, 10], where 10 - 1 = 2 = 10_2,
    (10, 11], where 11 - 10 = 1 = 1_2,

    Each node of binary indexed tree stores prefix sum from range

    ------------------------------------------------------------------------------------------
    Query

    Prefix sum of current current index i can be recursively divided into ranges like
    (parent(i), i].

    Parent index is obtained by removing the last bit of current index.
    parent(i)  = i - i & (-i)

    Removing the last 1bit, is to subtract a power of 2.

    ------------------------------------------------------------------------------------------
    Update

    Now, the trick is to update values. HOW?
    When updating a value, we need to update a range prefix sum after this index. What index?
    Of course it's not the parent node in query tree.
    The nodes that should be updated are those with larger index, and representing ranges containing
    current index.

    It's the siblings and recursively parents' siblings!
    The adjacent sibling represents a sum of range twice as the size of current one: 1, 2¹, 2², ...

    parent(i) = i + i & (-1), adding the last 1 bit is to add a power of 2.
    Since each node represents a sum over a range of size of power of 2,
    Adding last 1 bit, is to add

    ---------------------------------------------

    Time Complexity
    ----------------
    The number of set bits in binary representation of a number n is O(Logn).
    Therefore, we traverse at-most O(Logn) nodes in both getSum() and update() operations.
    Time complexity of construction is O(nLogn) as it calls update() for all n elements.

    Construct: O(nlogn)

    Query: O(logn)

    Update: O(logn)


    Reference
    ---------
    https://www.geeksforgeeks.org/two-dimensional-binary-indexed-tree-or-fenwick-tree/
    https://www.topcoder.com/community/data-science/data-science-tutorials/binary-indexed-trees/#2d

    """

    def __init__(self, nums):
        if isinstance(nums, list):
            self._tree = [0 for _ in range(len(nums) + 1)] # 0 is dummy root node
            self.size = len(self._tree) - 1
            for i, num in enumerate(nums):
                self.update(i, num)
        elif isinstance(nums, int):
            self._tree = [0 for _ in range(nums + 1)]
            self.size = nums
        pass

    def update(self, x, diff):
        """
        update the prefix sum

        Inputs
        -----
        x: element index, starting from 0
        diff: difference to old value

        Returns
        -------
        None
        """
        if x < 0:
            raise Exception("ERROR: BIT update index x = {} is smaller than 0!".format(x))
        if x >= self.size:
            # TODO: add a number to the end of array
            pass

        n = self.size
        x += 1 # zero indexed to one indexed
        while x <= n:
            self._tree[x] += diff
            x += x & -x
        return

    def query(self, x):
        # n = len(self._tree) - 1 # 0 is dummy root node
        if x < 0:
            return 0
        if x >= self.size:
            return self.query(self.size - 1)

        s = 0
        x += 1
        while x:
            s += self._tree[x]
            x -= x & -x
        return s

    def prefixSum(self, x):
        return self.query(x)

    def queryRangeSum(self, i, j):
        """
        Range sum query: [i, j]
        i, j: 0 based index
        """
        a = 0
        b = 0
        if i >= 0:
            a = self.prefixSum(i - 1)
        if j >= 0:
            b = self.prefixSum(j)
        return b - a

    def lowerBound(self, target):
        # DONE: binary search for lower bound index of cumulative value target,
        # assuming increasing cumulative function!
        low, high = 0, self.size - 1
        while low <= high:
            mid = (low + high) // 2
            if self.query(mid) >= target:
                high = mid - 1
            else:
                low = mid + 1
            pass
        # print("prefix sum: ", self.query(low), low)
        return low

    def upperBound(self, target):
        # DONE: binary search for upper bound index of cumulative value cum,
        # assuming increasing cumulative function!
        low, high = 0, self.size - 1
        while low <= high:
            mid = (low + high) // 2
            if self.query(mid) <= target:
                low = mid + 1
            else:
                high = mid - 1
            pass
        return high

class BinaryIndexedTree2D:
    """
    Two dimensional binary indexed tree is nothing but an array of 1D binary indexed tree.

    In two dimensional binary indexed tree, bit[x][y] stores range sum over:
        point [parent(x) + 1][maxY] to point [x][y].
    """
    def __init__(self, nums):
        if isinstance(nums, list):
            self.maxX = len(nums)
            self.maxY = len(nums[0]) if nums else 0

        self._tree = [[0 for _ in range(self.maxY + 1)] for _ in range(self.maxX + 1)]

    def update(self, x, y, diff):
        x += 1
        y += 1
        while x <= self.maxX:
            self._updatey(x, y, diff)
            x += x & -x
        pass

    def _updatey(self, x, y, diff):
        while y <= self.maxY:
            self._tree[x][y] += diff
            y += y & -y

    def query(self, x, y):
        x += 1
        y += 1
        if x <= 0 or y <= 0: return 0

        s = 0
        while x:
            y1 = y
            while y1:
                s += self._tree[x][y1]
                y1 -= y1 & -y1
                pass
            x -= x & -x

        return s

    def prefixSum(self, x, y):
        return self.query(x, y)


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

    print("segment tree for range minimum query passed!")

def testBIT():
    nums = []
    bit = BinaryIndexedTree(nums)
    assert bit.prefixSum(0) == 0
    assert bit.prefixSum(1) == 0
    assert bit.prefixSum(9) == 0

    nums = [1]
    bit = BinaryIndexedTree(nums)
    assert bit.prefixSum(0) == 1
    assert bit.prefixSum(2) == 1
    assert bit.prefixSum(9) == 1

    nums = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    bit = BinaryIndexedTree(nums)
    assert bit.prefixSum(5) == 12
    print("Sum of elements in arr[0..5] is " + str(bit.prefixSum(5)))
    bit.update(3, +6)
    assert bit.prefixSum(5) == 18
    try:
        bit.update(-1, 9)
    except Exception as e:
        # raise(e)
        print(e)

    # test binary search for lower bound and upper bound
    nums = [2, 1, 1, 0, 0, 0, 0, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    bit = BinaryIndexedTree(nums)
    assert bit.lowerBound(4) == 2
    assert bit.upperBound(4) == 6

    print("binary indexed tree passed!")

def test():
    testSegmentTree()

    testBIT()

    print("self test passed!")

if __name__ == '__main__':
    test()
