/**
 *
421. Maximum XOR of Two Numbers in an Array

Total Accepted: 8291
Total Submissions: 19023
Difficulty: Medium
Contributors: shen5630

Given a non-empty array of numbers, a₀, a₁, a₂, … , a_{n-1}, where 0 ≤ aᵢ < 2^31.

Find the maximum result of aᵢ XOR aⱼ, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.

================================================================================
SOLUTION

1. Naive solution - element-wise

Compute pair-wise XOR result, take the maximum.

Complexity: O(N²), O(1).

2. Search in value space and verify

Complexity: O(N), O(1)

3. Prefix tree trie

Complexity: O(N), O(N)

 *
 */
#include <debug.hpp>

#include <vector>
#include <map>
#include <set>
#include <unordered_set>
#include <algorithm>
#include <iostream>
#include <assert.h>

using namespace std;

class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        int result = findMaximumXORBitwiseGreedy(nums);

        cout << nums << " => " << result << endl;
        return result;
    }

    int findMaximumXORBitwiseGreedy(vector<int>& nums) {
        int prefix = 0, mask = 0; // prefix: xor result prefix, mask: bitwise mask
        set<int> exist; // for verifying existence in linear time
        for (int i = 31; i >= 0; --i) // dfs with pruning, without backtracking!
        {
            mask |= 1 << i;
            prefix |= 1 << i; // set current
            exist.clear();
            size_t j = 0;
            for (; j < nums.size(); ++j)
            {
                if (exist.find(nums[j] & mask) != exist.end()) { break; }
                exist.insert((nums[j] & mask) ^ prefix); // x ^ b = a => x ^ a = b
            }
            if (j == nums.size())
            {
                prefix ^= 1 << i; // such XOR prefix test filed, unset current bit
            }
        }

        return prefix;
    }

};

int test()
{
    Solution solution;
    vector<int> input;
    int result;
    //vector<pair<vector<int>, int>> cases {
        //{make_pair(vector<int>{}, 0)},
        //{make_pair(vector<int>{1}, 0)},
        //{make_pair(vector<int>{1, 2}, 3)},
        //{make_pair(vector<int>{3, 10, 5, 25, 2, 8}, 28)},
    //};
    //for (auto item: cases)
    //{
        //assert(solution.findMaximumXOR(item.first) == item.second);
    //}

    input = vector<int>{};
    result = 0;
    assert(solution.findMaximumXOR(input) == 0);

    input = vector<int>{1};
    result = 0;
    assert(solution.findMaximumXOR(input) == result);

    input = vector<int>{1, 2};
    result = 3;
    assert(solution.findMaximumXOR(input) == result);

    input = vector<int>{3, 10, 5, 25, 2, 8};
    result = 28;
    assert(solution.findMaximumXOR(input) == result);

    return 0;
}

int main(int argc, char *argv[])
{
    int rtn = test();

    return rtn;
}
