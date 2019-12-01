/**
 *
1140. Stone Game II
Medium

Alex and Lee continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones.

Alex and Lee take turns, with Alex starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.



Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex takes two piles at the beginning, then Lee can take all three piles left. In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger.


Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 10 ^ 4

Hint 1:
Use dynamic programming: the states are (i, m) for the answer of piles[i:] and that given m.

SOLUTION
================================================================================

1. Minimax dynamic programming

Define state f[m][i]:
    maximum value that can be obtained with m , starting with position i,
by first player.
State transition:
    f[m][i] = max({
        sum(nums[i...i+x-1]) + sum(num[i+x...]) - f[m'][i+x]
    }),
where m' = max(m, x, n-i-x), and 1 <= x <= 2m.
Then search space (m, i) is n*n.

Sum operation can be sped up with prefix sum.

Do memorized dfs?

Complexity:
O(N^3).


 *
 *
 */

#include <debug.hpp>

class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        int result = 0;
        result = stoneGameIIMinimaxDP2D(piles);
        cout << piles << " => " << result << endl;

        return result;
    }

    int stoneGameIIMinimaxDP2D(vector<int> &piles) {
        const int &n = piles.size();
        vector<vector<int>> f(n + 2, vector<int>(n + 2, 0)); // f[m][i]
        if (!piles.size()) return 0;
        vector<int> prefixSum(n + 1, 0);
        for (int i = 1; i <= n; ++i)
            prefixSum[i] = prefixSum[i - 1] + piles[i - 1];

        auto getSum = [&prefixSum](int start, int end) -> int {
            return (start <= end) ? prefixSum[end] - prefixSum[start - 1]:0; // length indexed
        };

        for (int i = n; i >= 1; --i) {
            for (int m = (n+1)/2; m >= 1; --m) {
                for (int x = 1 ; x <= 2*m && i + x - 1 <= n; ++x) {
                    int p = std::max(m, x); // dependent state, next m
                    p = std::min(p, (n+1)/2); // clip
                    f[m][i] = max(f[m][i], getSum(i, i+x-1) + getSum(i+x, n) - f[p][i+x]); // state transition
                }
            }
        }

        return f[1][1];
    }


};

int test() {
    Solution solution;

    vector<int> piles;
    int result;

    piles = {};
    result = 0;
    assert(solution.stoneGameII(piles) == result);

    piles = {1};
    result = 1;
    assert(solution.stoneGameII(piles) == result);

    piles = {1, 2};
    result = 3;
    assert(solution.stoneGameII(piles) == result);

    piles = {1, 2, 3};
    result = 3;
    assert(solution.stoneGameII(piles) == result);

    piles = {2, 7, 9, 4, 4};
    result = 10;
    assert(solution.stoneGameII(piles) == result);

    cout << "self test passed!" << endl;
    return 0;
}

int main(int argc, char *argv[])
{
    test();
    return 0;
}
