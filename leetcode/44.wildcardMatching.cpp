/**
 *
 *
44. Wildcard Matching
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

================================================================================
SOLUTION

For normal string matching, just comparing character by character will do. But,
with wildcard character, pattern "*" might match multiple characters, giving
undetermined search branches.

--------------------------------------------------------------------------------
1. Graph search -  backtracking dfs
Since there are multiple branches, it's possible to perform depth first search.

Define state as a tuple of:
(i: text starting index to match, j: pattern starting index to match)

1) For pattern '?', just increase both pointers.
2) For pattern '*', there are undetermined branches. '*' can match any sequence.
For this case, after transition, next state may will have branches:
    (i, j + 1), (i + 1, j + 1), ..., (i + m, j + 1), where i + m = text length.


2. Backtracking with prune
Naive backtracking will exceed time limit.
This is due to the lots of unnecessary computation.

Optimization by PRUNING
-------------
The core problem is with wildcard '*'. It involves multiple search branches,
leading to overlapping subproblems. Beside dynamic programming, we can
prune it by some heuristics.

1) A little problem is duplicate computation with successive '*'.
Eliminate successive '*'. Successive '*' is equivalent to just one '*'.

2) EXHAUST TO VERIFY NEGATIVE MATCH
The major performance problem occurs when the dfs subroutine returns
no match, the backtracking procedure will EXHAUST all possible situations
to verify whether there is indeed no match.

So the question is, shall we exhaust all cases to say no?

Absolutely not. We are trying to search with '*' matching shorter sequence to
longer sequence. When the sub-routine returns false, there are several different
cases: '*' just matched too little sequences or '*' just matched too many sequences.

For the former case, it will be searched in the later iteration. And for the
latter case, there is NO NEED TO GO FURTHER!

For only one '*', it can be easily shown. If there are multiple '*', use
mathematical induction to prove!

Complexity: O(mn)
How about worst case?

3. Iterative backtracking

    For pattern `*p` and text `*text`, there may exist such cases:
    if `*text == *pattern` or `*pattern == '?'`: this is a match for now, then go to `text++`, `pattern++`.
    if `*pattern == '*'`: Save the star's position as `star` and current position of text
to match as `pText` and go on:
        If there are no match, then backtrack: set current pointer pattern's position next to `star`,
    and current `text` pointer to `++pText`.
        If we encounter a second star '*', then any matched parts before this star
    match could be ignored, because we can do any sequence match with a single
    star. So this is where we need to update the `star` and matched `pText`.


4. Dynamic programming
Since backtracking solution involves overlapping subproblems, try dynamic programming.

Define state dp[i][j], indicates whether text[:i + 1] and pattern p[:j + 1] is a match.

----------------------------------------------------------------------------------------------
Dynamic Programming:

Case 1: The character is ‘*’
Here two cases arise

    1. We can ignore ‘*’ character and move to next character in the Pattern.
    2. ‘*’ character matches with one or more characters in Text. Here we will
move to next character in the string.

Case 2: The character is ‘?’
We can ignore current character in Text and move to next character in the Pattern
and Text.

Case 3: The character is not a wildcard character
If current character in Text matches with current character in Pattern, we move to
next character in the Pattern and Text. If they do not match, wildcard pattern and
Text do not match.

We can use Dynamic Programming to solve this problem –
Let T[i][j] is true if first i characters in given string matches the first j
characters of pattern.

DP Initialization:

```
// both text and pattern are null
T[0][0] = true;

// pattern is null
T[i][0] = false;

// text is null
T[0][j] = T[0][j - 1] if pattern[j – 1] is '*'
```

DP recurrence relation :

```
// If current characters match, result is same as
// result for lengths minus one. Characters match
// in two cases:
// a) If pattern character is '?' then it matches
//    with any character of text.
// b) If current characters in both match
if ( pattern[j – 1] == ‘?’) ||
    (pattern[j – 1] == text[i - 1])
    T[i][j] = T[i-1][j-1]

// If we encounter ‘*’, two choices are possible-
// a) We ignore ‘*’ character and move to next
//    character in the pattern, i.e., ‘*’
//    indicates an empty sequence.
// b) '*' character matches with ith character in
//     input
else if (pattern[j – 1] == ‘*’)
    T[i][j] = T[i][j-1] || T[i-1][j]

else // if (pattern[j – 1] != text[i - 1])
    T[i][j]  = false <Paste>
```

The look up table may consumes a lot of memory.

Complexity: O(mn), O(mn).

5. Finite State Machine (finite automata)
Well, this is the fancy part.

The state transition can not only modeled by RECURRENCE RELATION, but also STATE MACHINE.

Build a nondeterministic Finite Automata, and search along the state machine graph.


*/

#include <assert.h>
#include <iostream>
#include <string.h>
using namespace std;

class Solution {
public:
    /**
     * s: string, input text tomatch
     * p: string, pattern
     *
     */
    bool isMatch(string s, string p) {
        bool result;
        result = _isMatchBacktrack(s, p);
        //result = _isMatchDP(s, p);
        //result = _isMatchDPRolling(s, p);
        //result = _isMatchBacktrackIterative(s.c_str(), p.c_str());

        cout << s << " | " << p << " => " << result << endl;

        return result;
    }

    bool dfsNaiveWithoutPrune(string& s, string& p, unsigned int si, unsigned int pi) {
        while (si < s.size() && pi < p.size()) {
            if (s[si] == p[pi] or p[pi] == '?') {
                ++si;
                ++pi;
            } else if (p[pi] == '*') {
                for (unsigned int k = si; k <= s.length(); ++k) {
                    if (dfs(s, p, k, pi + 1)) {
                        return true;
                    } // XXX: exhausted searching for negative, of course slow
                }
                return 0;
            } else { return 0; }
        }
        while (pi < p.size() && (p[pi] == '*'))  ++pi;
        return si == s.size() && pi == p.size();
    }
    /**
     * Inputs:
     * s: string to match
     * p: string, the pattern
     * si: int, index pointing to s
     * pi: int, index pointing to p
     *
     * Returns:
     * int:
     * ret = 1: match, end of string and pattern
     * ret = 0: no match, characters no match, both text and pattern not exhausted
     * ret = -1: no match, another state, string s is exhausted: pattern contains more characters
     *
     */
    int dfs(string& s, string& p, unsigned int si, unsigned int pi) {
        while (si < s.size() && pi < p.size()) {
            if (s[si] == p[pi] or p[pi] == '?') {
                ++si;
                ++pi;
            } else if (p[pi] == '*') {
                while (pi < p.size() - 1 && p[pi + 1] == '*') ++pi; // skip successive '*'
                for (unsigned int k = si; k <= s.length(); ++k) {
                    int ret = dfs(s, p, k, pi + 1);
                    if (ret == -1 || ret == 1) { return ret; } // avoid exhaustive search for negative
                }
                return -1;
            } else { return 0; } // characters no match.
        }
        while (pi < p.size() && (p[pi] == '*'))  ++pi;
        if (si == s.size() && pi == p.size()) { return 1; }
        if (pi < p.size()) { return -1; } // pattern contains more characters
        return 0;
    }

    bool _isMatchBacktrack(string s, string p) {
        return dfs(s, p, 0, 0) > 0;
    }

    bool _isMatchBacktrackIterative(const char* text, const char* pattern)
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

    bool _isMatchDP(string text, string pattern)
    {
        int m = text.length(), n = pattern.length();
        // empty pattern can only match with
        // empty string
        if (!n)
            return !m;

        int i, j;
        // lookup table for storing results of
        // subproblems
        // for big dynamic 2d array, allocate memory from heap using new
        bool** f = new bool*[m + 1];
        for (i = 0; i <= m; ++i) {
            f[i] = new bool[n + 1];
            memset(f[i], false, sizeof(bool) * (n + 1));
        }

        // empty pattern can match with empty string
        f[0][0] = true;
        // '*' can match with empty string
        for (j = 1; j <= n; ++j) {
            if (pattern[j - 1] == '*') {
                f[0][j] = f[0][j - 1];
            }
        }
        // fill the table in bottom-up fashion
        for (i = 1; i <= m; ++i) {
            for (j = 1; j <= n; ++j) {
                if (text[i - 1] == pattern[j - 1] || pattern[j - 1] == '?') {
                    f[i][j] = f[i - 1][j - 1];
                } else if (pattern[j - 1] == '*') {
                    f[i][j] = f[i][j - 1] || f[i - 1][j];
                    //for(int k = 0; k <= m; ++k) {
                        //if (f[k][j - 1]) {
                            //f[i][j] = true;
                            //break;
                        //}
                    //}
                } else {
                    // characters don't match
                    f[i][j] = false;
                }
                //cout << text[i-1] << ',' << pattern[j - 1] << f[i][j]<< endl;
            }
        }
        return f[m][n];
    }

    bool _isMatchDPRolling(string text, string pattern)
    {
        // XXX(done): optimized to use rolling array to reduce memory consumption
        int m = text.length(), n = pattern.length();
        // empty pattern can only match with
        // empty string
        if (!n)
            return !m;

        int i, j;
        // lookup table for storing results of
        // subproblems
        // for big dynamic 2d array, allocate memory from heap using new
        bool *f1 = new bool[n + 1];
        bool *f2 = new bool[n + 1];
        memset(f1, false, sizeof(bool) * (n + 1));
        memset(f2, false, sizeof(bool) * (n + 1));
        bool *f[] = { f1, f2 };

        // empty pattern can match with empty string
        f[0][0] = true;
        // '*' can match with empty string
        for (j = 1; j <= n; ++j) {
            if (pattern[j - 1] == '*') {
                f[0][j] = f[0][j - 1];
            }
        }
        // fill the table in bottom-up fashion
        for (i = 1; i <= m; ++i) {
            for (j = 1; j <= n; ++j) {
                if (text[i - 1] == pattern[j - 1] || pattern[j - 1] == '?') {
                    f[1][j] = f[0][j - 1];
                } else if (pattern[j - 1] == '*') {
                    // XXX a star matches empty sequence or many characters
                    f[1][j] = f[1][j - 1] || f[0][j];
                } else {
                    // characters don't match
                    f[1][j] = false;
                }
                //cout << text[i-1] << ',' << pattern[j - 1] << ',' << f[1][j]<< endl;
            }
            //swap f1 and f2 to roll the array
            bool *tmp = f[0];
            f[0] = f[1];
            f[1] = tmp;
            // XXX: not only to roll the array, but also initialize the edge condition
            f[0][0] = false;
        }
        return f[0][n];
    }

    bool isMatchNFA(const char* text, const char* pattern)
    {
        // TODO: finite state machine solution
        // First convert the wildcard expression into a regular expression, then use NFA or DFA
        // to match it
        int plen = strlen(pattern);
        char re[2 * plen];
        int i = 0;
        for (const char *p = pattern; *p; ++p) {
            switch (*p) {
                default:
                    re[i++] = *p;
                    break;
                case '?':
                    re[i++] = '.';
                    break;
                case '*':
                    re[i++] = '.';
                    re[i++] = '*';
                    break;
            }
        }
        re[i] = '\0';
        // XXX: refer ./regularExpressionMatching.c
        //return rematch(re, text);
        return false;
    }
};

// A function to run test cases
bool test(string s, string p)
{
    bool result = Solution().isMatch(s, p);
    //bool result = Solution()._isMatchDP(s, p);
    //bool result = Solution()._isMatchDPRolling(s, p);
    std::cout << (result ? ("Yes") : ("No")) << std::endl;
    return result;
}

// Driver program to test above functions
int main()
{
    Solution solution;

    assert(solution.isMatch("", ""));
    assert(!solution.isMatch("", "?"));
    assert(solution.isMatch("", "*"));
    assert(!solution.isMatch("", "*??**"));
    assert(solution.isMatch("a", "*?**"));
    assert(!solution.isMatch("a", "*??**"));
    assert(solution.isMatch("a", "a"));
    assert(!solution.isMatch("ab", "a"));
    assert(solution.isMatch("aa", "aa"));
    assert(solution.isMatch("aa", "a*"));
    assert(solution.isMatch("ab", "?*"));
    assert(!solution.isMatch("aab", "c*a*b"));

    assert(!solution.isMatch(
                "bbbbbbbabbaabbabbbbaaabbabbabaaabbababbbabbbabaaabaab",
                "b*b*ab*ba*b*b*bba"));

    // successive '*' test
    assert(!solution.isMatch(
                "bbbbbbbabbaabbabbbbaaabbabbabaaabbababbbabbbabaaabaab",
                "b*b*ab**ba*b**b***bba"));
    assert(!solution.isMatch(
                "abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb",
                "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"));

    assert(!test((char*)"mississippi", (char*)"m*issi*iss*"));
    assert(test((char*)"geeks", (char*)"g*ks"));           // Yes
    assert(test((char*)"ho", (char*)"**ho"));              // Yes
    assert(!test((char*)"geeks", (char*)"g*k"));           // No
    assert(test((char*)"geeksforgeeks", (char*)"ge?ks*")); // Yes
    assert(!test((char*)"gee", (char*)"g*k"));             // No because 'k' is not in p
    assert(!test((char*)"pqrst", (char*)"*pqrs"));         // No because 't' is not in s
    assert(test((char*)"abcdhghgbcd", (char*)"abc*bcd"));  // Yes
    assert(!test((char*)"abcd", (char*)"abc*c?d"));        // No because p must have 2 instances of 'c'
    assert(test((char*)"abcd", (char*)"*c*d"));            // Yes
    assert(test((char*)"abcd", (char*)"*a*cd"));           // Yes
    assert(test((char*)"aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaa"
                       "aaabbaabbbbaababbababaabbbaababbbba",
        (char*)"*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*")); // Yes

    cout << "self test passed!" << endl;
    return 0;
}
