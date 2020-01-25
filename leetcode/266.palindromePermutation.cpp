/**
 *
 *
266. Palindrome Permutation

Difficulty:
Easy

Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true

================================================================================
SOLUTION

Just count occurrences of characters, there should be at most one character
with odd occurrence.

 *
 */

#include <debug.hpp>

class Solution {
public:
    bool canPermutatePalindrome(string s) {
        bool result;
        //result = canPermutatePalindromeSet(s);
        result = canPermutatePalindromeBitset(s);

        cout << s << " => " << result <<endl;

        return result;
    }

    bool canPermutatePalindromeSet(string s) {
        unordered_set<char> charSet;
        for (int i = 0; i < (int)s.size(); ++i) {
            if (charSet.count(s[i])) {
                charSet.erase(s[i]);
            } else {
                charSet.insert(s[i]);
            }
        }

        return charSet.size() <= 1;
    }

    bool canPermutatePalindromeBitset(string s) {
        bitset<256> bits;
        for (int i = 0; i < (int)s.size(); ++i) {
            bits.flip(s[i]);
        }

        return bits.count() <= 1;
    }
};


int test() {

    Solution solution;
    string s;
    bool output;

    s = "", output = true;
    assert(solution.canPermutatePalindrome(s) == output);
    s = "a", output = true;
    assert(solution.canPermutatePalindrome(s) == output);
    s = "aa", output = true;
    assert(solution.canPermutatePalindrome(s) == output);
    s = "aab", output = true;
    assert(solution.canPermutatePalindrome(s) == output);
    s = "aabc", output = false;
    assert(solution.canPermutatePalindrome(s) == output);

    cout << "test passed" << endl;

    return 0;
}

int main(int argc, char **argv) {
    test();
}
