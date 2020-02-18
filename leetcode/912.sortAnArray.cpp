/**
 *
912. Sort an Array
Medium

Given an array of integers nums, sort the array in ascending order.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]


Constraints:

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000

Accepted
48,919
Submissions
78,095

SOLUTION
================================================================================

1. Insertion sort - adding new elements

Complexity: O(N²)

2. Heap sort - adding new elements

Complexity: O(NlogN)

3. Quick sort - divide and conquer with nondeterministic dividing, inplace

Complexity: O(NlogN)

4. Merge sort - divide and conquer with deterministic dividing

Complexity: O(NlogN)

Above are all comparison based sorting.
Sorting with buckets counting: bucket sorting, radix sorting.
4. Bucket - divide and conquer with deterministic dividing

Complexity: O(N)

FOLLOW UP
================================================================================
1. Sort a nearly sorted (or K sorted) array
Given an array of n elements, where each element is at most k away from its target position, devise an algorithm that sorts in O(n log k) time.

We have to approaches:
1) Add elements one by one: find right position to insert, O(k)
2) Fill positions one by one: find the minimum within window of size k!

First approach:
1) Add new element - insert sort: for each number, find its right position in
the window of size k, and make room for it.
Complexity: O(nk)

For the second approach, the objective is to find the MINIMUM in range!
1) Fill position: find minimum in the window and swap.
Complexity: O(nk)
2) Fill position: maintain a min heap of size k: pop the minimum to put to the
result array, and add a new element after pop.
Complexity: O(nlogk)

 *
 */
#include <debug.hpp>

class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        vector<int> output;
        //output = sortArrayBuiltinSort(nums);
        output = sortArrayMergeSort(nums);

        cout << nums << " => " << output << endl;

        return output;
    }

    vector<int> sortArrayBuiltinSort(vector<int>& nums) {
        vector<int> output = nums;
        std::sort(output.begin(), output.end());
        return output;
    }

    template<class T>
    int mergeSort(vector<T> &nums, int low, int high) {
        if (low >= high) return 0;
        int mid = (low + high) >> 1;
        // divide
        mergeSort(nums, low, mid); // [low, mid]
        mergeSort(nums, mid + 1, high); // [mid+1, high]
        // combine
        int k = low, p = 0, q = 0; // [low, high], [0, mid-low], [0, high-mid-1]
        vector<int> left(nums.begin() + low, nums.begin() + mid + 1); // mid - low + 1
        vector<int> right(nums.begin() + mid + 1, nums.begin() + high + 1); // high - mid
        while (p <= mid-low || q <= high-mid-1) {
            if (p > mid-low) {
                nums[k++] = right[q++];
            } else if (q > high-mid-1) {
                nums[k++] = left[p++];
            } else {
                if (left[p] <= right[q]) { nums[k++] = left[p++]; }
                else { nums[k++] = right[q++]; }
            }
        }

        return 0;
    }

    vector<int> sortArrayMergeSort(vector<int>& nums) {
        vector<int> output = nums;
        mergeSort(output, 0, output.size() - 1);

        return output;
    }
};

int test() {
    Solution solution;

    vector<int> nums;
    vector<int> output;

    nums = {};
    output = nums; sort(output.begin(), output.end());
    assert(solution.sortArray(nums) == output);

    nums = {5, 4, 3, 2, 1};
    output = nums; sort(output.begin(), output.end());
    assert(solution.sortArray(nums) == output);

    cout << "test passed"<< endl;
    return 0;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
