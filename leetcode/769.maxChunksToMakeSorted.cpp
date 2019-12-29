/**
 *
769. Max Chunks To Make Sorted
Medium

Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
Note:

arr will have length in range [1, 10].
arr[i] will be a permutation of [0, 1, ..., arr.length - 1].


Accepted
30.2K
Submissions
56.6K

SOLUTION
================================================================================

Analyze the simplest situation:
1) arr is already sorted: answer is n.
2) arr is reversely sorted: answer is n.

Why?
Every such chunk s=arr[i...j] must meet requirement:
min(s) > max(arr[...i-1]) and max(s) < min(arr[j...]).

1. Brute force
Exhaust and verify.

Complexity: O(2ⁿ).

2. Dynamic programming
Define state f[n]: max chunks to make sorted ending here at n.
State transition:
    f[n] = max(f[i] + 1), where i in [0, n-1] and min(arr[i+1,...n]) > max[arr[...i]].

Complexity: O(N²)

0 1 2 3 4
4 3 2 1 0
0 1 4 2 3
1 0 4 2 3

3. Dynamic programming optimized
The values are in range [0, n-1], so max(arr[...i]) must be i.

 *
 */

#include <debug.hpp>

class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int result;
        result = maxChunksToSortedDynamicProgramming(arr);

        cout << arr << " =>" << result << endl;

        return result;
    }

    int maxChunksToSortedDynamicProgramming(vector<int> &arr) {
        const int n = arr.size();
        vector<int> maxEndingHereChunks(n + 1, 0);

        vector<int> maxSoFar(n + 1, std::numeric_limits<int>::min());
        for (int i = 1; i <= n; ++i) {
            maxSoFar[i] = std::max(maxSoFar[i-1], arr[i-1]);
        }

        for (int i = 1; i <= n; ++i) {
            int minSoFar = arr[i - 1];
            for (int j = i; j >= 1; --j) {
                minSoFar = std::min(minSoFar, arr[j-1]);
                if (minSoFar > maxSoFar[j-1]) {
                    maxEndingHereChunks[i] = std::max(maxEndingHereChunks[j-1] + 1,
                            maxEndingHereChunks[i]);
                    break; // XXX: if f[i] > f[j] for i > j, then there must be smaller elements then a[i-1], between i+1 and j. And in such case if branch never entered!
                }
            }
        }

        return maxEndingHereChunks[n];
    }
};


int test() {
    vector<int> arr;
    int result;

    Solution solution;

    arr = {};
    result = 0;
    assert(solution.maxChunksToSorted(arr) == result);

    arr = {1};
    result = 1;
    assert(solution.maxChunksToSorted(arr) == result);

    arr = {4, 3, 2, 1, 0};
    result = 1;
    assert(solution.maxChunksToSorted(arr) == result);

    arr = {0, 1, 2, 3, 4};
    result = 5;
    assert(solution.maxChunksToSorted(arr) == result);

    cout << "test passed!" << endl;

    return 0;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
