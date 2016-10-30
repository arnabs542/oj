#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
399. Evaluate Division

Total Accepted: 5245
Total Submissions: 13888
Difficulty: Medium
Contributors: Admin

Equations are given in the format A / B = k, where A and B are variables represented
as strings, and k is a real number (floating point number). Given some queries, return
the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values,
vector<pair<string, string>> queries , where equations.size() == values.size(),
and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
The input is always valid. You may assume that evaluating the queries will
result in no division by zero and there is no contradiction.
===============================================================================================
SOLUTION:
    The problem can be converted/treated as a GRAPH problem where variables are graph VERTICES
and the quotients are EDGES connecting vertices.
    Then it can be solved by search the graph with depth-first search or breadth-first search.
'''
class Solution(object):

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        adj = self.buildGraph(equations, values, queries)
        result = []
        for query in queries:
            result.append(self.BFS(query, adj))

        print(result)
        return result

    def BFS(self, query, adj):
        '''
        Graph search with BFS

        32ms, beats 98.14%, 2016-10-30 18:02
        '''
        i, j = query
        if not (i in adj and j in adj):
            return -1.0
        # search
        frontier, visited = [i], set([i])

        while frontier:
            v = frontier.pop(0)
            if v == j:
                return adj[i][j]
            for u in adj[v].keys():
                # push
                if u not in visited:
                    adj[i][u] = adj[i][v] * adj[v][u]
                    frontier.append(u)
                    visited.add(u)
                pass
            pass

        return -1.0

    def floydWarshall(self, query, adj):
        '''
        Graph search with BFS

        '''
        # TODO: floyd-warshall algorithm

    def unionFind(self, query, adj):
        '''
        Graph search with BFS

        '''
        # TODO: union-find algorithm?

    def buildGraph(self, equations, values, queries):
        '''
        Build the graph represented by matrix(actually it's a dictionary)
        '''
        adj = {}
        for i, equation in enumerate(equations):
            adj.setdefault(equation[0], {})
            adj.setdefault(equation[1], {})
            adj[equation[0]][equation[0]] = 1.0
            adj[equation[1]][equation[1]] = 1.0

            adj[equation[0]][equation[1]] = values[i]
            adj[equation[1]][equation[0]] = 1.0 / values[i]
            pass
        # for _, query in enumerate(queries):
            # adj.setdefault(query[0], {})
            # adj.setdefault(query[1], {})
            # adj[query[0]][query[0]] = 1.0
            # adj[query[1]][query[1]] = 1.0
            # pass

        # print(adj)
        return adj

def test():
    solution = Solution()
    assert solution.calcEquation(
        [["a", "b"], ["b", "c"]],
        [2.0, 3.0],
        [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]) == \
        [6.00000, 0.5, -1.00000, 1.00000, -1.00000]
    print('self test passed')

if __name__ == '__main__':
    test()
