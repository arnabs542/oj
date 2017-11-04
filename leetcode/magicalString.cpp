/*
 *
481. Magical String

A magical string S consists of only '1' and '2' and obeys the following rules:

The string S is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string S itself.

The first few elements of string S is the following: S = "1221121221221121122……"

If we group the consecutive '1's and '2's in S, it will be:

1 22 11 2 1 22 1 22 11 2 11 22 ......

and the occurrences of '1's or '2's in each group are:

1 2	2 1 1 2 1 2 2 1 2 2 ......

You can see that the occurrence sequence above is the S itself.

Given an integer N as input, return the number of '1's in the first N number in the magical string S.

Note: N will not exceed 100,000.

Example 1:
Input: 6
Output: 3
Explanation: The first 6 elements of magical string S is "12211" and it contains three 1's, so return 3.


==============================================================================================
SOLUTION

S:        1221121221221121122
Group:    1 22 11 2 1 22 1 22 11 2 11 22 ......
Count:    1 2  2  1 1 2  1 2  2  1 2  2 ......
Generate: 122112122122

1. Generate the sequence and count.

State:
Current string, current character to append, count(how many times does current character repeat),
group(group rank/index of characters).

Complexity: O(n), O(n).

*/

#include <assert.h>
#include <memory>
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int magicalString(int n)
    {
        //int result = magicalStringGenerate(n);
        int result = magicalStringGenerateOpt(n);
        cout << "result: " << result << endl;

        return result;
    }

    /*
     * Performance: 29ms
     */
    int magicalStringGenerate(int n)
    {
        //string S = "1221121221221121122";
        //string S = "1";
        unsigned int nOnes = 0;
        string S = "";
        string currentChar = "1";
        unsigned int group = 0; // group index
        int count = 0;          // number of elements in current group
        while ((int)S.size() < n) {
            // continue generating
            if (S.size() < group + 1) {
                count = stoi(currentChar);
            } else {
                count = stoi(S.substr(group, 1));
                //count = atoi(S.at(group));
            }
            //cout << "count: " << count << ", character: " << currentChar << endl;
            for (int i = 0; i < count; ++i) {
                S.append(currentChar);
            }

            // accumulate result
            if (!currentChar.compare("1")) {
                nOnes += count; // DONE: count number of ones
                if ((int)S.size() > n)
                    nOnes--;
            }

            // update state
            ++group;
            currentChar = (currentChar.compare("1") == 0) ? "2" : "1";
        }
        //cout << "S=" << S << ", number of ones: " << nOnes << endl;
        return nOnes;
    }

    // FIXME: above solution too slow, why?

    /*
     * Optimized: using integers instead of string.
     *
     * Performance: 6ms
     */
    int magicalStringGenerateOpt(int n)
    {
        unsigned int nOnes = 0;
        vector<int> S;
        int currentChar = 1;
        unsigned int group = 0; // group index
        int groupSize = 0;          // number of elements in current group

        while ((int)S.size() < n) { // a standard C++ compiler will handle comparison between integers of different signs by casting signed number x as an unsigned int before doing the comparison, which may turn a negative number into a large positive number
            // continue generating
            groupSize = (S.size() < group + 1) ? currentChar : S[group];
            for (int i = 0; i < groupSize; ++i)
                S.push_back(currentChar);

            // accumulate result
            if (currentChar == 1) {
                nOnes += groupSize; // DONE: count number of ones
                if ((int)S.size() > n)
                    nOnes--;
            }

            // update state
            ++group;
            currentChar ^= 3;
        }
        //if (n >= 0) nOnes = count(S.begin(), S.begin() + n, 1);
        return nOnes;
    }
};

void test()
{
    //Solution solution;
    shared_ptr<Solution> solution = make_shared<Solution>();
    //shared_ptr<Solution> solution = shared_ptr<Solution>(new Solution());
    //Solution *solution = new Solution();

    assert(solution->magicalString(-1) == 0);
    assert(solution->magicalString(0) == 0);
    assert(solution->magicalString(1) == 1);
    assert(solution->magicalString(2) == 1);
    assert(solution->magicalString(3) == 1);
    assert(solution->magicalString(4) == 2);
    assert(solution->magicalString(10) == 5);
    assert(solution->magicalString(10000) == 4996);

    cout << "self test passed!" << endl;
}

int main(int argc, char* argv[])
{
    test();
    return 0;
}
