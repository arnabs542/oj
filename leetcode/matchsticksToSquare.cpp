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

This combinatoric problem resembles the combination sum problem or 0-1 knapsack problem. The only
difference is that we have several search sub-goals: find four subsets that sum up to the same value.

Several search goals indicate another dimension of state, so be it!

Define state as a tuple of:
    (target sum, available elements, subsets)
    - target sum: target sum of the combination in current search subsets
    - available elements: unused elements that are available for constructing a combination
    - matches: number of matching subsets summing up to target to construct. It indicates
    which side of the square we are constructing combinations for, the extra dimension of
    state compared to combination sum problem.

Since we have four sides of a square, we have four subsets to search, of sum of the same value.
So total subsets can be reduced to three because using up all matchsticks.

A combinatoric problem should be treated avoiding involving duplicate computations, otherwise
it is reduced to permutation problem.
To avoid duplicate, we have restrict the elements are chosen in order during each search subset.

But four subsets elements may be interleaving, so we need to reset some variables when moving to
next subsets.

2. Dynamic programming?
Does this problem illustrate optimal substructure?

3. Maybe iterative dfs?


 */

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
        bool result = _makesqureDfs(nums);

        cout << "result: " << result << ", nums: " << nums.size() << endl;
        return result;
    }

    /*
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
                if( dfs(target - nums[i], i + 1, matches)) return true;
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

    // TODO: iterative dfs
};

void test()
{
    Solution solution;

    vector<int> nums;
    nums = {};
    assert(solution.makesquare(nums) == false); // edge case, result depends on definition, both true or false are reasonable

    nums = {0, 0, 0, 0};
    assert(solution.makesquare(nums) == false); // edge case, result depends on definition, both true or false are reasonable

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
        3, 3, 3, 3, 4, 1, 2, 2, 3, 4,
    };
    assert(solution.makesquare(nums));

    nums = {
        1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2,
    };
    assert(solution.makesquare(nums));

    nums = {
        1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2,
    };
    assert(solution.makesquare(nums));

    cout << "self test passed" << endl;
}

int main()
{
    test();
}
