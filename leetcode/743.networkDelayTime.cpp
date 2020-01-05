/**
 *
743. Network delay time
Medium

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.



Example 1:



Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2


Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.

Hints
We visit each node at some time, and if that time is better than the fastest time we've reached this node, we travel along outgoing edges in sorted order. Alternatively, we could use Dijkstra's algorithm.

 *
 * SOLUTION
 * ===============================================================================
 *
 * Model the network as a weighted directed graph, the objective is:
 *   find single source shortest paths to all vertices.
 * And there are no negative weight cycle.
 *
 * 1. Bellman-ford dynamic programming
 *
 * Complexity: O(VE)
 *
 * 2. Dijkstra's - greedy and bfs like
 *
 * TODO:
 *
 * Complexity: O(V+E)
 *
 */

#include <debug.hpp>

class Solution{
public:
    int networkDelayTime(vector<vector<int>> &times, int n, int k) {
        int result;
        result = networkDelayTimeBellmanFord(times, n, k);

        cout << times << " " << n << " " << k << " " << result << endl;

        return result;
    }

    int networkDelayTimeBellmanFord(vector<vector<int>> &times, int n, int k) {
        if (n < 0 || k < 0 || k > n) return -1;
        //vector<int> opt(n+1, std::numeric_limits<int>::max()); // single source
        vector<unsigned int> opt(n+1, -1); // single source
        opt[k] = 0;

        for (int i = 1; i < n; ++i) { // optimal substructure
            vector<unsigned int> opt1 = opt;
            for (vector<int> &edge: times) {
                if (opt[edge[0]] == (unsigned int)-1) continue; // bad for branch prediction
                opt1[edge[1]] = std::min(opt1[edge[1]], opt1[edge[0]] + edge[2]); // path relaxation recurrence relation
            }
            opt = std::move(opt1); // XXX: opt1 can be dropped, since no max step restriction
        }
        int result = *std::max_element(opt.begin()+1, opt.end());
        return result;
    }
};

int test() {

    Solution solution;

    vector<vector<int>> times;
    int N, K;
    int output;

    times = {{2,1,1}, {2,3,1}, {3,4,1}};
    N = 4, K = 2;
    output = 2;
    assert(solution.networkDelayTime(times, N, K) == output);

    times = {{2,1,1}, {2,3,1}, {3,4,1}};
    N = 5, K = 5;
    output = -1;
    assert(solution.networkDelayTime(times, N, K) == output);

    times = {{1,2,1},{2,3,7},{1,3,4},{2,1,2}};
    N = 3, K = 2;
    output = 6;
    assert(solution.networkDelayTime(times, N, K) == output);

    cout << "test passed" << endl;

    return 0;
}

int main(int argc, char **argv) {
    test();

    return 0;
}
