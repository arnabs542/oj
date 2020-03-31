/**
 *
774. Minimize Max Distance to Gas Station
Difficulty:
Hard


On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1], where N = stations.length.

Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.

Return the smallest possible value of D.

Example:

Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
Output: 0.500000
Note:

stations.length will be an integer in range [10, 2000].
stations[i] will be an integer in range [0, 10^8].
K will be an integer in range [1, 10^6].
Answers within 10^-6 of the true value will be accepted as correct.

================================================================================
SOLUTION

An intuition is to add gas stations to adjacent stations of max distance.
But how to proceed? Stuck...

What's the mathematical objective of this problem?
There are n intervals with n distances given by n stations, and we want allocate
k extra stations to minimize max distance.

Objective:
    minimize{max{dᵢ/(kᵢ+1)}}, subject to Σkᵢ=K, 0<=kᵢ<=K,
    where dᵢ is the distance from stations[i] to statations[i+1].

So this is a combinatorial optimization problem!

1. Graph search on search space (k₁, k₂, ..., k_{n-1}).

The search process can be performed with depth first search or breadth first search.
This is brute force search involving lots of duplicate computations.

Complexity: O(2ⁿ)
To reduce the combinatorial complexity, we can memoize on state (n, k).

2. Dynamic programming - memoization
The combinatorial optimization model is similar to knapsack problem.
Define state: f(n, k) optimal solution given (n, k).
State transition: f(n, k) = min{max(f(n-1, k-m), d_n/(1+m))}, where 0<=m<=k.

Complexity: O(nk²)

3. Greedy strategy
Dynamic programming solution can be optimized to greedy strategy, by
exploiting optimal substructure, making a locally optimal choice instead of
iterating all possible choices.

Greedy strategy: add a station between two stations of max distance so far.

Why it works?
Suppose we have k gas stations added so far, and we need to add more stations.
Then the optimal solution must be adding one station between two stations of
maximum distance.

Proof
Suppose the adjacent two stations of maximum distance is:
    max(d[])=dⱼ=(stations[j]-stations[j-1])/(m+1), where m is stations added between before.
If we don't add station between j-1 and j, and there is a better solution by not
adding a station between j-1 and j.
Then for the optimal solution, we have max(d') < dⱼ.
But dⱼ is the maximum value, so dⱼ = max(d') > max(d').
Contradict!

Implementation
Keep track of a max heap, keyed by (d: evenly cut distance, m: number of gas stations added).
For i = 1, ..., k:
    Pop heap top, and insert (d*m/(m+1), m+1).
pass
return heap top distance

TODO:
Complexity: O(KlogN + NlogN)


4. Range value space search
What's the range space of minimal maximal distance? (0, max(d)).

Then we can binary search in the value space, and verify whether it's possible.
To verify for (n, k, d), iterate all stations, and see how many stations need to be
added between j-1 and j. If we need more stations quota, then it's not possible.

Complexity: O(NlogD), where D is the maximum distance between adjacent stations given.


 *
 */

#include <debug.hpp>

class Solution {
public:
    float minDistance(vector<int> &nums, int K) {
        float result;

        result = minDistanceDP(nums, K);
        cout << nums << " " << K << " " << result << endl;

        return result;
    }

    float minDistanceDP(vector<int> &nums, int K) {
        int n = (int)nums.size();
        vector<vector<double>> f(n+1, vector<double>(K+1, 0.));
        // init
        for (int i = 2; i <= n; ++i) {
            for (int k = 0; k <= K; ++k) {
                f[i][k] = max(double(nums[i-1] - nums[i-2]), f[i-1][k]);
            }
        }
        for (int i = 2; i <= n; ++i) {
            for (int k = 0; k <= K; ++k) {
                //double dis = f[i][k]; // min, max
                for (int j = 0; j <= k; ++j) {
                    f[i][k] = std::min(f[i][k], std::max(f[i-1][k-j], (double)(nums[i-1]-nums[i-2])/(j+1.0))); // XXX: beware typo k, K
                }
            }
        }

        //cout << f << endl;

        return f[n][K];
    }
};

int test() {
    vector<int> nums;
    double output;
    int k = 0;

    Solution solution;

    nums = {};
    k = 0;
    output = 0;
    assert(abs(solution.minDistance(nums, k ) - output) < 1e-6);


    nums = {1};
    k = 0;
    output = 0;
    assert(abs(solution.minDistance(nums, k ) - output) < 1e-6);

    nums = {1, 2};
    k = 0;
    output = 1;
    assert(abs(solution.minDistance(nums, k ) - output) < 1e-6);

    nums = {1, 2};
    k = 1;
    output = 0.5;
    assert(abs(solution.minDistance(nums, k ) - output) < 1e-6);

    nums = {1, 2, 3};
    k = 1;
    output = 1;
    assert(abs(solution.minDistance(nums, k ) - output) < 1e-6);

    nums = {1, 2, 102};
    k = 9;
    output = 10;
    assert(abs(solution.minDistance(nums, k ) - output) < 1e-6);

    nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    k = 1;
    output = 1;
    assert(abs(solution.minDistance(nums, k ) - output) < 1e-6);

    nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    k = 1;
    output = 1;
    assert(abs(solution.minDistance(nums, k ) - output) < 1e-6);

    nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    k = 9;
    output = 0.5;
    assert(abs(solution.minDistance(nums, k ) - output) < 1e-6);


    cout << "test passed" << endl;
    return 0;
}

int main(int argc, char **argv) {
    // TODO: submit
    test();
    return 0;
}
