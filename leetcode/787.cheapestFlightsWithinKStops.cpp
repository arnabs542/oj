/**
 *
787. Cheapest Flights Within K Stops
Medium

There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
Note:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.

SOLUTION
================================================================================

This is a single source shortest path in weighted directed graph problem.

1. Bellman-ford algorithm
Define state: f(v, i)=shortest path to v within i steps(i edges).
State transition:
    f(v, i) = min(f(v, i-1), f(u, i-1) + w(u,v) for each u in neighbours(v)).

Complexity: O(kE), where E is number of edges.

2. Dijkstra's algorithm

Dijkstra algorithm maintains a data structure to query/update minimum for current
search frontier.
But how to incorporate the constraint of k stops?
Maintain a tuple (vertex, distance, number of stops remaining)!

Complexity:
O(klogV+E), where k is the number of stops.

3. Breadth first search modified - actually it's bellman-ford
Modify the bfs algorithm to add a vertex into search frontier once its distance
is reduced by edge relaxation.
And this is actually Bellman-ford algorithm modified to keep tracking of updated
vertices only instead of all vertices at each step of edge relaxation.

Complexity: O(kE)

 *
 */

#include <debug.hpp>

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>> edges, int src, int dst, int k) {
        int result;
        //result = findCheapestPriceDPBellmanFord(n, edges, src, dst, k);
        //result = findCheapestPriceBfs(n, edges, src, dst, k);
        result = findCheapestPriceDijkstra(n, edges, src, dst, k);

        cout << n << " " << edges << " " << src << "->" << dst << " " << k << ": " << result << endl;

        return result;
    }

    int findCheapestPriceDPBellmanFord(int n, vector<vector<int>> edges, int src, int dst, int k) {
        if (src < 0 || src >= n || dst < 0 || dst >= n) return -1; // bounds checking can be optimized
        k = std::min(k, n - 2);

        //vector<int> cost(n, std::numeric_limits<int>::max());
        vector<unsigned int> cost(n, -1); // define state f[v][i]: optimal cost after i steps
        cost[src] = 0;
        for (int i = 1; i <= k + 1; ++i) {
            vector<unsigned int> cost1 = cost; // optimal cost after i+1 steps
            for (const vector<int> &edge: edges) { // similar to bfs if enumerating adjacent vertices
                if ((int)cost[edge[0]] == -1) continue; // bad for branch prediction?
                cost1[edge[1]] = std::min(cost1[edge[1]], cost[edge[0]] + edge[2]);
            }
            cost = std::move(cost1);
        }

        //if (cost[dst] == std::numeric_limits<int>::max())
            //cost[dst] = -1;

        return cost[dst];
    }

    // actually another centralized implementation of bellman-ford
    int findCheapestPriceBfs(int n, vector<vector<int>> edges, int src, int dst, int k) {
        if (src < 0 || src >= n || dst < 0 || dst >= n) return -1; // bounds checking can be optimized
        k = std::min(k, n - 2);

        // build graph
        //vector<vector<int>>
        unordered_map<int, vector<vector<int>>> adj; // v, {{u, w}, ...}
        for (auto const &edge: edges) {
            adj[edge[0]].push_back({edge[1], edge[2]});
        }

        // initialize distance
        vector<int> cost(n + 1, std::numeric_limits<int>::max());
        cost[src] = 0;

        queue<int> frontier;
        frontier.push(src);
        for (int i = 0; i <= k && frontier.size(); ++i) {
            queue<int> frontier1;
            vector<int> cost1 = cost;
            while (frontier.size()) { // make one step
                int v = frontier.front(); frontier.pop();
                for (auto &edge: adj[v]) {
                    int &u = edge[0];
                    if (cost1[u] > cost[v] + edge[1]) { // path relaxation
                        cost1[u] = cost[v] + edge[1]; // XXX: resolve the topological dependency!
                        frontier1.push(u); // add neighbour to search frontier once distance updated!
                    }
                }
            }
            frontier = std::move(frontier1);
            cost = std::move(cost1);
        }

        return cost[dst] == std::numeric_limits<int>::max() ? -1: cost[dst];
    }

    int findCheapestPriceDijkstra(int n, vector<vector<int>> edges, int src, int dst, int k) {
        if (src < 0 || src >= n || dst < 0 || dst >= n) return -1; // bounds checking can be optimized
        vector<vector<pair<int, int>>> adj(n, {}); // [u:[v, weight]]
        for (const vector<int> &edge: edges) {
            //adj[edge[0]].push_back({edge[1], edge[2]});
            adj[edge[0]].emplace_back(edge[1], edge[2]);
        }
        typedef tuple<int, int, int> ti3;
        priority_queue<ti3, vector<ti3>, std::greater<ti3>> frontier; //cost, allowed steps, vertex,
        frontier.push({0, k+1, src});
        while (!frontier.empty()) {
            int v, cost, step;
            std::tie(cost, step, v) = frontier.top(); frontier.pop();
            if (v == dst) return cost;
            if (step == 0) continue; // no more steps allowed
            for (pair<int, int> connection: adj[v]) {
                frontier.emplace(cost + connection.second, step-1, connection.first); // could result in O(V²) space of frontier
            }
        }

        return -1;
    }
};


int test() {
    int n;
    vector<vector<int>> edges;
    int output;
    int src, dst;
    int k;

    Solution solution;

    n = 3, edges = {};
    src = 0, dst = 2, k = 1;
    output = -1;
    assert(solution.findCheapestPrice(n, edges, src, dst, k) == output);

    n = 3, edges = {{0, 2, 100}};
    src = 0, dst = 2, k = 1;
    output = 100;
    assert(solution.findCheapestPrice(n, edges, src, dst, k) == output);

    n = 3, edges = {{0, 2, 100}};
    src = 0, dst = 2, k = 3;
    output = 100;
    assert(solution.findCheapestPrice(n, edges, src, dst, k) == output);

    n = 3, edges = {{0,1,100},{1,2,100},{0,2,500}};
    src = 0, dst = 2, k = 1;
    output = 200;
    assert(solution.findCheapestPrice(n, edges, src, dst, k) == output);

    n = 3, edges = {{0,1,100},{1,2,100},{0,2,500}};
    src = 0, dst = 2, k = 0;
    output = 500;
    assert(solution.findCheapestPrice(n, edges, src, dst, k) == output);

    n = 4, edges = {{0,1,1},{0,2,5},{1,2,1},{2,3,1}};
    src = 0, dst = 3, k = 1;
    output = 6;
    assert(solution.findCheapestPrice(n, edges, src, dst, k) == output);

    cout << "test passed" << endl;

    return 0;
}

int main(int argc, char **argv) {

    test();
    return 0;
}
