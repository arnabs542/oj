/**
 *
487.Max Consecutive Ones II

Medium

Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

Follow up:
What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?

SOLUTION
================================================================================

This is a follow up of max consecutive ones ii, and similar to
'buy and sell stock k times'.

1. Brute force - exhaust windows with at most 1 zero and verify

Complexity: O(N²), or O(N) in a sliding window manner

2. Dynamic programming - Keep track of max ending here, with additional state of number of flips

Complexity: O(2N) = O(N)

 *
 */

#include <debug.hpp>

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int result;
        result = findMaxConsecutiveOnesMaxEndingHere(nums);

        cout << nums << " => " << result << endl;

        return result;
    }

    int findMaxConsecutiveOnesMaxEndingHere(vector<int>& nums) {
        int maxSoFar = 0;
        vector<int> maxEndingHere(2, 0);
        for (int i = 0; i < (int) nums.size(); ++i) {
            if (nums[i] == 0) {
                maxEndingHere[1] = maxEndingHere[0] + 1; // flip once
                maxEndingHere[0] = 0; // no flip
            } else {
                ++maxEndingHere[1];
                ++maxEndingHere[0];
            }

            maxSoFar = std::max(*std::max_element(maxEndingHere.begin(), maxEndingHere.end()), maxSoFar);
        }

        return maxSoFar;
    }

};

int test() {

    vector<int> nums;
    int result;

    Solution solution;

    nums = {};
    result = 0;
    assert(solution.findMaxConsecutiveOnes(nums) == result);

    nums = {0};
    result = 1;
    assert(solution.findMaxConsecutiveOnes(nums) == result);

    nums = {1};
    result = 1;
    assert(solution.findMaxConsecutiveOnes(nums) == result);

    nums = {1, 0, 1, 1, 0};
    result = 4;
    assert(solution.findMaxConsecutiveOnes(nums) == result);

    nums = {1,1,0,1,1,1};
    result = 6;
    assert(solution.findMaxConsecutiveOnes(nums) == result);

    cout << "self test passed!" << endl;

    return 0;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
