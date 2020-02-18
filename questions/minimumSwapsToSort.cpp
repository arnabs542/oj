/**
 *
 *
Minimum number of swaps required to sort an array
Given an array of n distinct elements, find the minimum number of swaps required to sort the array.

Examples:

Input : {4, 3, 2, 1}
Output : 2
Explanation : Swap index 0 with 3 and 1 with 2 to
              form the sorted array {1, 2, 3, 4}.

Input : {1, 5, 4, 3, 2}
Output : 2

================================================================================
SOLUTION

How is minimum number of swaps is obtained?
Well we don't know the mathematical model yet and how how prove it yet.

Analyze the LOWER BOUND AND UPPER BOUND.
--------------------------------------------------------------------------------

For an already sorted array, minimum number of swaps is 0.

For a completely out of order array(no element is in right place), answer is n.
This is n numbers are all out of order, so we need to at least place them in
the right position, this needs at least n operations of swaps.

Can we develop a algorithm with UPPER BOUND of complexity is N?
Yes, if we already know where each number belongs to!

Dependency graph cycle model
--------------------------------------------------------------------------------
We will have n nodes and an edge directed from node i to node j if the element
at i'th index must be present at j’th index in the sorted array.

And the graph has several non-intersecting cycles. For each cycle, the
minimum number of swaps to make vertices in position is (V-1).

answer = Σi = 1k(cycle_size – 1)
where k is the number of cycles.

How to deal with a duplicate values
--------------------------------------------------------------------------------
If there are duplicate values and some of them are already in position, we can
skip swapping during depth first search in the graph cycle.

1. Sort - follow dependency graph cycle to sort

Complexity: O(NlogN)

2. Sort - but try to restore to original order given list of {value, index}

Scan for sorted list of pair, if a pair is not the same as its original place,
then swap to its original index. Count number of swaps to restore.

Complexity: O(NlogN)


 *
 *
 */
#include <debug.hpp>

class Solution {
public:
    int minSwap(vector<int> &nums) {
        int result;
        result = minSwapDependencyGraphCycle(nums);

        cout << nums << " => " << result << endl;

        return result;
    }

    int minSwapDependencyGraphCycle(vector<int> &nums) {
        int n = nums.size();
        vector<pair<int, int>> valIdx;
        for (int i = 0; i < n; ++i) {
            valIdx.push_back({nums[i], i});
        }
        sort(valIdx.begin(), valIdx.end());
        cout << valIdx << endl;
        vector<int> edges(n, -1); // target indices. XXX: can be removed by restoring the ordered pairs to original order.
        for (int i = 0; i < n; ++i) {
            edges[valIdx[i].second] = i; // source to destination index mapping
        }

        //cout << edges << endl;
        int result = 0;
        vector<int> visited(n, 0);
        for (int i = 0; i < n; ++i) {
            if (visited[i]) continue;
            int u = i;
            int nNodes = 0;
            int nSwaps = 0;
            do { // not cycle entry
                visited[u] = 1; // visited
                int v = edges[u];
                if (nums[u] != nums[v] && v != i) { // swap, u -> v
                    ++nSwaps;
                }
                ++nNodes;
                //cout << u  << " " << nNodes << endl;
                u = v;
            } while (u != i);
            //result += (nNodes - 1);
            result += (nSwaps);
        }

        return result;
    }
};

int test() {
    Solution solution;
    vector<int> nums;
    int output;

    nums = {};
    output = 0;
    assert(solution.minSwap(nums) == output);

    nums = {1};
    output = 0;
    assert(solution.minSwap(nums) == output);

    nums = {2, 1};
    output = 1;
    assert(solution.minSwap(nums) == output);

    nums = {1, 1};
    output = 0;
    assert(solution.minSwap(nums) == output);

    nums = {1, 1, 1};
    output = 0;
    assert(solution.minSwap(nums) == output);

    nums = {1, 1, 1, 0};
    output = 1;
    assert(solution.minSwap(nums) == output);

    nums = {4, 3, 2, 1};
    output = 2;
    assert(solution.minSwap(nums) == output);

    nums = {1, 5, 4, 3, 2};
    output = 2;
    assert(solution.minSwap(nums) == output);

    cout << "test passed" << endl;

    return 0;
}

int main() {
    test();
    return 0;
}
