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

 *
 */

#include <debug.hpp>

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>> edges, int src, int dst, int k) {
        int result;
        result = findCheapestPriceDPBellmanFord(n, edges, src, dst, k);

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

    return 0;
}

int main(int argc, char **argv) {

    test();
    return 0;
}
