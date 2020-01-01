/**
 *
507. Perfect Number
Easy

We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)

Accepted
51.9K
Submissions
147.7K

SOLUTION
================================================================================

 *
 */

#include <debug.hpp>

class Solution {
public:
    bool checkPerfectNumber(int num) {
        bool result = checkPerfectNumberBruteForce(num);

        cout << num << " " << result << endl;
        return result;
    }

    bool checkPerfectNumberBruteForce(int num) {
        if (num == 0) return false;
        int x = num;
        for (int i = 1; i <= num/2; ++i) {
            if (num % i == 0) x -= i;
            if (x < 0) return false;
        }
        return x == 0;
    }
};

int test() {
    Solution solution;

    assert(solution.checkPerfectNumber(0) == false);
    assert(solution.checkPerfectNumber(28) == true);
    assert(solution.checkPerfectNumber(99999997) == false);

    return 0;
}

int main() {
    return test();
}
