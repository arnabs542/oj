/**
 *
267. Palindrome Permutation II

Difficulty:
Medium

Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []

================================================================================
SOLUTION

It's easy to verify whether such palindromic permutation exists or not.
The problem is how to generate such palindromic permutation.

1. Generate all permutations and verify

Complexity: O(n*n!)

2. Generate palindromic permutations
A palindromic permutation is symmetric, so we can generate the first half,
then the second is the reverse of the first half permutation.

The permutation generating sequence should be treated as a graph traversal problem,
refer to problem 'permutations'.

Complexity: O((n/2)!)

 *
 */

#include <debug.hpp>

class Solution {
public:
    vector<string> generatePalindromes(string s) {
        vector<string> result;
        result = generatePalindromesGenerateHalf(s);

        cout << s << " => " << result << endl;
        return result;
    }

    void dfs(string &s, int k, vector<string> &result) {
        if (k == (int)s.size()) {
            result.push_back(s);
            return;
        }
        unordered_set<char> charSet;
        for (int i = k ; i < (int)s.size(); ++i) {
            if (charSet.count(s[i])) continue; // filter duplicate
            charSet.insert(s[i]);
            swap(s[i], s[k]);
            dfs(s, k + 1, result);
            swap(s[i], s[k]);
        }
    }

    vector<string> generatePalindromesGenerateHalf(string s) {
        vector<string> result;
        //int n = (int)s.size();
        //unordered_map<char, int> counters; // char counter
        map<char, int> counters; // char counter
        for (int i = 0; i < (int)s.size(); ++i) {
            ++counters[s[i]];
        }
        //char oddChar = 0;
        string oddString;
        vector<char> halfChars;
        for (auto item: counters) { // verify and construct half string
            if (item.second % 2) {
                //oddChar = item.first;
                oddString += string(1, item.first);
                if (oddString.size() > 1) return result;
            }
            for (int i = 0; i < item.second/2; ++i) {
                halfChars.push_back(item.first);
            }
        }

        string halfPerm(halfChars.begin(), halfChars.end()); // first half
        vector<string> permutations; // permutations of first half
        if (halfPerm.size() || oddString.size()) {
            dfs(halfPerm, 0, permutations);
        }
        for (string p: permutations) {
            string rear = p;
            reverse(rear.begin(), rear.end()); // reverse first half
            string palin = p + oddString + rear;
            result.push_back(palin);
        }

        return result;
    }

};

int test() {
    Solution solution;

    string s;
    vector<string> output;

    s = "";
    output = {};
    assert(solution.generatePalindromes(s) == output);

    s = "a";
    output = {"a"};
    assert(solution.generatePalindromes(s) == output);

    s = "aa";
    output = {"aa"};
    assert(solution.generatePalindromes(s) == output);

    s = "ab";
    output = {};
    assert(solution.generatePalindromes(s) == output);

    s = "aba";
    output = {"aba"};
    assert(solution.generatePalindromes(s) == output);

    s = "aabb";
    output = {"abba", "baab"};
    assert(solution.generatePalindromes(s) == output);

    s = "aabbc";
    output = {"abcba", "bacab"};
    assert(solution.generatePalindromes(s) == output);

    s = "aaaabb";
    output = {"aabbaa", "abaaba", "baaaab",};
    assert(solution.generatePalindromes(s) == output);

    cout << "test passed" << endl;
    return 0;
}

int main(int argc, char **argv) {
    // TODO: submit
    test();
    return 0;
}
