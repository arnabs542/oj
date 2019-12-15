/**
 *
1004.Max Consecutive Ones III

Medium

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s.



Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation:
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation:
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.


Note:

1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1
SOLUTION
================================================================================

This is a follow up of max consecutive ones ii, and similar to
'buy and sell stock K times'.

1. Brute force - exhaust windows with at most K zeroes and verify

Complexity: O(N²)

2. Dynamic programming - Keep track of max ending here, with additional state of number of flips

Define state of multivariate: f[k][i] = optimal solution ending here i with k flips.
State transition for :
    if nums[i] == 0:
        f[k][i] = f[k-1][i-1] + 1
        ...
        f[0][i] = 0
    if nums[i]] == 1:
        f[k][i] += 1
        ...
        f[0][i] += 1

Complexity: O(KN) = O(N)

3. Sliding window - Keep track of max ending here

State transition: expand or shrink the sliding window

Complexity: O(N)

 *
 */

#include <debug.hpp>

class Solution {
public:
    int longestOnes(vector<int>& nums, int K) {
        int result;
        //result = findMaxConsecutiveOnesDynamicProgrammingMaxEndingHere(nums, K);
        result = findMaxConsecutiveOnesSlidingWindowMaxEndingHere(nums, K);

        cout << nums << " => " << result << endl;

        return result;
    }

    int findMaxConsecutiveOnesSlidingWindowMaxEndingHere(vector<int> &nums, int K) {
        int maxSoFar = 0, maxEndingHere = 0;
        int nZeroes = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (nums[i] == 1) {
                ++maxEndingHere;
            } else {
                ++nZeroes;
                ++maxEndingHere;
                while (nZeroes > K) {
                    if (nums[i - --maxEndingHere] == 0) {
                        nZeroes -= 1;
                    }
                }
            }
            maxSoFar = std::max(maxSoFar, maxEndingHere);
        }

        return maxSoFar;
    }

    // XXX: time limit exceeded
    int findMaxConsecutiveOnesDynamicProgrammingMaxEndingHere(vector<int>& nums, int K) {
        int maxSoFar = 0;
        vector<int> maxEndingHere(K + 1, 0);
        for (int i = 0; i < (int) nums.size(); ++i) {
            if (nums[i] == 0) {
                for (int j = K; j > 0; --j) {
                    maxEndingHere[j] = maxEndingHere[j-1] + 1; // flip one more time
                }
                maxEndingHere[0] = 0; // no flip
            } else {
                for (int j = K; j >= 0; --j) {
                    maxEndingHere[j] += 1; // no need to flip
                }
            }

            maxSoFar = std::max(*std::max_element(maxEndingHere.begin(), maxEndingHere.end()), maxSoFar);
        }

        return maxSoFar;
    }

};

int test() {

    vector<int> nums;
    int K = 0;
    int result;

    Solution solution;

    nums = {};
    K = 4;
    result = 0;
    assert(solution.longestOnes(nums, K) == result);

    nums = {0};
    K = 1;
    result = 1;
    assert(solution.longestOnes(nums, K) == result);

    nums = {1};
    K = 1;
    result = 1;
    assert(solution.longestOnes(nums, K) == result);


    nums = {1, 0, 1, 1};
    K = 1;
    result = 4;
    assert(solution.longestOnes(nums, K) == result);

    nums = {1, 0, 1, 1, 0};
    K = 1;
    result = 4;
    assert(solution.longestOnes(nums, K) == result);

    nums = {1,1,0,1,1,1};
    K = 1;
    result = 6;
    assert(solution.longestOnes(nums, K) == result);

    nums = {1,1,1,0,0,0,1,1,1,1,0};
    K = 2;
    result = 6;
    assert(solution.longestOnes(nums, K) == result);

    nums = {0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1};
    K = 3;
    result = 10;
    assert(solution.longestOnes(nums, K) == result);

    nums = {0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1};
    K = 0;
    result = 4;
    assert(solution.longestOnes(nums, K) == result);

    cout << "self test passed!" << endl;

    return 0;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
