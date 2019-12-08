/**
 *
 * 215. Kth Largest Element in an Array
 *
 * SOLUTION
 * ===============================================================================
 * 1. min heap with max size k
 *
 * Complexity:
 * O(NlogK)
 *
 * Follow up
 * ===============================================================================
 * How to implement priority_queue to support push, pop, top?
 * Implement function maintainHeap(int k), to maintain the heap with top index i.
 * This function maintain the heap, which is violated because of the updated top value.
 * 1) push(int v): append value to array.
 *        do {n = parent(n);maintainHeap(n)} while (n);
 * Complexity: O(logN)
 * 2) pop(): swap top and last element, maintainHeap(0).
 *       return the former top element.
 * Complexity: O(logN)
 * 3) top: return top element(0th element).
 * Complexity: O(1)
 *
 */

#include <debug.hpp>

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int result;
        result = findKthLargestMinHeap(nums, k);

        return result;
    }

    int findKthLargestMinHeap(vector<int>& nums, int k) {
        //auto f = [&nums](int a, int b) {
            //return nums[a] > nums[b];
        //};
        //priority_queue<int, vector<int>, decltype(&f)> heap{f};

        priority_queue<int, vector<int>, std::greater<int>> heap;
        // assume k valid
        for (int i = 0; i < (int) nums.size(); ++i) {
            if ((int)heap.size() < k) {
                heap.push(nums[i]); // push when heap size less than k
            } else if (heap.top() < nums[i]) {
                heap.pop(); // pop and push to replace top element
                heap.push(nums[i]);
            }
        }

        return heap.top();
    }
};

int test() {
    Solution solution;

    vector<int> nums;
    int k;
    int result;

    nums = {1};
    k = 1;
    result = 1;
    assert(solution.findKthLargest(nums, k) == result);

    nums = {2, 1};
    k = 2;
    result = 1;
    assert(solution.findKthLargest(nums, k) == result);

    nums = {3, 2, 1, 5, 6, 4};
    k = 2;
    result = 5;
    assert (solution.findKthLargest(nums, k) == result);

    cout << "self test passed!" << endl;

    return 0;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
