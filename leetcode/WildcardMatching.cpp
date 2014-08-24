#include <iostream>
#include <stdio.h>

class Solution
{
  public:
    bool isMatch(const char *s, const char *p)
    {
        // char *p = pattern, *t = text;
        const char *t = s;
        const char *pp = NULL, *tp = NULL; // previous p and t for backtrack.
        while (*p && *t)
        {
            /*if (*p == '\0' && *t == '\0')*/
            /*return true;*/
            if (*p == *t || *p == '?')
            {
                p++;
                t++;
            }
            else if (*p == '*')
            {
                pp = p;
                tp = t;
                p++;
            }
            else
            {
                if (pp && tp)
                {
                    tp++;
                    p = pp + 1;
                    t = tp;
                }
                else
                    return false;
            }
        }
        while (*p == '*')
            p++;
        return !*p;
    }
};

// A function to run test cases
void test(char *s, char *p)
{
    Solution().isMatch(s, p) ? puts("Yes") : puts("No");
}

// Driver program to test above functions
int main()
{
    test("geeks", "g*ks");           // Yes
    test("geeksforgeeks", "ge?ks*"); // Yes
    test("gee", "g*k");              // No because 'k' is not in p
    test("pqrst", "*pqrs");          // No because 't' is not in s
    test("abcdhghgbcd", "abc*bcd");  // Yes
    test("abcd", "abc*c?d"); // No because p must have 2 instances of 'c'
    test("abcd", "*c*d");    // Yes
    test("abcd", "*?c*d");   // Yes
    test("aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaa"
         "aaabbaabbbbaababbababaabbbaababbbba",
         "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*");
    return 0;
}
