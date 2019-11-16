/**
 *
280. Wiggle Sort

Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] ,=
nums[3]....

Example
    Input: nums = [3, 5, 2, 1, 6, 4]
    Output: One possible answer is [3,5,1,6,2,4]

SOLUTION
================================================================================

1. Sort and swap adjacent elements

- Sort.
- Swap nums[2i+1] and nums[2i+2], i = 0, 1, ...

Complexity:
O(NlogN)

2. Scan and swap

Keep track of state j, indicating longest subarray [0,j] that
have already been wiggle sorted.
Then, figure out the state transition of j.
if j is odd:
    if nums[j+1]<= nums[j], j += 1
    else:
        swap nums[j+1], nums[j], j += 1
if j is even:
    symmetric logic...


0: 123
1: 123
2: 132


Complexity:
O(N)

 *
 */

#include <debug.hpp>

class Solution {
public:
    void wiggleSort(vector<int> &nums) {
        cout << nums << "=>";
        wiggleSortPartition(nums);
        cout << nums << endl;
    }

    void wiggleSortPartition(vector<int> &nums) {
        int i = 0;
        while (i < (int)nums.size() - 1) {
            if ((i%2 && nums[i] < nums[i + 1])
                    || (i%2==0 && nums[i]>nums[i+1])) {
                int tmp = nums[i];
                nums[i] = nums[i+1];
                nums[i+1] = tmp;
            }
            ++i;
        }

    }
};

int main(int argc, char *argv[])
{
    // TODO: submit & test
    Solution solution;
    vector<int> nums;

    nums = {};
    solution.wiggleSort(nums);
    nums = {1};
    solution.wiggleSort(nums);
    nums = {2,1};
    solution.wiggleSort(nums);
    nums = {1,2};
    solution.wiggleSort(nums);
    nums = {1,2,3};
    solution.wiggleSort(nums);
    nums = {3,5,2,1,6,4};
    solution.wiggleSort(nums);

    return 0;
}
