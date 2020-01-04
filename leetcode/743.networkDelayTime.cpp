/**
 *
743. Network delay time
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
                if (edge[0] == -1) continue; // bad for branch prediction
                opt1[edge[1]] = std::min(opt1[edge[1]], opt1[edge[0]] + edge[2]); // path relaxation recurrence relation
            }
            opt = std::move(opt1);
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

    cout << "test passed" << endl;

    return 0;
}

int main(int argc, char **argv) {
    // TODO: submit
    test();

    return 0;
}
