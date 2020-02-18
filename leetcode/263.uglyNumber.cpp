/**
 *
263. Ugly Number

Total Accepted: 79362
Total Submissions: 208465
Difficulty: Easy
Contributors: Admin

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For
example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.

SOLUTION
================================================================================

1. Keep dividing if we can
Complexity: O(N)

 *
 */
#include <debug.hpp>

class Solution {
public:
    bool isUgly(int num) {
        bool result;

        result = isUglyDivide(num);
        cout << num << " => " << result << endl;
        return result;
    }

    bool isUglyDivide(int num) {
        if (num == 0) return false;
        static vector<int> const factors{2, 3, 5};
        for (int factor: factors) {
            while (num % factor == 0) {
                num /= factor;
            }
        }
        return num == 1;
    }
};

int test() {
    Solution solution;
    assert(solution.isUgly(6) == true);
    assert(solution.isUgly(0) == false);
    cout << "passed" << endl;
    return 0;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
