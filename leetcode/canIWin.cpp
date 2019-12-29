/**
 *
 */

#include <debug.hpp>

class Solution {
public:
    bool canIWin(int maxChoosableInteger, int desiredTotal) {
        bool result = canIWinMinimax(maxChoosableInteger, desiredTotal);

        cout << maxChoosableInteger << " " << desiredTotal << " => " << result << endl;

        return result;
    }

    bool canIWinMinimax(int maxChoosableInteger, int desiredTotal) {
        //unordered_map<int, int> cache;
        vector<int> cache(1 << maxChoosableInteger);
        int sum = maxChoosableInteger*(maxChoosableInteger+1)/2;
        if (maxChoosableInteger < 1) return desiredTotal <= 0;
        if (sum < desiredTotal) return false;
        else if (sum == desiredTotal && maxChoosableInteger % 2) return true;
        else if (desiredTotal <= 0) return true;

        int state = 0;
        for (int i = 0; i < maxChoosableInteger; ++i) {
            state |= (1 << i);
        }
        return dfs(state, desiredTotal, cache, maxChoosableInteger) > 0;
    }

    //int dfs(int state, int target, unordered_map<int, int> &cache, int n) {
    int dfs(int state, int target, vector<int> &cache, int n) {
        //int result = -1; // XXX: initial value

        if (target <= 0) return -1;

        //if (cache.count(state)) return cache[state];
        if (cache[state] != 0) return cache[state];
        for (int i = 0; i < n; ++i) {
            int mask = 1 << i;
            if (state & mask) {
                //if (i + 1 >= target) {
                    //cache[state] = 1;
                    //return 1;
                //}
                //state ^= mask;
                //result = std::max(result, -dfs(state ^ mask, target - i - 1, cache, n));
                //state ^= mask;
                if (i + 1 >= target || dfs(state ^ mask, target-i-1, cache, n) < 0) {
                    cache[state] = 1;
                    return 1;
                }

            }
        }

        cache[state] = -1;
        return -1;
        //cache[state] = result;
        //return result;
    }

};

int test() {
    int maxChoosableInteger;
    int desiredTotal;
    bool output;

    Solution solution;

    maxChoosableInteger = 0;
    desiredTotal = 0;
    output = true;
    assert(solution.canIWin(maxChoosableInteger, desiredTotal) == output);

    maxChoosableInteger = 10;
    desiredTotal = 0;
    output = true;
    assert(solution.canIWin(maxChoosableInteger, desiredTotal) == output);

    maxChoosableInteger = 1;
    desiredTotal = 1;
    output = true;
    assert(solution.canIWin(maxChoosableInteger, desiredTotal) == output);

    maxChoosableInteger = 10;
    desiredTotal = 11;
    output = false;
    assert(solution.canIWin(maxChoosableInteger, desiredTotal) == output);

    maxChoosableInteger = 15;
    desiredTotal = 100;
    output = true;
    assert(solution.canIWin(maxChoosableInteger, desiredTotal) == output);

    maxChoosableInteger = 20;
    desiredTotal = 168;
    output = false;
    assert(solution.canIWin(maxChoosableInteger, desiredTotal) == output);

    cout << "test passed!" << endl;

    return 0;
}

int main(int argc, char **argv) {
    return test();
}
