/**
 *
 *
 Number of swaps to sort when only adjacent swapping allowed
 https://www.geeksforgeeks.org/number-swaps-sort-adjacent-swapping-allowed/
 *
 * ===============================================================================
 * SOLUTION
 *
 * 1. Brute force - Bubble sort
 *
 * Complexity: O(N²)
 *
 * 2. Count inversion pairs
 * This is the problem of "count of smaller numbers after self".
 *
 * Complexity: O(NlogN)
 *
 */
#include <debug.hpp>

class Solution {
    public:
        int numberSwaps(vector<int> &nums) {
            // TODO: implementation
        }
};

int test() {
    cout << "passed" << endl;
    return 0;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
