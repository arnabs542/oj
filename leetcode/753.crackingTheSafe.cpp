/**
 *
753. Cracking the Safe
Hard

There is a box protected by a password. The password is a sequence of n digits where each digit can be one of the first k digits 0, 1, ..., k-1.

While entering a password, the last n digits entered will automatically be matched against the correct password.

For example, assuming the correct password is "345", if you type "012345", the box will open because the correct password matches the suffix of the entered password.

Return any password of minimum length that is guaranteed to open the box at some point of entering it.



Example 1:

Input: n = 1, k = 2
Output: "01"
Note: "10" will be accepted too.
Example 2:

Input: n = 2, k = 2
Output: "00110"
Note: "01100", "10011", "11001" will be accepted too.


Note:

n will be in the range [1, 4].
k will be in the range [1, 10].
k^n will be at most 4096.


Hints
We can think of this problem as the problem of finding an Euler path (a path visiting every edge exactly once) on the following graph: there are $$k^{n-1}$$ nodes with each node having $$k$$ edges. It turns out this graph always has an Eulerian circuit (path starting where it ends.) We should visit each node in "post-order" so as to not get stuck in the graph prematurely.


Accepted
22,270
Submissions
45,333

 * SOLUTION
 * ===============================================================================
 *
 * This can be modeled as a directed graph, the key is defining vertices and edges.
 *
 * If we define vertices to be valid combinations of length n, then the problem is
 * Hamilton path to visit each vertex once, which is NP hard.
 * However, wen can define a vertex as combination of length n-1, and an edge as
 * a single digit. In this way, a vertex and an edge forms a combination.
 * And we will try to visit all edges just once: Euler path!
 *
 * 1. Euler path - vertex as n-1 digits, edge as 1 digit - dfs
 *
 * Whether Euler path exists can be determined within O(V+E):
 *      every vertex must have indegree equal to outdegree.
 *
 * Apparently in such directed graph each vertex has its indegree equal to outdegree.
 *
 * Complexity:
 *
 * O()
 *
 * Reference:
 * This is actually De Bruijn sequence(https://en.wikipedia.org/wiki/De_Bruijn_sequence).
 *
 */

#include <debug.hpp>

class Solution {
public:
    string crackSafe(int n, int k) {
        string result = crackSafeEulerPath(n, k);

        cout << n << " " << k << " " << result << endl;

        return result;
    }

    int dfsEulerPath(vector<char> vertex, vector<char> &trail) {
        // FIXME: not that fast, took 36ms
        if (trail.size() == lenTrail) return true;
        for (int i = 0; i < k; ++i) {
            char edge = '0' + i; // a single digit
            string combination = string(vertex.begin(), vertex.end()) + edge;
            if (visited.count(combination)) {
                continue; // Euler path: visit each edge just once
            }
            //cout << "combination:  " << combination << endl;
            vector<char> u(combination.begin(), combination.end()); // neighbour vertex
            u.erase(u.begin());

            //vector<char> u(vertex.begin() + 1, vertex.end()); // new vertex
            //u.push_back(edge); // n == 1?
            visited.insert(combination); // color: visit state
            trail.push_back(edge); // trial
            if (dfsEulerPath(u, trail)) return true; // found a Euler path
            trail.erase(trail.end()-1); // backtrack, restoring state
            visited.erase(combination);
        }

        return false;
    }

    string crackSafeEulerPath(int n, int k) {
        if (k <= 0 || n <= 0) return "";
        this->n = n, this->k = k;
        this->lenTrail = pow(k, n);
        this->visited.clear();

        vector<char> trail; // single digit, form a combination with a vertex
        //unordered_set<string> visited; // visited edges
        vector<char> vertex(n-1, '0');
        // TODO: faster Euler path algorithm?
        dfsEulerPath(vertex, trail);

        //cout << trail << endl;
        //cout << visited << endl;

        string result = string(vertex.begin(), vertex.end()); // concatenate result
        result.insert(result.end(), trail.begin(), trail.end());

        return result;
    }

    int n = 0, k = 0;
    unordered_set<string> visited;
    unsigned int lenTrail = 0;
};

int test() {
    Solution solution;

    int n, k;
    string output;

    n = 1, k = 1; // '', 0
    output = "0";
    assert(solution.crackSafe(n, k) == output);

    n = 1, k = 2; // '', 0, '', 1
    output = "01";
    assert(solution.crackSafe(n, k) == output);

    n = 2, k = 2;
    output = "00110";
    assert(solution.crackSafe(n, k) == output);

    n = 4, k = 2;
    (solution.crackSafe(n, k) == output);
    //assert(solution.crackSafe(n, k) == output);

    n = 4, k = 4;
    (solution.crackSafe(n, k) == output);
    //assert(solution.crackSafe(n, k) == output);

    n = 2, k = 10;
    (solution.crackSafe(n, k) == output);
    //assert(solution.crackSafe(n, k) == output);

    //n = 4, k = 10;
    //(solution.crackSafe(n, k) == output);
    //assert(solution.crackSafe(n, k) == output);

    cout << "test passed" << endl;

    return 0;
}

int main() {
    test();
    return 0;
}
