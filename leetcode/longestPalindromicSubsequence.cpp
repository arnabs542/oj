#include <debug.hpp>


class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int result;
        //result = _longestPalindromeSubseqDp(s);
        result = _longestPalindromeSubseqDp2(s);

        cout << s << " =>" << result << endl;

        return result;
    }

    int _longestPalindromeSubseqDp(string s) {
        int n = (int)s.size();
        // int dp[n + 1][n + 1];
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
        for (int i = 0; i < n; ++i) dp[i][i] = 1;
        int maxLen = std::min(1, n);
        for (int l = 2; l <= n; ++l) {
            for (int i = 0; i <= n - l; ++i) {
                int j = i + l - 1;
                if (s[i] == s[j]) {
                    dp[i][j] = 2 + (l >= 3 ? dp[i + 1][j - 1]:0);
                } else {
                    dp[i][j] = max(dp[i][j-1], dp[i + 1][j]);
                }
                maxLen = max(maxLen, dp[i][j]);
            }
        }
        return maxLen;
    }

    int _longestPalindromeSubseqDp2(string s) {
        int n = (int)s.size();
         //int dp[n + 1][n + 1];
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
        for (int i = n - 1; i >= 0; --i) {
            dp[i][i] = 1;
            for (int j = i + 1; j <= n - 1; ++j) {
                if (s[i] == s[j]) {
                    dp[i][j] = 2 + dp[i + 1][j - 1]; // dependency requires (i + 1, j - 1) computed first
                } else {
                    dp[i][j] = max(dp[i][j-1], dp[i + 1][j]);
                }
            }
        }
        return n ? dp[0][n - 1] : 0;
    }
};


void test() {
    Solution solution;
    string s;

    s = "";
    assert(solution.longestPalindromeSubseq(s) == 0);

    s = "a";
    assert (solution.longestPalindromeSubseq(s) == 1);

    s = "aa";
    assert (solution.longestPalindromeSubseq(s) == 2);

    s = "ab";
    assert (solution.longestPalindromeSubseq(s) == 1);

    s = "aab";
    assert (solution.longestPalindromeSubseq(s) == 2);

    s = "aba";
    assert (solution.longestPalindromeSubseq(s) == 3);

    s = "bbbab";
    assert (solution.longestPalindromeSubseq(s) == 4);

    s = "cbbd";
    assert (solution.longestPalindromeSubseq(s) == 2);

    cout << "self test passed!" << endl;
}

int main(int argc, char *argv[])
{
    test();
    return 0;
}
