/**
 *
179. Largest Number
Medium

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.

Accepted
155.8K
Submissions
571.5K

================================================================================
SOLUTION

 *
 *
 */

#include <debug.hpp>

class Solution {
public:
    string largestNumber(vector<int>& nums) {
        string result;
        result = largestNumberLexicographicalSort(nums);

        cout << nums << " => " << result << endl;

        return result;
    }

    string largestNumberLexicographicalSort(vector<int>& nums) {
        vector<string> arr; // vector of strings
        for (uint i = 0; i < nums.size(); ++i) {
            arr.push_back(to_string(nums[i]));
        }
        sort(arr.begin(), arr.end(), [](string &s1, string &s2) {return s1+s2 > s2+s1;}); // decreasing order
        string result;
        for (const string &s: arr) { result += s; }
        if (result.size() && result[0] == '0') return "0";
        // uint i = 0;
        // while (i + 1 < result.size() && result[i] == '0') { ++i; }
        // if (i > 0) { result.erase(result.begin(), result.begin() + i); }

        return result;
    }
};

int test() {

    return 0;
}

int main(int argc, char **argv) {
    test();

    return 0;
}
