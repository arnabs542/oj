/**
 *
31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater
permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie,
sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the
right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

SOLUTION
================================================================================
2. Lexicographical order

Take '123' for example:
123, + 1 -> 124 -> 132
132, + 1 -> 133
213
231
312
321

If the sequence is lexicographically decreasing, then it's the largest permutation.
To find a next permutation, we need to find a rightmost non-decreasing sequence, since
right positions are less significant as for lexicographical order.

Procedure:
- Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
- Find the largest index l greater than k such that a[k] < a[l].
- Swap the value of a[k] with that of a[l].
- Reverse the sequence from a[k + 1] up to and including the final element a[n].

How to deal with duplicate elements?


FOLLOW UP
================================================================================
1. How about permutations of m given n numbers? A_{4}^{2}
1,2,3 → 1,2,4
1,3,2 → 1,3,4
1,3,4 → 1,4,2

 *
 */

#include <debug.hpp>

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        cout << nums << " => ";
        nextPermutationLexicographicalOrder(nums);
        cout << " " << nums << endl;

    }

    void nextPermutationLexicographicalOrder(vector<int> &nums) {
        int n = (int)nums.size();
        int i = n - 1;
        for (; i > 0 && nums[i] <= nums[i-1]; --i); // nums[i-1] < nums[i]
        if (i <= 0)  {
            sort(nums.begin(), nums.end());
            return; // decreasing sequence, largest permutation already
        }
        //cout << nums << " " << i << " " << nums[i-1] << endl;
        //auto rit = upper_bound(nums.rbegin(), nums.rend(), nums[i-1]); // [i, n -1]
        auto rit = upper_bound(nums.rbegin(), nums.rbegin() + n-i, nums[i-1]); // [i, n -1]. XXX: need to pass monotonic subarray!
        assert(rit != nums.rend());
        swap(nums[i-1], *rit);
        reverse(nums.rbegin(), nums.rbegin() + (n-i)); // reverse [i, n-1]
    }
};

int test() {

    Solution solution;
    vector<int> nums;
    vector<int> output;

    nums = {};
    output = {};
    solution.nextPermutation(nums);
    assert(nums == output);

    nums = {0};
    output = {0};
    solution.nextPermutation(nums);
    assert(nums == output);

    nums = {1, 2, 3};
    output = {1, 3, 2};
    solution.nextPermutation(nums);
    assert(nums == output);

    nums = {3, 2, 1};
    //output = {3, 2, 1};
    output = {1, 2, 3,};
    solution.nextPermutation(nums);
    assert(nums == output);

    nums = {1, 1, 5};
    output = { 1, 5, 1};
    solution.nextPermutation(nums);
    assert(nums == output);

    return 0;
}

int main(int argc, char **argv) {
    test();

    return 0;
}
