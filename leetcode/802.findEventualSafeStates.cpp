/**
 *
802. Find Eventual Safe States
Medium

In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Here is a diagram of the above graph.

Illustration of graph

Note:

graph will have length at most 10000.
The number of edges in the graph will not exceed 32000.
Each graph[i] will be a sorted list of different integers, chosen within the range [0, graph.length - 1].

SOLUTION
================================================================================

The recurrence relation is, for each vertex v:
    v is safe if and only if all u which (v, u) has en edge is safe.
    If there is a cycle, then all nodes within the cycle is not safe.
And the base case is terminal nodes which are safe by definition.

1. Brute force verification with depth first search

Complexity: O(N²)

2. Depth first search with memoization

Memoize the is safe or not result to avoid duplicate calculation.
And remember, there are cycles in the graph, and it's not a tree.
So,
    1) Be careful about the STATE TRANSITION if mixing visited state and memoized result.
    2) Memoized result can't be passed by recursive call return value, because it's a graph.

Complexity: O(N)

3. Topological sort
1) Do topological sort with dfs
2) Keep cutting 0 out-degree nodes.

Complexity: O(N)

 *
 */

#include <debug.hpp>


class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        vector<int> result;
        //result = eventualSafeNodesDfs(graph);
        result = eventualSafeNodesSingleStateMachine(graph);

        cout << graph << " => " << result << endl;

        return result;
    }

    void dfs(int v, vector<vector<int>> &graph, vector<int> &result) {
        if (visited.count(v)) {
            if(visited[v] == 0) mem[v] = false; // cycle
            return;
        }
        bool isSafe = true;
        // recurrence
        visited[v] = 0;
        for (int u: graph[v]) {
            //if (u == v) continue; // self forming cycle
            if (visited.count(u)) {
                if (visited[u] == 0) { // cycle
                    isSafe = false;
                } else {
                    isSafe = isSafe && mem[u]; // memoized result
                }
            } else {
                dfs(u, graph, result);
                isSafe = isSafe && mem[u];
            }
        }

        visited[v] = 1; // visited;
        mem[v] = isSafe;
        if (isSafe) result.push_back(v);
    }

    vector<int> eventualSafeNodesDfs(vector<vector<int>> &graph) {
        vector<int> result;
        int n = graph.size();

        visited.clear();
        mem.clear();
        for (int i = 0; i < n; ++i) {
            dfs(i, graph, result);
        }
        std::sort(result.begin(), result.end());
        return result;
    }

    unordered_map<int, int> visited; // visiting = 1, visited = 2
    unordered_map<int, bool> mem; // 0: unsafe, 1: safe. Can be stored in vector

    // optimized: dfs with single state machine in visited
    enum State {INITIAL, VISITING, SAFE, UNSAFE};
    void dfs(int v, vector<vector<int>> &graph, vector<int> &result, vector<char> &states) {
        if (states[v] != INITIAL) {
            return; // visited
        }
        bool isSafe = true;
        // recurrence relation
        states[v] = VISITING;
        for (int u: graph[v]) {
            // if (u == v) continue; // self forming cycle
            if (states[u] == VISITING) { // cycle
                isSafe = false;
            }
            else if (states[u] != 0) { // already states, have two kinds of results
                isSafe = isSafe && states[u] == SAFE; // memoized result
            } else { // not visited
                dfs(u, graph, result, states);
                isSafe = isSafe && states[u] == SAFE;
            }
        }

        states[v] = isSafe ? SAFE:UNSAFE; // visited;
        if (isSafe) result.push_back(v);
    }

    vector<int> eventualSafeNodesSingleStateMachine(vector<vector<int>> &graph) {
        vector<int> result;
        int n = graph.size();

        vector<char> visited = vector<char>(n , INITIAL);
        for (int i = 0; i < n; ++i) {
            dfs(i, graph, result, visited);
        }
        std::sort(result.begin(), result.end());
        return result;
    }
};

int test() {
    Solution solution;
    vector<vector<int>> graph;
    vector<int> output;

    graph = {};
    output = {};
    assert(solution.eventualSafeNodes(graph) == output);

    graph = {{1}, {0}};
    output = {};
    assert(solution.eventualSafeNodes(graph) == output);

    // self forming cycle
    //graph = {{0}};
    //output = {0};
    //assert(solution.eventualSafeNodes(graph) == output);

    //graph = {{0}, {1}};
    //output = {0, 1};
    //assert(solution.eventualSafeNodes(graph) == output);

    graph = {{1,2},{2,3},{5},{0},{5},{},{}};
    output = {2,4,5,6};
    assert(solution.eventualSafeNodes(graph) == output);

    cout << "passed" << endl;
    return 0;
}

int main() {
    test();
    return 0;
}
