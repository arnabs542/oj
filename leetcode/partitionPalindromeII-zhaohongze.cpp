// Given a string s, partition s such that every substring of the partition is a
// palindrome.

// Return the minimum cuts needed for a palindrome partitioning of s.

// For example, given s = "aab",
// Return 1 since the palindrome partitioning ["aa","b"] could be produced using
// 1 cut.

// Solution:
//@1 Dynamic Programming:
// Use DP to check whether a string is palindromic
// Use DP to decide the min cut of a string by partitioning it,
// with the recurrence similar to the matrix chain order problem

// table[i][j]=
//      -1  (initialization)
//      0   (palindrome)
//      n   (n>0,not palindrome,n is the min cut of palindromic partitioning)

#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution
{
  public:
    //@param s,a string
    //@return an integer
    int minCut(string s)
    {
        vector<int> minCuts(s.length() + 1, 0);
        for (int i = 0; i <= s.length(); i++)
        {
            minCuts[i] = i - 1;
        }
        vector<bool> temp(s.length() + 1, false);
        vector<vector<bool> > isPalFast(s.length() + 1, temp);
        for (int i = 2; i <= s.length(); i++)
        {
            for (int j = 1; j <= i; j++)
            {
                if (s[i - 1] == s[j - 1] &&
                    ((i - j) < 2 || isPalFast[j + 1][i - 1]))
                {
                    isPalFast[j][i] = true;
                    minCuts[i] = min(minCuts[i], minCuts[j - 1] + 1);
                }
            }
        }
        return minCuts[s.length()];
    }
};

int main(int argc, char **argv)
{
    std::cout << Solution().minCut("abaa");
    // std::cout <<
    // Solution().minCut("adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece");
    return 0;
}
