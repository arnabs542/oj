#include <debug.hpp>


class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        int result = findMaximumXORDfs(nums);

        cout << result << endl;

        return result;
    }

    int findMaximumXORDfs(vector<int>& nums) {
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

int main(int argc, char *argv[])
{
    Solution solution;
    vector<int> input;
    int result;
    vector<pair<vector<int>, int>> cases {
        {make_pair(vector<int>{}, 0)},
        {make_pair(vector<int>{1}, 0)},
        {make_pair(vector<int>{1, 2}, 3)},
        {make_pair(vector<int>{3, 10, 5, 25, 2, 8}, 28)},
    };
    for (auto item: cases)
    {
        assert(solution.findMaximumXOR(item.first) == item.second);
    }
    return 0;
}
