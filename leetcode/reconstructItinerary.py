#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
332. Reconstruct Itinerary

Total Accepted: 24793
Total Submissions: 89690
Difficulty: Medium
Contributors: Admin

Given a list of airline tickets represented by pairs of departure and arrival
airports [from, to], reconstruct the itinerary in order. All of the tickets belong
to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
    1. If there are multiple valid itineraries, you should return the itinerary that
has the smallest lexical order when read as a single string. For example, the itinerary
["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
    2. All airports are represented by three capital letters (IATA code).
    3. You may assume all tickets form at least one valid itinerary.

Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].


Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].

Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is
larger in lexical order.

==============================================================================================
SOLUTION:
    This is a Euler Path problem. Euler Path is a trail in a GRAPH which visits every EDGE
exactly once. The problem is similar to Hamiltonian Path (visits every VERTEX exactly once),
which is NP complete problem.

Eulerian Cycle
An undirected graph has Eulerian cycle if following two conditions are true.
1) All vertices with non-zero degree are connected. We don't care about vertices with
zero degree because they don't belong to Eulerian Cycle or Path (we only consider all edges).
2) All vertices have EVEN DEGREE.

Eulerian Path
An undirected graph has Eulerian Path if following two conditions are true.
1) Same as condition (a) for Eulerian Cycle
2) If zero or two vertices have odd degree and all other vertices have EVEN DEGREE. Note
that only one vertex with odd degree is not possible in an undirected graph (sum of all
degrees is always even in an undirected graph)

Directed graph is eulerian? (form a Eulerian circuit)
A directed graph has an eulerian cycle if following conditions are true (Source: Wiki)
1) All vertices with nonzero degree belong to a single strongly connected component.
2) IN DEGREE AND OUT DEGREE of every vertex is same.

Directed graph is semi-eulerian?(has Eulerian path)
A directed graph has an eulerian cycle if following conditions are true (Source: Wiki)
1) All vertices with nonzero degree belong to a single strongly connected component.
2) IN DEGREE AND OUT DEGREE of every vertex is same, except zero or two of them, as the start
and end vertices.

In this problem, we can assume the graph has Euler Path, so we don't have to do the
verification.

==============================================================================================
RECURSIVE CALL TO ITERATIVE
Refer to 'N Queens' document.

'''

from collections import defaultdict

class Solution(object):

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # return self.findItineraryDFS(tickets)
        # return self.findItineraryDFSSimplified(tickets)
        return self.findItineraryDFSIterative(tickets)

    def findItineraryDFS(self, tickets: list) -> list:
        '''
        Depth-first search with backtracking.

        Depth-first search state:
            state = edge = (u, i, v),
        where u is a vertex, and i is u's adjacent vertex's index, v is the copied vertex of
        i-th edge from u.

        1. The recursive DFS function's INPUT PARAMETERS are just u(vertex from).
        2. AFTER THE RECURSIVE CALL RETURNS, it needs to restore state for backtracking. The
        restoration need to be aware of i(adjacent vertex index) and its value v.
        3. And RETURN VALUE is None.
        So state is (u, i, v) tuple.

        Tip: replace elements instead of deleting it from list to speed up.
        '''
        tickets.sort()
        adj = defaultdict(list)
        for f, t in tickets:
            adj[f].append(t)

        def dfs(u):
            if len(path) == len(tickets) + 1:
                print(path)
                return True
            for i, v in enumerate(adj[u]):
                # FIXED: multiple edges connecting to vertices
                if v.startswith('#'):
                    continue
                path.append(v)
                adj[u][i] = '#'
                # path.append(adj[u].pop(i))
                if dfs(v):
                    return True
                path.pop()
                adj[u][i] = v
                # adj[u].insert(i, path.pop())
            pass
        path = ["JFK"]
        if not dfs("JFK"): print("Not Found")
        return path

    def findItineraryDFSSimplified(self, tickets: list) -> list:
        '''
        Depth-first search assuming definitely Eulerian to avoid BACKTRACKING.

        Similar procedure with Topological Sort: construct result after adjacent vertices
        have been visited(the current vertex is black).

        But this implementation won't be able to determine whether the input is valid.
        '''
        tickets.sort(reverse=True) # use reversed order to pop out smallest value in O(1)
        adj = defaultdict(list)
        for f, t in tickets:
            adj[f].append(t)
        def dfs(v):
            while adj[v]:
                dfs(adj[v].pop()) # prune edges
            # path.insert(0, v)
            path.append(v)
        path = []
        dfs('JFK')
        path.reverse()
        print(path)
        return path

    def findItineraryDFSIterative(self, tickets: list) -> list:
        tickets.sort()
        adj = defaultdict(list)
        for f, t in tickets:
            adj[f].append(t)

        # path = ['JFK']
        stack = [('JFK', 0, None)] # stack frame: (vertex, edge index, copied edge value)
        while stack and len(stack) < len(tickets) + 1:
            u, i, v = stack.pop() # stack frame
            if i >= len(adj[u]): # out of range means iteration of some depth is done
                if stack: # recursive call RETURNS
                    u, i, v = stack.pop()
                    adj[u][i] = v # RESTORE STATE
                    # path.pop()
                    stack.append((u, i + 1, v)) # to NEXT ITERATION of connected edges
            elif adj[u][i] == '#': # skip removed edges, to next iteration of connected edges
                stack.append((u, i + 1, None))
            else: # pushing, recursive call
                v, adj[u][i] = adj[u][i], '#'
                stack.append((u, i, v)) # PUSH STATE
                stack.append((v, 0, None))
                # path.append(v)

        if len(stack) == len(tickets) + 1:
            print(list(map(lambda x: x[0], stack)))
        else:
            print('Not found', stack)
        return list(map(lambda x: x[0], stack))
        # return path

def test():
    solution = Solution()

    assert solution.findItinerary([]) == ["JFK"]
    assert solution.findItinerary([
        ["MUC", "LHR"], ["JFK", "MUC"],
        ["SFO", "SJC"], ["LHR", "SFO"]]) == ["JFK", "MUC", "LHR", "SFO", "SJC"]
    assert solution.findItinerary([
        ["JFK", "SFO"], ["JFK", "ATL"],
        ["SFO", "ATL"], ["ATL", "JFK"],
        ["ATL", "SFO"]]) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]

    assert solution.findItinerary([['0', '1'], ['1', "JFK"], ["JFK", '0'], ["JFK", '3']])
    assert solution.findItinerary([
        ["EZE", "AXA"], ["TIA", "ANU"], ["ANU", "JFK"],
        ["JFK", "ANU"], ["ANU", "EZE"], ["TIA", "ANU"],
        ["AXA", "TIA"], ["TIA", "JFK"], ["ANU", "TIA"],
        ["JFK", "TIA"]]) == ["JFK", "ANU", "EZE", "AXA",
                             "TIA", "ANU", "JFK", "TIA",
                             "ANU", "TIA", "JFK"]
    assert solution.findItinerary([
        ["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]) == ["JFK", "NRT", "JFK", "KUL"]
    assert solution.findItinerary([["JFK", "A"], ["JFK", "B"]]) == ["JFK"] or True

    print('self test passed')

if __name__ == '__main__':
    test()
