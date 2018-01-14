/*
 *
310. Minimum Height Trees

For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]

Note:

(1) According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”

(2) The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
==============================================================================================
SOLUTION

1. Brute force
Start dfs/bfs for every node, assuming it's root, track the distance from from root to every
node. And accumulate the roots with minimum tree height.

Complexity: O(V(V+E)), O(logN) ~ O(N)

2. Reduce and induce - graph degrees analysis - cut the leaves until reach the root(s)

Note that the tree is described by the edges, maybe we can find something, like degrees, about
this problem?`

Simple cases:
1
1 - 2
1 - 2 - 3
1 - 2 - 3 -4

    0
    |
    1
   /
  2

    0
    |
    1
   / \
  2   3


     0  1  2
      \ | /
        3
        |
        4
        |
        5


     0  1  2
      \ | /
        3
        |
        4 - 6
        |
        5

One heuristic is that nodes with only one degree can never be a root node of a minimum height tree.
This is because a minimum height tree root must have balanced subtree height on each side.

Then, removing those nodes with only one degree just cut out some leaves, and leave the structure
of minimum height tree intact!

Then, why don't we REDUCE the problem to its simplest form!

1) remove all leaf edges from edges set, update degrees of vertices
2) repeat 1)
3) terminate until certain removal causes the edges set to be empty. Then that edges set is the
set of target root nodes!

If a removing step causes the edges to be empty, then there are two cases:
1) all nodes have same degrees(with 1), all eligible for root
2) all nodes are connected to one node(there exists one unique root, with maximum degree).

Removing an edge from a list(vector, array) is O(N) complexity, too much overhead.

Complexity: O(E² + V), where E is the number of edges, V is the number of vertices.

3. Optimization on removing leaf nodes or edges
Instead of removing edges, remove vertices at each time.

First, represent the tree more efficiently, like variant of adjacency list.
Use an adjacency set, map<node, set<nodes>>, to store the adjacency list representation of tree.

In this way, removing an edge or a leaf node, only takes O(1) complexity.

4. Breadth first search - further optimization of the idea of cutting leaves

Don't cut the leaves, just follow them to do breadth first search.

Start breadth first search with leaves...
Stop when there are only two nodes, or one node

Complexity: O(V + E)

Note that for a tree, we have always V = E + 1

 *
 *
 */

#include <debug.hpp>
#include <assert.h>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<pair<int, int>>& edges) {
        vector<int> result;

        //result = _findMinHeightTreesReduceNaive(n, edges);
        //result = _findMinHeightTreesReduceOpt(n, edges);
        result = _findMinHeightTreesBfs(n, edges);
        sort(result.begin(), result.end());
        cout << "result: " << result << endl;
        return result;
    }

    /**
     * Performance: 1000+ms
     * Find the roots by cutting edges
     * TODO: optimize! This is way to slow...
     */
    vector<int> _findMinHeightTreesReduceNaive(int n, vector<pair<int, int>>& edges) {
        map<int, int> degrees;
        vector<pair<int, int>> removedEdges;
        vector<int> result;

        if (edges.empty()) { // corner case: one node without any edges
            return  n == 1 ? vector<int>({0}) : vector<int>();
        }

        // build the hash count
        for (auto edge: edges) {
            int a = std::get<0>(edge), b = std::get<1>(edge);
            degrees[a] += 1;
            degrees[b] += 1;
        }
        while(true) {
            removedEdges.clear();
            for (auto it = edges.begin(); it != edges.end(); ) {
                pair<int, int> edge = *it;
                int a = std::get<0>(edge), b = std::get<1>(edge);
                if (degrees[a] == 1 || degrees[b] == 1) {
                    //removedEdges.insert(edge);
                    removedEdges.push_back(edge);
                    it = edges.erase(it); // TODO: erasing from vector while iterating? Optimize!
                } else ++it;
            }
            // XXX: lazy decrease
            for (auto it = removedEdges.begin(); it != removedEdges.end(); ++it) {
                pair<int, int> edge = *it;
                int a = std::get<0>(edge), b = std::get<1>(edge);
                degrees[a] -= 1;
                degrees[b] -= 1;
            }
            cout << "edges size: " << edges.size() << endl;
            if (0 == edges.size()) {
                cout << "removed size: " << removedEdges.size() << endl;
                // construct solution
                degrees.clear();
                int maxDegree = 0;
                for (auto edge: removedEdges) {
                    int a = std::get<0>(edge), b = std::get<1>(edge);
                    degrees[a] += 1;
                    degrees[b] += 1;
                    maxDegree = max(maxDegree, degrees[a]);
                    maxDegree = max(maxDegree, degrees[b]);
                }
                cout << "degrees size: " << degrees.size() << endl;
                for (auto it = degrees.begin(); it != degrees.end(); ++it) {
                    if (maxDegree == 1 || it->second > 1) { // case: 0 - 1
                        result.push_back(it->first);
                    }
                }
                break;
            }
        }
        return result;
    }

    /**
     *
     * Optimize using efficient data structure to represent tree: adjacency set
     *
     * Performance: 400+ms
     * After using vector instead of map to store degrees: 90+ms.
     *
     * Involves vector copy or destroy, so it's slow?
     *
     */
    vector<int> _findMinHeightTreesReduceOpt(int n, vector<pair<int, int>>& edges) {
        vector<int> degrees(n, 0);
        vector<pair<int, int>> allEdges;
        vector<pair<int, int>> remainingEdges = edges;
        vector<pair<int, int>> removedEdges;
        vector<int> result;

        if (edges.empty()) { // corner case: one node without any edges
            return  n == 1 ? vector<int>({0}) : vector<int>();
        }

        // build the hash count
        for (auto &edge: edges) {
            int a = std::get<0>(edge), b = std::get<1>(edge);
            degrees[a] += 1;
            degrees[b] += 1;
        }
        while(remainingEdges.size()) {
            removedEdges.clear();
            allEdges = std::move(remainingEdges);

            for (auto it = allEdges.begin(); it != allEdges.end(); ++it) {
                pair<int, int> &edge = *it;
                int a = std::get<0>(edge), b = std::get<1>(edge);
                if (degrees[a] == 1 || degrees[b] == 1) {
                    removedEdges.push_back(edge);
                } else {
                    remainingEdges.push_back(edge);
                };
            }
            // XXX: lazy decrease
            for (auto it = removedEdges.begin(); it != removedEdges.end(); ++it) {
                pair<int, int> edge = *it;
                int a = std::get<0>(edge), b = std::get<1>(edge);
                degrees[a] -= 1;
                degrees[b] -= 1;
            }
        }
        // construct solution
        degrees = vector<int>(n, 0);
        int maxDegree = 0;
        for (auto edge: removedEdges) {
            int a = std::get<0>(edge), b = std::get<1>(edge);
            degrees[a] += 1;
            degrees[b] += 1;
            maxDegree = max(maxDegree, degrees[a]);
            maxDegree = max(maxDegree, degrees[b]);
        }
        for (auto it = degrees.begin(); it != degrees.end(); ++it) {
            if ((maxDegree == 1 && *it > 0) || *it > 1) { // case: 0 - 1
                result.push_back(distance(degrees.begin(), it));
            }
        }
        return result;
    }

    /**
     *
     * Cut tree leaves in a breadth first search approach
     */
    vector<int> _findMinHeightTreesBfs(int n, vector<pair<int, int>>& edges) {
        if (n == 1) {
            return vector<int>({0});
        }

        vector<unordered_set<int>> adj(n, unordered_set<int>());
        vector<int> frontier;
        vector<int> frontierNext;

        for (auto edge: edges) {
            adj[edge.first].insert(edge.second);
            adj[edge.second].insert(edge.first);
        }
        for (int i = 0; i < n; ++i) {
            if (adj[i].size() <= 1) {
                frontierNext.push_back(i);
            }
        }
        while (n > 2) {
            frontier = std::move(frontierNext);
            n -= frontier.size();
            for (int i: frontier) {
                int j = *adj[i].begin();
                adj[i].erase(j);
                adj[j].erase(i); // remove edge from adjacency list
                if (adj[j].size() == 1) { // only add for 1, avoiding duplicate adding
                    frontierNext.push_back(j); // next search frontier
                }
            }
        }

        return frontierNext;
    }

};

void test()
{
    Solution solution;

    vector<pair<int, int>> edges;

    edges = {};
    assert(solution.findMinHeightTrees(0, edges) == vector<int>({}));

    edges = {};
    assert(solution.findMinHeightTrees(1, edges) == vector<int>({0}));

    edges = {{0,1}}; // 0 - 1
    assert(solution.findMinHeightTrees(2, edges) == vector<int>({0, 1}));

    edges = {{0,1}, {0, 2}}; // 0 - 1
    assert(solution.findMinHeightTrees(3, edges) == vector<int>({0}));

    edges = {{0, 1}, {0, 2}, {0, 3}, };
    assert(solution.findMinHeightTrees(4, edges) == vector<int>({0}));

    edges = {{0, 3}, {1, 3}, {2, 3}, {4, 3}, {5, 4}, };
    assert(solution.findMinHeightTrees(6, edges) == vector<int>({3, 4}));

    edges = {{0, 3}, {1, 3}, {2, 3}, {4, 3}, {5, 4}, {4, 6}};
    assert(solution.findMinHeightTrees(7, edges) == vector<int>({3, 4}));

    edges = {{0,1},{1,2},{1,3},{2,4},{3,5},{4,6}};
    assert(solution.findMinHeightTrees(7, edges) == vector<int>({1, 2}));

    cout << "self test passed" << endl;
}

int main(int argc, char *argv[])
{
    test();
    return 0;
}
