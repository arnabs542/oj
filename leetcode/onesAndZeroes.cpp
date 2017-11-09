/*
 *
474. Ones and Zeroes

In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:
The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.

Example 1:
    Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
    Output: 4

    Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”

Example 2:
    Input: Array = {"10", "0", "1"}, m = 1, n = 1
    Output: 2

    Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

==============================================================================================
SOLUTION
1. Naive brute force solution
Enumerate all possible combinations of the strings.

Complexity: O(2^ⁿ), O(2^ⁿ).

2. Graph search(dfs or bfs)

The wanted strings can be found in a process of which at each step, choose an eligible string
from the array. At each step, we have multiple choices with respect to which string to
use. Different choices or branches indicate a GRAPH structure, on which search frontiers can be
explored in a depth first or breadth first approach.

Define the state as a tuple of:
    (available strings in the array, number of available ones and zeroes: m, n).

This graph search method is kind of brute force method, trying to find all the combinations,
except that there are memoization procedure during the search.

Complexity: O(2^ⁿ).

3. Greedy strategy?
First of all, shorter strings are better, since they consumes less 0s and 1s?

BUT THIS IS WRONG.
This greedy strategy can be proven by contradiction.
Consider this case:
Array = {"100", "1110", "11101"}, m = 7, n = 2;

3. Dynamic Programming?

RELATION AND DIFFERENCE BETWEEN DYNAMIC PROGRAMMING AND GRAPH SEARCH(breadth first search or depth first search)

Dynamic programming can be viewed as a subset of breadth first search

The only difference the DEFINITION OF THE STATES(NODES/VERTICES).

Dynamic programming defines such state that incorporate the PROBLEM SIZE and utilize the
optimal substructure and search the graph in a topological sorted order, thus reducing the
complexity to be proportional to the problem size, instead of exponential.

While breadth first search is a more general search technique, its state definition can be very flexible.

Define the state as a tuple of (array size, number of zeroes, number of ones).
Then the state transition function of objective function number of strings, denoted as dp(l, m, n), is:

dp[l][m][n] = max(dp[l-1][m-nZeroes][n-nOnes] + 1, dp[l-1][m][n]);

The idea behind this is similar to 0-1 knapsack problem. For an array of size l, where have two
branches: use the last element or not, then we have recurrence relation to its sub-problems.

Complexity: O(lmn), O(lmn), where l is the size of string array.

4. Space optimized dynamic programming
The state transition function has only dependency on the previous dimension of l. Then it's
possible to use rolling array to store the intermediate value to save space.

Note that the inner loops with respect to m and n should be done FROM TOP TO BOTTOM.

By inspecting the recurrence relation above, the current value is updated using bottom value from
previous iteration. And if we override the table from bottom to top, then the previous value would
be overridden by the current one, which may be used by updating current value for larger m, n. This
would cause over counting.

*/

#include "_decorators.hpp"
#include <assert.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


//static Memoized<int, const vector<string>&, int, int, int> dfs;
class Solution {
    public:
        int findMaxForm(vector<string>& strs, int m, int n) {
            cout << "intput size: " << strs.size() << ", m: " << m << ", n: " << n << endl;;
            for (size_t i = 0; i < strs.size(); ++i) cout << strs[i] << " ";
            cout << endl;

            int result = 0;
            //result = this->_findMaxFormDfsBruteForce(strs, m, n);
            //result = this->_findMaxFormDfsOpt(strs, m, n);
            //result = this->_findMaxFormDfsOpt2(strs, m, n);
            //result = this->_findMaxFormDp(strs, m, n);
            result = this->_findMaxFormDpOpt(strs, m, n); // best solution
            cout << "result: " << result << ", m: " << m << ", n: " << n << endl;
            return result;
        }

        int _findMaxFormDfsBruteForce(vector<string>& strs, int m, int n) {

            map<tuple<int, int, int>, int> cache;
            function<int(int m, int n, int start)>
                dfs = [&](int m, int n, int start) -> int {
                    //int dfs(const vector<string> &strs, int m, int n, int start=0) {
                    // FIXME: time limit exceeded for large array and m, n. How to prune?
                    //auto t = make_tuple(m, n, start);
                    tuple<int, int, int> t = make_tuple(m, n, start);
                    if (cache.find(t) != cache.end()) {
                        return cache.at(t);
                    }

                    if ((m <= 0 && n <= 0) || start >= (int)strs.size()) { // base case
                        return 0;
                    }

                    int result = 0;
                    for (size_t i = start; i < strs.size(); ++i) {
                        int nZeroes = count(strs[i].begin(), strs[i].end(), '0');
                        int nOnes = count(strs[i].begin(), strs[i].end(), '1');
                        if (nZeroes <= m && nOnes <= n) {
                            result = max(result, dfs(m - nZeroes, n - nOnes, i + 1) + 1);
                            result = max(result, dfs(m, n, i + 1));
                            // XXX: severe performance issue!
                            // DUPLICATE CALCULATIONS involved, second transition branch is
                            // covered by first statement with larger i.

                        }
                    }
                    //cache.insert(make_pair(t, result));
                    cache[t] = result;
                    return result;
                };

            int result = dfs(m, n, 0);
            return result;
        }

        int _findMaxFormDfsOpt(vector<string> &strs, int m, int n) {
            // XXX: trick here: sort the list first
            sort(strs.begin(), strs.end(), [](string s1, string s2)->int {
                    return s1.length() != s2.size() ? s1.length() < s2.length() : s1 < s2;
                    });

            map<tuple<int, int, int>, int> cache;
            function<int(int m, int n, int start)>
                dfs = [&](int start, int m, int n) -> int {
                    if ((m <= 0 && n <= 0) || start >= (int)strs.size()) { return 0; }// base case
                    auto t = make_tuple(m, n, start);
                    //tuple<int, int, int> t = make_tuple(m, n, start);
                    if (cache.find(t) != cache.end()) { return cache.at(t); }

                    int result = 0;

                    int i = start;
                    int nZeroes = count(strs[i].begin(), strs[i].end(), '0');
                    int nOnes = strs[i].size() - nZeroes;
                    result = max(result, nZeroes <= m && nOnes <= n ? (dfs(i + 1, m - nZeroes, n - nOnes) + 1):0);
                    result = max(result, dfs(i + 1, m, n));

                    cache[t] = result;
                    return result;
                };

            int result = dfs(0, m, n);
            return result;

        }

        int _findMaxFormDfsOpt2(vector<string> &strs, int m, int n) {
            // XXX: trick here: sort the list first
            sort(strs.begin(), strs.end(), [](string s1, string s2)->int {
                    return s1.length() != s2.size() ? s1.length() < s2.length() : s1 < s2;
                    });

            map<tuple<int, int, int>, int> cache;
            function<int(int m, int n, int start)>
                dfs = [&](int start, int m, int n) -> int {
                    if ((m <= 0 && n <= 0) || start >= (int)strs.size()) { return 0; }// base case
                    auto t = make_tuple(m, n, start);
                    //tuple<int, int, int> t = make_tuple(m, n, start);
                    if (cache.find(t) != cache.end()) { return cache.at(t); }

                    int result = 0;

                    for (int i = start; i < (int)strs.size(); ++i) {
                        if (i > start && strs[i] == strs[i -1]) { continue; }
                        int nZeroes = count(strs[i].begin(), strs[i].end(), '0');
                        int nOnes = strs[i].size() - nZeroes;
                        result = max(result, nZeroes <= m && nOnes <= n ? (dfs(i + 1, m - nZeroes, n - nOnes) + 1):0);
                    }

                    cache[t] = result;
                    return result;
                };

            int result = dfs(0, m, n);
            return result;
        }


        int _findMaxFormDp(vector<string>& strs, int m, int n) {
            // working solution
            if (m < 0 || n < 0) { return 0; }

            // initialization
            vector<vector<vector<int>>> dp;
            for (size_t l = 0; l < strs.size() + 1; ++l)  {
                dp.push_back(vector<vector<int>>());
                for (int i = 0; i < m + 1; ++i) {
                    dp[l].push_back(vector<int>());
                    for (int j = 0; j < n + 1; ++j) {
                        dp[l][i].push_back(0);
                    }
                }
            } // XXX: this initialization is slow ! Make use of vector constructor
            //int dp[strs.size() + 1][m][n];
            //dp = {0};

            for( size_t l = 0; l < strs.size(); ++l ) {
                for (int i = m; i >= 0; --i) {
                    for (int j = n; j >= 0; --j) {
                        int nZeroes = count(strs[l].begin(), strs[l].end(), '0');
                        int nOnes = count(strs[l].begin(), strs[l].end(), '1');
                        dp[l + 1][i][j] = max(dp[l][i][j], i >= nZeroes && j >= nOnes ? 1 + dp[l][i-nZeroes][j-nOnes] : 0);
                    }
                }
            }
            return dp[strs.size()][m][n];
        }

        /*
         * Space optimized
         */
        int _findMaxFormDpOpt(vector<string>& strs, int m, int n) {
            if (m < 0 || n < 0) { return 0; }
            vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

            for( size_t l = 0; l < strs.size(); ++l ) {
                // move below two lines in the outside most loop.
                int nZeroes = count(strs[l].begin(), strs[l].end(), '0');
                int nOnes = strs[l].size() - nZeroes;
                for (int i = m; i >= nZeroes; --i) {
                    for (int j = n; j >= nOnes; --j) {
                        dp[i][j] = max(dp[i][j], 1 + dp[i - nZeroes][j - nOnes]);
                    }
                }
            }
            return dp[m][n];
        }

};

        // FIXME: memoized function method seems not working.(segmentation fault when calling)
        //auto dfs = Memoized<int, const vector<string>&, int, int, int>(Solution::_dfs);
        //auto dfs = memoize<int, const vector<string>&, int, int, int>(Solution::_dfs);


    int main(int argc, char *argv[])
    {
        Solution solution;

        vector<string> strs;

        strs = vector<string>({});
        assert(solution.findMaxForm(strs, 1, 1) == 0);

        strs = vector<string>({});
        assert(solution.findMaxForm(strs, -1, -1) == 0);

        strs = vector<string>({"10", "0", "1"});
        assert(solution.findMaxForm(strs, 1, 1) == 2);

        strs = vector<string>({"10", "0001", "111001", "1", "0"});
        assert(solution.findMaxForm(strs, 1, 1) == 2);
        assert(solution.findMaxForm(strs, 5, 3) == 4);

        strs = vector<string>({"11","11","0","0","10","1","1","0","11","1","0","111","11111000","0","11","000","1","1","0","00","1","101","001","000","0","00","0011","0","10000"});
        assert(solution.findMaxForm(strs, 90, 66) == 29);

        strs = vector<string>({"10","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0","0001","111001","1","0"});
        assert(solution.findMaxForm(strs, 20, 20) == 40);
        assert(solution.findMaxForm(strs, 50, 50) == 81);
        assert(solution.findMaxForm(strs, 100, 100) == 101);

        cout << "self test passed!" << endl;
        return 0;
    }
