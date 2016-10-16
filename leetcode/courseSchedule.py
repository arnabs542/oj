#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
207. Course Schedule

Total Accepted: 56176
Total Submissions: 191216
Difficulty: Medium
Contributors: Admin

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it
possible for you to finish all courses?

For example:

  2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have
finished course 0. So it is possible.

  2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have
finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices.

#1 Topological sorting with depth-first search:

TOPOLOGICAL-SORT(G)
1 call DFS(G) to compute finishing times v.f for each vertex
2 as each vertex is finished, insert it onto the front of a linked list(or append)
3 return the linked list of vertices
'''

class Solution(object):

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = self.buildGraph(numCourses, prerequisites)
        return self.topologicalSort(adj)

    def buildGraph(self, numCourses, prerequisites):
        '''
        Build a graph with adjacency list representation
        '''
        adj = [[] for i in range(numCourses)]
        for edge in prerequisites:
            adj[edge[0]].append(edge[1])
        return adj

    def topologicalSort(self, adj):
        color = {}
        vertices_sorted = []
        for v in range(len(adj)):
            # vertex not visited yet
            if v not in color:
                if not self.DFS(adj, v, color, vertices_sorted):
                    return False
        print(vertices_sorted)
        return True

    def DFS(self, adj, v, color, vertices_sorted):
        '''
        Topological sort with depth-first search.

        '''
        # exploring its neighbors
        color[v] = 'gray'
        # explore connected edges
        for u in adj[v]:
            # adjacent vertex's is predecessor, being visited:
            # cycle exists in the DAG
            if color.get(u) == 'gray':
                return False
            # if adjacent vertex has already been visited, ignore
            if u not in color and not self.DFS(adj, u, color, vertices_sorted):
                return False
        color[v] = 'black'
        vertices_sorted.append(v)
        return True

    # TODO: BFS(breadth-first search) to topologically sort

def test():
    solution = Solution()
    assert solution.canFinish(2, [[1, 0]])
    assert not solution.canFinish(2, [[1, 0], [0, 1]])

if __name__ == '__main__':
    test()
