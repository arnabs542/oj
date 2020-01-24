/**
 *
528. Random Pick with Weight
Medium

Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.

Accepted
48.8K
Submissions
112.6K

================================================================================
SOLUTION

Sample within range of weight prefix sum: [1, max sum], and search for upper bound.
Corner case:
1) weight = 0, not possible
2) max sum is very large?

For every sample value v, the objective is:
    find such i that ps[i] <= target < ps[i+1];
Then return index i;

How to search for such upper bound? Use binary search!

 *
 */

#include <debug.hpp>
#include <random>

class Solution {
public:
    Solution(vector<int>& w) {
        for (int i = 0; i < (int)w.size(); ++i) {
            ps.push_back((ps.empty() ? 0:ps.back()) + w[i]);
        }

        // can be removed if using std::uniform_int_distribution<>.
        if (ps[ps.size() - 1]  > RAND_MAX) {
            float r = RAND_MAX/ps[ps.size() - 1];
            for (int i = 0; i < (int)ps.size(); ++i) {
                ps[i] *= r;
            }
        }
    }

    int pickIndex() {
        int result = pickIndexPrefiSumUpperBound();

        return result;
    }


    int pickIndexPrefixSumUpperBound2() {
        // generate uniform distribution with builtin methods.
        std::random_device rd;  //Will be used to obtain a seed for the random number engine
        std::mt19937 gen(rd()); //Standard mersenne_twister_engine seeded with rd()
        std::uniform_int_distribution<> dis(0, ps[ps.size() - 1] - 1); // sample in [0, max sum - 1]
        int v  = dis(gen);
        auto itr = std::upper_bound(ps.begin(), ps.end(), v);

        return itr-ps.begin();
    }

    int pickIndexPrefiSumUpperBound() {
        int v = rand() % ps[ps.size() - 1] + 1; // sample in [1, max sum];
        int low = 0, high = ps.size() - 1;
        // cout << v  << endl;
        // objective: find upper bound i such that ps[i-1] < target <= ps[i]
        while (low <= high) {
            int mid = (low + high) >> 1;
            if (ps[mid] == v) {
                return mid;
            } else if (ps[mid] < v) {
                low = mid + 1;
            } else if (ps[mid] > v) {
                high = mid - 1;
            }
        }

        // XXX: return low or high?
        return low; // low-1=high, meaning ps[low] > v > ps[high], return low?
    }
    // vector<int> w;
    vector<int> ps; // prefix sum
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */

int test() {
    return 0;
}

int main() {
    test();
    return 0;
}
