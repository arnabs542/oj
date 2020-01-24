/**
 *
768. Max Chunks To Make Sorted II
Hard

This question is the same as "Max Chunks to Make Sorted" except the integers of the given array are not necessarily distinct, the input array could be up to length 2000, and the elements could be up to 10**8.

Given an array arr of integers (not necessarily distinct), we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
Example 2:

Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
Note:

arr will have length in range [1, 2000].
arr[i] will be an integer in range [0, 10**8].


Accepted
16.3K
Submissions
34.3K

SOLUTION
================================================================================

1. Brute force

Exhaust and verify.

Complexity: O(2ⁿ).

2. Dynamic programming
Like 'max chunks to make sorted'.

Define state f[n]: max chunks to make sorted ending here at n.
State transition:
    f[n] = max(f[i] + 1), where i in [0, n-1] and min(arr[i+1,...n]) > max[arr[...i]].

Complexity: O(N²).

3. Dynamic programming optimized
In the state transition relation,
    f[n] = max(f[i] + 1), where i in [0, n-1] and min(arr[i+1,...n]) > max[arr[...i]].
do we have to iterate all i in [0, n-1] once we found such i?
For i > j, if f[i] > f[j], then there must be such j<k<i that arr[k] < max(arr[...i]),
otherwise f[i] can't be larger than f[j].
But if arr[k] < arr[i] exists, min(arr[i+1,...n]) > max[arr[...i]] doesn't hold!
If another word, if we found such i that min(arr[i+1,...n]) > max(arr[...i]),
we don't need to exhaust all i in [0, n-1] once we find the first chunk!

Complexity: O(N), worst case is O(N²) for reversely sorted array.

4. DYNAMIC PROGRAMMING OPTIMIZED TO GREEDY strategy
The dynamic programming approach can be optimized in a greedy way, so we can
just apply greedy strategy.

Complexity: O(N)

5. Interval merging - monotonic stack(increasing)
We can keep track of each chunk represented with a interval.
And the intervals require merging, so a stack will help.

Maintain a monotonic increasing stack of intervals.

Iterate all the numbers, for each number e:
    1) Construct a new interval (e, e)
    2) If stack top (l, h) meets e < h then pop and insert (min(l, e), h).
    Else push (e, e).
Then stack size is max number of chunks.

TODO:

Complexity: O(N)

 *
 *
 */

#include <debug.hpp>

class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int result;
        //result = maxChunksToSortedDynamicProgramming(arr);
        result = maxChunksToSortedGreedyLeftMaxRightMin(arr);
        result = maxChunksToSortedIntervalStack(arr);

        cout << arr << " => " << result << endl;

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
                if (minSoFar >= maxSoFar[j-1]) {
                    maxEndingHereChunks[i] = std::max(maxEndingHereChunks[j-1] + 1,
                            maxEndingHereChunks[i]);
                    break; // early stop. XXX: if f[i] > f[j] for i > j, then there must be smaller elements then a[i-1], between i+1 and j. And in such case if branch never entered!
                }
            }
        }

        return maxEndingHereChunks[n];
    }

    int maxChunksToSortedGreedyLeftMaxRightMin(vector<int> &arr) {
        int result = 0;
        int n = arr.size();
        vector<int> leftMax(n+1, std::numeric_limits<int>::min());
        vector<int> rightMin(n+1, std::numeric_limits<int>::max());
        for (int i = 1; i <= n; ++i) {
            leftMax[i] = std::max(leftMax[i-1], arr[i-1]);
            //leftMax[i] = std::max(leftMax[i], arr[i-1]);
        }
        for (int i = n-1; i >= 0; --i) {
            //rightMin[i] = std::min(rightMin[i], arr[i]);
            rightMin[i] = std::min(rightMin[i+1], arr[i]); // XXX:i+1...
        }
        //cout << leftMax << endl;
        //cout << rightMin << endl;
        for (int i = 0; i < n; ++i) {
            if (leftMax[i+1] <= rightMin[i+1]) {
                //cout << i + 1 << "" << endl;
                ++result;
            }
        }

        return result;
    }

    int maxChunksToSortedIntervalStack(vector<int> &arr) {
        stack<pair<int, int>> filo;
        int n = arr.size();
        for (int i = 0; i < n; ++i) {
            int high = arr[i];
            while (!filo.empty() && filo.top().second > arr[i]) {
                pair<int, int> interval0 = filo.top(); filo.pop();
                high = std::max(high, interval0.second);
            }
            filo.push({arr[i], high});
        }

        return filo.size();
    }
};

int test() {

    Solution solution;
    vector<int> arr;
    int result;

    arr = {};
    result = 0;
    assert(solution.maxChunksToSorted(arr) == result);

    arr = {1};
    result = 1;
    assert(solution.maxChunksToSorted(arr) == result);

    arr = {1,1,1,1};
    result = 4;
    assert(solution.maxChunksToSorted(arr) == result);

    arr = {2, 1, 3, 4, 4}; // 1, 1, 2, 3, 4
    result = 4;
    assert(solution.maxChunksToSorted(arr) == result);

    arr = {2, 3, 3, 1, 4}; // 1, 2, 3, 1, 1
    // left max:  #, 2, 3, 3, 3, 4
    // right min: 1, 1, 1, 1, 4, #
    result = 2;
    assert(solution.maxChunksToSorted(arr) == result);

    arr = {2, 3, 1}; // 1, 2, 1
    result = 1;
    assert(solution.maxChunksToSorted(arr) == result);

    arr = {2, 3, 1, 3, 4}; // 1, 2, 1, 2, 3
    result = 3;
    assert(solution.maxChunksToSorted(arr) == result);

    //arr = {2, 3, 4, 1, 5, 6, 7};
    arr = {4, 3, 2, 3};
    result = 1;
    assert(solution.maxChunksToSorted(arr) == result);

    arr = {4, 3, 2, 1, 0};
    result = 1;
    assert(solution.maxChunksToSorted(arr) == result);

    arr = {0, 1, 2, 3, 4};
    result = 5;
    assert(solution.maxChunksToSorted(arr) == result);


    cout << "test passed" << endl;
    return 0;
}

int main(int argc, char **argv) {
    return test();
}
