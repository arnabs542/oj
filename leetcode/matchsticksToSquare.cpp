/*
 *
473. Matchsticks to Square

Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
Note:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.

==============================================================================================
SOLUTION

This is apparently a combinatorics problem, which illustrate a GRAPH STRUCTURE, which can
be treated with graph search (depth first search or breadth first search) or dynamic programming.

1. Graph search
dfs

1)
This combinatoric problem resembles the combination sum problem or 0-1 knapsack problem. The only
difference is that we have several search sub-goals: find four subsets that sum up to the same value.

Several search goals indicate another dimension of state, so be it!

Define state as a tuple of:
    (target sum, available elements, subsets)
    - target sum: side length, target sum of current combination/subset to search for.
    - available elements: unused elements that are available for constructing a combination
    - matches: number of subsets summing up to target to match. It indicates which side of the
    square we are constructing. This is the extra dimension of state compared to
    combination sum problem.

Since we have four sides of a square, we have four subsets to search, of sum of the same value.
So total subsets can be reduced to three because using up all matchsticks.

A combinatoric problem should be treated avoiding involving duplicate computations, otherwise
it is reduced to permutation problem.
To avoid duplicate, we have restrict the elements are chosen in order during each search subset.

But four subsets elements may be interleaving, so we need to reset some variables when moving to
next subsets.

Complexity: O(exponential), O(N) + O(?)

2) sequential selection - space optimization

The above solution needs auxiliary hash table to mark the status that whether an element is used
or not.

How about inplace representation optimization?
The above solution do the graph search in a subset-wise process.

We can inspect the problem in another perspective.
The problem can be viewed in a element-wise process.

For each element, there are four possible situations:
  subset/side 1, subset/side 2, ..., subset/side 4.

Then construct four subsets for each element to fill in. Then do graph search, each time add an
element to one of four subsets, the termination condition is when four subsets sum up to same value.

state = (global: sums of four subsets, available element starting index)


2. Dynamic programming?
Does this problem illustrate optimal substructure?

3. Maybe iterative dfs?


 */

#include <debug.hpp>
#include <algorithm>
#include <assert.h>
#include <iostream>
#include <functional>
#include <algorithm>
#include <numeric>
#include <map>
#include <vector>

using namespace std;

class Solution {
public:
    bool makesquare(vector<int>& nums)
    {
        bool result;
        //result = _makesqureDfs(nums);
        //result = _makesquareDfsElementwise(nums);
        //result = _makesquareDfsElementwise2(nums);
        result = _makesquareDfsElementwiseWithoutClosure(nums);
        //result = makesquare2(nums);

        cout << "result: " << result << ", nums: " << to_string(nums) << endl;
        return result;
    }

    /*
     * Fill four subsets one by one.
     *
     * 109ms, bests 32.67%
     */
    bool _makesqureDfs(vector<int>& nums) {
        int perimeter = accumulate(nums.begin(), nums.end(), 0);
        if (perimeter % 4 != 0 || perimeter == 0) {
            cout << "input illegal!" << endl;
            return false;
        }
        int sideLength = perimeter / 4;

        map<int, bool> visited;
        function<bool(int target, int start, int matches)> dfs = [&](int target, int start, int matches) -> bool {
            if (target < 0 || matches < 0) { return false; }
            //while (target == 0) { // if allowing zero perimeter square
            if (target == 0) { // matches search goal, new matches
                --matches;
                target = sideLength;
                start = 0;
            }
            if (matches == 0) { return true; } // grand search goal
            for (int i = start; i < (int)nums.size(); ++i) {
                if (visited[i]) { continue; }
                visited[i] = true;
                if(dfs(target - nums[i], i + 1, matches)) return true;
                visited[i] = false;
            }
            return false;
        };


        int target = sideLength;
        int start = 0;
        int matches = 3;

        bool result = dfs(target, start, matches);

        return result;
    }

    /*
     *
     */
    bool _makesquareDfsElementwise(vector<int>& nums) {
        int perimeter = accumulate(nums.begin(), nums.end(), 0);
        if (perimeter % 4 != 0 || perimeter == 0) {
            return false;
        }
        int sideLength = perimeter / 4;

        vector<int> sums(4, sideLength);
        function<bool(int start)> dfs = [&](int start) -> bool {
            if (start >= (int)nums.size()) {
                return sums[0] == sums[1] && sums[1] == sums[2] && sums[2] == sums[3] && sums[3] == 0;
            }
            for (int i = 0; i < (int)sums.size(); ++i) {
                if (nums[start] > sums[i]) { continue; } // XXX: prune invalid subset sum
                //for (int j = 0; j <= i; ++j) {
                    //if (sums[i] == sums[j]) continue;
                //} // XXX: prune duplicate permutation of subsets

                int j = i;
                while (--j >= 0) // while loop is faster than for, why?
                    if (sums[i] == sums[j]) break;
                sums[i] -= nums[start];
                if (dfs(start + 1)) { return true; }
                sums[i] += nums[start];
            }
            return false;
        };

        // XXX: reverse sorting avoids the worst case, why? Because it will be earlier to
        // return false for nums with very large number.
        sort(nums.begin(), nums.end(), [](const int &l, const int &r){return l > r;});
        return dfs(0);
    }

    bool _makesquareDfsElementwise2(vector<int>& nums) {
        int perimeter = accumulate(nums.begin(), nums.end(), 0);
        if (perimeter % 4 != 0 || perimeter == 0) {
            return false;
        }
        int sideLength = perimeter / 4;

        vector<int> sums(4, sideLength);
        class Dfs {
            public:
            bool operator() (int start, vector<int> &nums, vector<int> &sums) {
            if (start >= (int)nums.size()) {
                return sums[0] == sums[1] && sums[1] == sums[2] && sums[2] == sums[3] && sums[3] == 0;
            }
            for (int i = 0; i < (int)sums.size(); ++i) {
                if (nums[start] > sums[i]) { continue; } // XXX: prune invalid subset sum

                int j = i;
                while (--j >= 0) // while loop is faster than for, why?
                    if (sums[i] == sums[j]) break; // XXX: prune duplicate permutation of subsets
                sums[i] -= nums[start];
                if (operator()(start + 1, nums, sums)) { return true; }
                sums[i] += nums[start];
            }
            return false;
            }
        };
        sort(nums.begin(), nums.end(), [](const int &l, const int &r){return l > r;});
        return Dfs()(0, nums, sums);
    }

    bool dfs (int start, vector<int> &nums, vector<int> &sums) {
            if (start >= (int)nums.size()) {
                return sums[0] == sums[1] && sums[1] == sums[2] && sums[2] == sums[3] && sums[3] == 0;
            }
            for (int i = 0; i < (int)sums.size(); ++i) {
                if (nums[start] > sums[i]) { continue; } // XXX: prune invalid subset sum
                //for (int j = i; j >= i; --j) {
                    //if (sums[i] == sums[j]) continue;
                //}
                int j = i;
                while (--j >= 0) // while loop is faster than for, why?
                    if (sums[i] == sums[j])
                        break;
                if (j != -1) continue; // XXX: prune duplicate permutation of subsets
                sums[i] -= nums[start];
                if (dfs(start + 1, nums, sums)) { return true; }
                sums[i] += nums[start];
            }
            return false;
        };

    /*
     * 6ms, beats 85.10%
     */
    bool _makesquareDfsElementwiseWithoutClosure(vector<int>& nums) {
        int perimeter = accumulate(nums.begin(), nums.end(), 0);
        if (perimeter % 4 != 0 || perimeter == 0) { return false; }

        vector<int> sideLengths(4, perimeter / 4);

        // XXX: reverse sorting avoids the worst case, why?
        sort(nums.begin(), nums.end(), [](const int &l, const int &r){return l > r;});
        return dfs(0, nums, sideLengths);
    }

    // TODO: iterative dfs
};

void test()
{
    Solution solution;

    vector<int> nums;
    nums = {};
    assert(solution.makesquare(nums) == false); // edge case, result depends on definition, both true or false are reasonable

    nums = {0, 0, 0, 0};
    assert(solution.makesquare(nums) == false || true); // edge case, result depends on definition, both true or false are reasonable

    nums = {1, 1, 1};
    assert(solution.makesquare(nums) == false);

    nums = {1, 1, 1, 1};
    assert(solution.makesquare(nums));

    nums = {1, 1, 1, 1, 1};
    assert(solution.makesquare(nums) == false);

    nums = {
        1, 1, 2, 2, 2,
    };
    assert(solution.makesquare(nums));

    nums = {
        3, 3, 3, 3, 4,
    };
    assert(solution.makesquare(nums) == false);

    nums = {
        3, 3, 3, 3, 4000000,
    };
    assert(solution.makesquare(nums) == false);

    nums = {
        3, 3, 3, 3, 4, 1, 2, 2, 3, 4,
    };
    assert(solution.makesquare(nums));

    nums = {
        1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2,
    };
    assert(solution.makesquare(nums));

    nums = {
        1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2,
    };
    assert(solution.makesquare(nums));

    nums = {
        12,8,12,16,20,24,28,32,36,40,44,48,52,56,60,
    };
    assert(solution.makesquare(nums) == false);

    cout << "self test passed" << endl;
}

int main()
{
    test();
}
