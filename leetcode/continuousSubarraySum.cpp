/**
 *

523. Continuous Subarray Sum

Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

==============================================================================================
SOLUTION

1. Brute force
Enumerate all possible sub-arrays.

Complexity: O(N²)

2. Sliding window
To maintain a sliding window it's required to know the push and pop condition.

As for the multiple of k, it means the elements composing the sum must have their remainder,
with respect to k, sum to  multiple of k. Then we can replace the element with their remainders.

Then the sum of array will be at most NK, then we have n search goals: K, 1K, ..., NK.
The worst case is degraded to complexity O(N²).

3. Prefix sum
Compute prefix sums, and storing them with into buckets representing remainder modulo by k.

Input:           [23, 2, 4, 6, 7], k = 6
prefix sum:      23, 25, 29, 35, 42
remainder:       5,   1,  5, 5,  0

Complexity: O(N), O(K)

 */

#include <debug.hpp>


class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        bool result = false;
        result = _checkSubarraySumPrefixSum(nums, k);
        cout << "input: " << nums << ", k: " << k << endl;

        return result;
    }

    bool _checkSubarraySumPrefixSum(vector<int>& nums, int k) {
        //vector<int> indices(k, -1); // prefix sum[indices[i]] % k = i
        unordered_map<int, int> indices; // prefix sum[indices[i]] % k = i
        int ps = 0;
        indices.insert(make_pair(0, 0)); // XXX: fatal, initialize {0: 0}!
        for (unsigned int i = 0; i < nums.size(); ++i) {
            ps += nums[i];
            int r = k ? ps % k : ps;

            if (indices.find(r) != indices.end()) {
                if (i + 1 - indices[r] >= 2) {
                    return true;
                }
            } else {
                indices[r] = i + 1;
            }
        }

        return false;
    }

};

void test() {
    Solution solution;

    vector<int> nums;
    int k = 0;

    nums = {};
    k = 0;
    assert(!solution.checkSubarraySum(nums, k));

    nums = {};
    k = 1;
    assert(!solution.checkSubarraySum(nums, k));

    nums = {23, 2, 4, 6, 7};
    k=6;
    assert(solution.checkSubarraySum(nums, k));

    nums = {23, 2, 0, 4, 0, 0, 6, 7};
    k = 0;
    assert(solution.checkSubarraySum(nums, k));

    nums = {0,1,0};
    k = 0;
    assert(!solution.checkSubarraySum(nums, k));

    nums = {0, 0};
    k = 0;
    assert(solution.checkSubarraySum(nums, k));

    cout << "self test passed!" << endl;
}

int main(int argc, char *argv[])
{
    test();
    return 0;
}
