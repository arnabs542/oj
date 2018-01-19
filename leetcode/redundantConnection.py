#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
684. Redundant Connection

In this problem, A TREE IS AN UNDIRECTED GRAPH THAT IS CONNECTED AND HAS NO CYCLES.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

Update (2017-09-26):
We have overhauled the problem description + test cases and specified clearly the graph is an undirected graph. For the directed graph follow up please see Redundant Connection II). We apologize for any inconvenience caused.

==============================================================================================
SOLUTION

Redundant connection means cycle, and cycle detection on a graph can be done with
graph search like breadth first search or depth first search or union find.

However, this problem requires that the edge to remove must occur last.

1. Brute force - graph search

The core idea is to search for path from u to v while constructing the graph with edge [u, v].

For each edge (u, v), we do depth first search from u to v. If there is a path, then it's a
redundant path. Otherwise, add the edge to the graph, and repeat.

Complexity: O(N²), O(N)

2. Vertices set
Can we keep track of visited vertices, and if an edge connects two visited vertices then remove it?
Of course not, this is wrong ,consider this case: [[1, 2], [3, 4], [1, 4]]:
    1 - 2
    |
    4 - 3

There isn't even a cycle!

Don't even think about it, use union find!

3. Union find
Union find operation is performed on disjoint set data structure.

----------------------------------------------------------------------------------------------
Union find data structure

A disjoint set keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets.

A disjoint-set forest consists of a number of elements each of which stores an id, a parent pointer, and, in efficient algorithms, a value called the "rank".

The parent pointers of elements are arranged to form one or more trees, each representing a set. If an element's parent pointer points to no other element, then the element is the root of a tree and is the representative member of its set. A set may consist of only a single element. However, if the element has a parent, the element is part of whatever set is identified by following the chain of parents upwards until a representative element (one without a parent) is reached at the root of the tree.

Forests can be represented compactly in memory as arrays in which parents are indicated by their array index.

Reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure

We use two techniques to improve the run-time complexity: path compression, and union-by-rank.

----------------------------------------------------------------------------------------------
Time Complexity: O(Nα(N))≈O(N), where N is the number of vertices (and also the number of edges) in the graph, and α is the Inverse-Ackermann function. We make up to N queries of dsu.union, which takes (amortized) O(α(N)) time. Outside the scope of this article, it can be shown why dsu.union has O(α(N)) complexity, what the Inverse-Ackermann function is, and why O(α(N)) is approximately O(1).

Space Complexity: O(N). The current construction of the graph (embedded in our dsu structure) has at most N nodes.


"""

class Solution:

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        result = self._findRedundantConnectionUnionFind(edges)

        print(edges, 'remove: ', result)

        return result

    # TODO: graph search solution
    def _findRedundantConnectionDfs(self, edges):
        pass

    def _findRedundantConnectionUnionFind(self, edges):
        parents = [i for i in range(1001)]
        def find(u):
            if parents[u] != u: parents[u] = find(parents[u]) # path compression
            return parents[u]
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu < pv: parents[pv] = pu
            else: parents[pu] = pv

        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu == pv:
                return [u, v]
            union(pu, pv)

        return []


def test():
    solution = Solution()

    edges = [[1, 2], [1, 3], [2, 3]]
    assert solution.findRedundantConnection(edges) == [2, 3]

    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    assert solution.findRedundantConnection(edges) == [1, 4]

    edges = [[1, 2], [3, 4], [1, 3], [2, 4]]
    assert solution.findRedundantConnection(edges) == [2, 4]

    # ignore below cases, those are for directed graph
    # output = [4,2] Expected: [4,1]
    edges = [[2, 3], [5, 2], [1, 5], [4, 2], [4, 1]]
    assert solution.findRedundantConnection(edges) == [4, 1]

    edges = [[2, 3], [5, 3], [2, 1], [5, 4], [3, 2]]  # expects [5,3]?
    assert solution.findRedundantConnection(edges) == [3, 2]

    print("self test passed")

if __name__ == '__main__':
    test()
