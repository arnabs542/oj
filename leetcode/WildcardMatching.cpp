#include <iostream>
#include <stdio.h>

class Solution
{
public:
    bool isMatch(const char *s, const char *p)
    {
        // If we reach at the end of both strings, we are done
        if (*s == '\0' && *p == '\0')
            return true;

        // Make sure that the characters after '*' are present in p string.
        // This function assumes that the s string will not contain two
        // consecutive '*'
        //if (*s == '*' && *(s + 1) != '\0' && *p == '\0')
        //return false;

        // If the s string contains '?', or current characters of both
        // strings match
        if (*p == '?' || *s == *p)
            return this->isMatch(s + 1, p + 1);

        // If there is *, then there are two possibilities
        // a) We consider current character of p string
        // b) We ignore current character of p string.
        if (*p == '*')
        {
            if (*s != '\0')
                return this->isMatch(s + 1, p) || this->isMatch(s, p + 1);
            else
                return *(p + 1) == '\0';
        }
        return false;
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
    test( "geeks", "g*ks"); // Yes
    test( "geeksforgeeks", "ge?ks*"); // Yes
    test( "gee", "g*k"); // No because 'k' is not in p
    test( "pqrst", "*pqrs"); // No because 't' is not in s
    test( "abcdhghgbcd", "abc*bcd"); // Yes
    test( "abcd", "abc*c?d"); // No because p must have 2 instances of 'c'
    test( "abcd", "*c*d"); // Yes
    test( "abcd", "*?c*d"); // Yes
    test( "aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba", "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*");
    return 0;
}

