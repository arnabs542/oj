'''

210. Course Schedule II

Total Accepted: 39742
Total Submissions: 166532
Difficulty: Medium
Contributors: Admin

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the
ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it
is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have
finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished
both courses 1 and 2. Both courses 1 and 2 should be taken after you finished
course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.

Hints:
  This problem is equivalent to finding the topological order in a directed graph. If
a cycle exists, no topological ordering exists and therefore it will be impossible to
take all courses.
  Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining
the basic concepts of Topological Sort.
  Topological sort could also be done via BFS.

===================================================================================================
SOLUTION

A typical GRAPH problem, topological sort with DFS or BFS.

'''

class Solution(object):

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = self.buildGraph(numCourses, prerequisites)
        vertices_sorted = []
        self.topologicalSort(adj, vertices_sorted)
        print(vertices_sorted)
        return vertices_sorted

    def buildGraph(self, numCourses, prerequisites):
        adj = [[] for i in range(numCourses)]
        for edge in prerequisites:
            adj[edge[0]].append(edge[1])
        return adj

    def topologicalSort(self, adj, vertices_sorted):
        color = {}
        for v in range(len(adj)):
            if v not in color:
                if not self.DFS(v, adj, color, vertices_sorted):
                    vertices_sorted.clear()
                    return False
        return True

    def DFS(self, v, adj, color, vertices_sorted):
        color[v] = 'gray'
        for u in adj[v]:
            if color.get(u) == 'gray' or (
                u not in color and \
                not self.DFS(u, adj, color, vertices_sorted)):
                return False
        color[v] = 'black'

        vertices_sorted.append(v)
        return True

    # TODO: topological sort with BFS?

def test():
    solution = Solution()
    assert solution.findOrder(2, [[1, 0]]) == [0, 1]
    assert solution.findOrder(
        4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3]
    assert solution.findOrder(
        5, [[1, 4], [2, 4], [3, 1], [0, 2], [0, 3]]) == [4, 2, 1, 3, 0]
    assert not solution.findOrder(2, [[1, 0], [0, 1]])
    assert not solution.findOrder(4, [[0, 1], [1, 2], [0, 3], [3, 0]])

if __name__ == '__main__':
    test()
