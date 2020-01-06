/**
 *
485. Max Consecutive Ones
Easy

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

Accepted
162.3K
Submissions
290.5K

Hint:
You need to think about two things as far as any window is concerned. One is the starting point for the window. How do you detect that a new window of 1s has started? The next part is detecting the ending point for this window. How do you detect the ending point for an existing window? If you figure these two things out, you will be able to detect the windows of consecutive ones. All that remains afterward is to find the longest such window and return the size.

SOLUTION
================================================================================

1. Brute force - finding windows in a sliding window manner

Complexity: O(N)

2. Dynamic programming - Keep track of state of max length ending here

Complexity: O(N)

 *
 *
 */

#include <debug.hpp>

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int result;
        //result = findMaxConsecutiveOnesSlidingWindow(nums);
        result = findMaxConsecutiveOnesEndingHere(nums);

        cout << nums << " => " << result << endl;

        return result;
    }

    int findMaxConsecutiveOnesSlidingWindow(vector<int> &nums) {
        int result = 0;
        int i = 0, j = 0;
        while (i < (int) nums.size()) {
            // locate window starting index, of 1
            while ( i < (int)nums.size() && nums[i] == 0) ++i; // XXX: check range first
            // locate window ending index, of non 1
            for (j = i; j < (int)nums.size() && nums[j] == 1 ; ++j);
            result = std::max(result, j - i);

            i = j + 1; // set next offset
        }
        return result;
    }

    int findMaxConsecutiveOnesEndingHere(vector<int> &nums) {
        int maxSoFar = 0, maxEndingHere = 0; // globally and locally optimal

        for (int i = 0; i < (int) nums.size(); ++i) {
            if (nums[i] == 0) {
                maxEndingHere = 0;
            } else {
                maxSoFar = std::max(maxSoFar, ++maxEndingHere);
            }
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
    result = 0;
    assert(solution.findMaxConsecutiveOnes(nums) == result);

    nums = {1};
    result = 1;
    assert(solution.findMaxConsecutiveOnes(nums) == result);

    nums = {1,1,0,1,1,1};
    result = 3;
    assert(solution.findMaxConsecutiveOnes(nums) == result);

    cout << "self test passed!" << endl;

    return 0;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
