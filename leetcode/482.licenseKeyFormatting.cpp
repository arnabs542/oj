/**
 *
482. License Key Formatting
Easy

You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.

Example 1:
Input: S = "5F3Z-2e-9-w", K = 4

Output: "5F3Z-2E9W"

Explanation: The string S has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:
Input: S = "2-5g-3-J", K = 2

Output: "2-5G-3J"

Explanation: The string S has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
Note:
The length of string S will not exceed 12,000, and K is a positive integer.
String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
String S is non-empty.

SOLUTION
================================================================================

1. Scan and count

State machine perspective?

XXX: Be careful about "except the first part as it could be shorter".
The output is deterministic!

Complexity: O(n)

 *
 */

#include <debug.hpp>

class Solution {
public:
    string licenseKeyFormatting(string S, int K) {
        string result;
        result = licenseKeyFormattingBackwardScan(S, K);

        cout << S << " " << K << " => " << result << endl;

        return result;
    }

    string licenseKeyFormattingBackwardScan(string S, int K) {
        string output;
        vector<char> parts;
        vector<char> part;
        int i = 0;
        for (i = (int)S.size() - 1; i >= 0; --i) {
            if (S[i] == '-' && i) { // XXX: && i
                //if (parts.size() == 0) {
                    //parts.push_back(std::move(part));
                    //part.push_back('-'); // XXX
                    //parts.insert(parts.end(), part.begin(), part.end());
                    //part.clear(); // XXX
                //}
                continue;
            }
            else if ((int)part.size() < K) part.push_back(std::toupper(S[i]));
            //cout << "processing " << i << "  " << S[i] << endl;
            //if(i == 0) cout << part << endl;

            if (i == 0 || (int)part.size() == K) {
                    if (i != 0) part.push_back('-');
                    //parts.push_back(std::move(part));
                    parts.insert(parts.end(), part.begin(), part.end()); // XXX
                    part.clear();
            }

        }
        //cout << parts << endl;
        while (parts.size() && parts.back() == '-') parts.pop_back();
        //i = parts.size() - 1;
        //while (i >= 0 && parts[i] == '-') --i; // trim trailing -
        output = string(parts.rbegin(), parts.rend());

        return output;
    }
};

int test() {

    Solution solution;
    string S;
    int K;
    string output;

    S = "";
    K = 0;
    output = "";
    assert(solution.licenseKeyFormatting(S, K) == output);

    S = "";
    K = 2;
    output = "";
    assert(solution.licenseKeyFormatting(S, K) == output);

    S = "5F3Z-2e-9-w"; K = 4;
    output = "5F3Z-2E9W";
    assert(solution.licenseKeyFormatting(S, K) == output);

    S = "2-5g-3-J"; K = 2;
    output = "2-5G-3J";
    assert(solution.licenseKeyFormatting(S, K) == output);

    S = "12234-23";
    K = 2;
    output = "1-22-34-23";
    assert(solution.licenseKeyFormatting(S, K) == output);

    S = "--a-a-a-a--";
    K = 2;
    output = "AA-AA";
    assert(solution.licenseKeyFormatting(S, K) == output);

    S = "--------EyRfCyHxyUJzhygiazYpjuDFdHvrnDwoQKQEsccLDiwhpmjueADIzqIvExbDDFnEGovAxYeszbzuTekRuWUPXRPbVKJuDQzIzzTj";
    K = 16;
    output = "EYRF-CYHXYUJZHYGIAZYP-JUDFDHVRNDWOQKQE-SCCLDIWHPMJUEADI-ZQIVEXBDDFNEGOVA-XYESZBZUTEKRUWUP-XRPBVKJUDQZIZZTJ";
    assert(solution.licenseKeyFormatting(S, K) == output);

    cout << "self test passed!" << endl;

    return 0;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
