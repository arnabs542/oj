/**
 *
877. Stone Game
Medium

Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.



Example 1:

Input: [5,3,4,5]
Output: true
Explanation:
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.


Note:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd

SOLUTION
================================================================================

Apparently this is a zero-sum game that can be solved with minimax strategy.
The key is how to define proper state.

1. Minimax - 2D dynamic programming
Since we are taking stones from beginning or ending, the state transition is
two dimensional interval.

Define state f[i][j]: difference sum between first and second player, on interval
[i, j].
State transition:
    f[i][j] = max(
        f[i] - f[i + 1][j],
        f[j] - f[i][j-1]
    )
So state (i, j) depends on (i+1, j), (i, j-1).
In a bottom up approach, decrement i and increase j, where i <= j.

(i,   j) -> (i+1, j)
   |
   V
(i, j-1)

2. Minimax - 1D dynamic programming


3. Mathematical

Always pick even position or odd positions with larger sum of values.


 *
 */

#include <debug.hpp>

class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        //bool result = stoneGameMinimaxDP2D(piles);
        bool result = stoneGameMinimaxDP1D(piles);

        cout << piles << " => " << result << endl;

        return result;
    }

    bool stoneGameMinimaxDP2D(vector<int> &piles) {
        const int &n = piles.size();
        if (!n) return false;
        vector<vector<int>> f(n+1, vector<int>(n+1, 0)); // length+1

        for (int i = n - 1; i >= 1; --i) {
            f[i][i] = piles[i-1];
            for(int j = i + 1; j <= n; ++j) {
                f[i][j] = max(
                        piles[i-1] - f[i + 1][j], // out of bound
                        piles[j-1] - f[i][j - 1]
                        );
            }
        }

        //cout << f << endl;

        return f[1][n] > 0;
    }

    bool stoneGameMinimaxDP1D(vector<int> &piles) {
        const int &n = piles.size();
        if (!n) return false;
        vector<int> f(n+1, 0); // only inner vector needed. length+1

        for (int i = n - 1; i >= 1; --i) {
            f[i] = piles[i-1]; // initialization for f[i][i]
            for(int j = i + 1; j <= n; ++j) {
                f[j] = max(
                        piles[i-1] - f[j], // XXX: this is vector on j out of bound
                        piles[j-1] - f[j - 1]
                        );
            }
        }

        return f[n] > 0;
    }

    bool stoneGameMinimaxMath(vector<int> &piles) {
        return true;
    }
};

int test() {
    Solution solution;
    vector<int> piles;
    bool result;

    //piles = {};
    //result = false;
    //assert(solution.stoneGame(piles) == result);

    piles = {1, 2};
    result = true;
    assert(solution.stoneGame(piles) == result);

    piles = {5, 3, 4, 5};
    result = true;
    assert(solution.stoneGame(piles) == result);

    piles = {1,4,10,8,3,2,4,1};
    result = true;
    assert(solution.stoneGame(piles) == result);

    cout << "self test passed!";

    return 0;
}


int main(int argc, char *argv[])
{
    test();
    return 0;
}
