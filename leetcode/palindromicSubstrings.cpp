/**
 *

647. Palindromic Substrings
Medium


Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.

================================================================================
SOLUTION

1. Brute force
Don't think about it

Complexity: O(2ⁿ)

2. Dynamic programming

1) Two dimensional state
Define state dp[i][j] as whether substring s[i:j+1] is palindrome or not.

Complexity: O(N²)

2) One dimensional state
Define state f(n) by palindromic substrings of string of size n.

Then we have recurrence relation:
    f(n) = f(n - 1) + #(palindromic strings ending with n)

To get palindromic strings ending with n, we don't have to do brute force check.
There is actually state transition recurrence relation.

Observation:
s[i:n + 1] if palindromic if and only if s[i + 1:n] is palindromic and s[i] == s[n].

Then, define another state g(n), as a list of indices such that s[i:n+1] is palindrome.

Denote g(n) the palindromic strings ending with n, then we have recurrence relation.

Complexity:
average O(N), worst case O(N²) for "aaaa" case.
worst case O(N).

3. Manacher's algorithm

*/

#include <debug.hpp>


class Solution {
public:
    int countSubstrings(string s) {
        int result = _countSubstringsDp(s);

        cout << s << ", " << result << endl;

        return result;
    }

    int _countSubstringsDp(string s) {
        vector<int> dp(2, 0);
        vector<int> indices; // s[i:n] is palindromic // 0
        vector<int> indicesNew; // s[i:n] is palindromic

        for (int i = 0; (unsigned int) i < s.size(); ++i) {
            for (int j: indices) {
                if (j && s[j - 1] == s[i]) {
                    indicesNew.push_back(j - 1);
                } // length >= 3, general case of forming new palindrome string of
            }
            if (i && s[i] == s[i - 1]) {
                indicesNew.push_back(i - 1);
            } // length 2 palindrome, 'aa'
            indicesNew.push_back(i); // length 1, palindrome
            dp[1] = dp[0] + indicesNew.size();

            indices = move(indicesNew);
            dp[0] = dp[1];
        }
        return dp[1];
    }
};

void test() {
    Solution solution;
    string s;

    s = "";
    assert(solution.countSubstrings(s) == 0);

    s = "a";
    assert(solution.countSubstrings(s) == 1);

    s = "aa";
    assert(solution.countSubstrings(s) == 3);

    s = "abc";
    assert(solution.countSubstrings(s) == 3);

    s =  "aaa";
    assert(solution.countSubstrings(s) == 6);

    s =  "aaaa";
    assert(solution.countSubstrings(s) == 10);

    s =  "aaaaa";
    assert(solution.countSubstrings(s) == 15);

    cout << "self test passed!" << endl;
}

int main(int argc, char *argv[])
{
    test();
    return 0;
}
