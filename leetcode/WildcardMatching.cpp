/*
 * 44. Wildcard Matching
 *
    Total Accepted: 70378
    Total Submissions: 380786
    Difficulty: Hard
    Implement wildcard pattern matching with support for '?' and '*'.

    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).

    The matching should cover the entire input string (not partial).

    The function prototype should be:
    bool isMatch(const char *s, const char *p)

    Some examples:
    isMatch("aa","a") → false
    isMatch("aa","aa") → true
    isMatch("aaa","aa") → false
    isMatch("aa", "*") → true
    isMatch("aa", "a*") → true
    isMatch("ab", "?*") → true
    isMatch("aab", "c*a*b") → false

ANALYSIS:
    1) Backtracking, for problems with substructures
    2) Dynamic Programming, for problems with (overlapping) substructures
    3) Finite State Machine (finite automata)

Backtracking:
    For pattern `*p` and text `*text`, there may exist such cases:
    if `*text == *pattern` or `*pattern == '?'`: this is a match for now, then go to `text++`, `pattern++`.
    if `*pattern == '*'`: Save the star's position as `star` and current position of text
to match as `pText` and go on:
        If there are no match, then backtrack: set current pointer pattern's position next to `star`,
    and current `text` pointer to `++pText`.
        If we encounter a second star '*', then any matched parts before this star
    match could be ignored, because we can do any sequence match with a single
    star. So this is where we need to update the `star` and matched `pText`.


Dynamic Programming:


Deterministic Finite Automata:


*/

#include <iostream>

class Solution {
public:
    bool isMatch(const char* text, const char* pattern)
    {
        // previous star in patter and matched text's position for backtrack.
        const char *star = NULL, *pText = text;
        while (*text) {
            if (*pattern == *text || *pattern == '?') {
                pattern++;
                text++;
            } else if (*pattern == '*') {
                star = pattern;
                pText = text;
                pattern++;
            } else if (star) {
                pattern = star + 1;
                text = ++pText;
            } else
                return false;
        }
        while (*pattern == '*')
            pattern++;
        return !*pattern;
    }
};

// A function to run test cases
void test(char* s, char* p)
{
    std::cout << (Solution().isMatch(s, p) ? ("Yes") : ("No")) << std::endl;
}

// Driver program to test above functions
int main()
{
    test((char*)"geeks", (char*)"g*ks");           // Yes
    test((char*)"geeks", (char*)"g*k");            // No
    test((char*)"geeksforgeeks", (char*)"ge?ks*"); // Yes
    test((char*)"gee", (char*)"g*k");              // No because 'k' is not in p
    test((char*)"pqrst", (char*)"*pqrs");          // No because 't' is not in s
    test((char*)"abcdhghgbcd", (char*)"abc*bcd");  // Yes
    test((char*)"abcd", (char*)"abc*c?d");         // No because p must have 2 instances of 'c'
    test((char*)"abcd", (char*)"*c*d");            // Yes
    test((char*)"abcd", (char*)"*a*cd");           // Yes
    test((char*)"aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaa"
                "aaabbaabbbbaababbababaabbbaababbbba",
        (char*)"*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*"); // Yes
    return 0;
}
