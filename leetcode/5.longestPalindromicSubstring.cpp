/*
 * 5. Longest Palindromic Substring
 *
 * Total Accepted: 136906
 * Total Submissions: 572137
 * Difficulty: Medium
 * Given a string S, find the longest palindromic substring in S. You may assume
 * that the maximum length of S is 1000, and there exists one unique longest
 * palindromic substring.
 *
 * ANALYSIS:
 *  A typical overlapping substructured problem can be solved by DYNAMIC PROGRAMMING.
 *  Let table[i][j] denote whether the substring [i, ..., j] is palindromic, then we
 *  have such state transition relation:
 *      table[i][j] == table[i + 1][j - 1] && string[i] == string[j]
 */

#include <iostream>
#include <string>
#include <debug.hpp>

using namespace std;

class Solution
{
public:
    string longestPalindrome(string s) {
        string result = _longestPalindromeDP(s);

        cout << s << " => " << result << endl;

        return result;
    }

    string _longestPalindromeDP(string s) {
        int n = s.length();
        int longestBegin = 0;
        int maxLen = 1;
        bool table[1000][1000] = {false};
        for (int i = 0; i < n; i++)
        {
            table[i][i] = true;
        }
        for (int i = 0; i < n - 1; i++)
        {
            if (s[i] == s[i + 1])
            {
                table[i][i + 1] = true;
                longestBegin = i;
                maxLen = 2;
            }
        }
        for (int len = 3; len <= n; len++)
        {
            for (int i = 0; i < n - len + 1; i++)
            {
                int j = i + len - 1;
                if (s[i] == s[j] && table[i + 1][j - 1])
                {
                    table[i][j] = true;
                    longestBegin = i;
                    maxLen = len;
                }
            }
        }
        return s.substr(longestBegin, maxLen);
    }
};

int main()
{
    Solution s = Solution();
    std::cout << s.longestPalindrome("ukxidnpsdfwieixhjnannbmtppviyppjgbsludrzdleeiydzawnfmiiztsjqqqnthwinsqnrhfjxtklvbozkaeetmblqbxbugxycrlzizthtuwxlmgfjokhqjyukrftvfwikxlptydybmmzdhworzlaeztwsjyqnshggxdsjrzazphugckgykzhqkdrleaueuajjdpgagwtueoyybzanrvrgevolwssvqimgzpkxehnunycmlnetfaflhusauopyizbcpntywntadciopanyjoamoyexaxulzrktneytynmheigspgyhkelxgwplizyszcwdixzgxzgxiawstbnpjezxinyowmqsysazgwxpthloegxvezsxcvorzquzdtfcvckjpewowazuaynfpxsxrihsfswrmuvluwbdazmcealapulnahgdxxycizeqelesvshkgpavihywwlhdfopmmbwegibxhluantulnccqieyrbjjqtlgkpfezpxmlwpyohdyftzgbeoioquxpnrwrgzlhtlgyfwxtqcgkzcuuwagmlvgiwrhnredtulxudrmepbunyamssrfwyvgabbcfzzjayccvvwxzbfgeglqmuogqmhkjebehtwnmxotjwjszvrvpfpafwomlyqsgnysydfdlbbltlwugtapwgfnsiqxcnmdlrxoodkhaaaiioqglgeyuxqefdxbqbgbltrxcnihfwnzevvtkkvtejtecqyhqwjnnwfrzptzhdnmvsjnnsnixovnotugpzuymkjplctzqbfkdbeinvtgdpcbvzrmxdqthgorpaimpsaenmnyuyoqjqqrtcwiejutafyqmfauufwripmpcoknzyphratopyuadgsfrsrqkfwkdlvuzyepsiolpxkbijqw");
}


