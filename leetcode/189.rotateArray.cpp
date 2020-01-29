/**
 *
189. Rotate Array

Total Accepted: 96377
Total Submissions: 420656
Difficulty: Easy
Contributors: Admin

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve
this problem.

Hint:
Could you do it in-place with O(1) extra space?

The easiest solution would use additional memory and that is perfectly fine.
The actual trick comes when trying to solve this problem without using any additional memory. This means you need to use the original array somehow to move the elements around. Now, we can place each element in its original location and shift all the elements around it to adjust as that would be too costly and most likely will time out on larger input arrays.
One line of thought is based on reversing the array (or parts of it) to obtain the desired result. Think about how reversal might potentially help us out by using an example.
The other line of thought is a tad bit complicated but essentially it builds on the idea of placing each element in its original position while keeping track of the element originally in that position. Basically, at every step, we place an element in its rightful position and keep track of the element already there or the one being overwritten in an additional variable. We can't do this in one linear pass and the idea here is based on cyclic-dependencies between elements.

SOLUTION
================================================================================

1. Copy and map

Complexity: O(n), O(n)

2. Brute force inplace - shift one, repeat for k times

Complexity: O(kn), O(1)

3. Dependency graph cycle - dfs - chained iterative

Model this as a graph.

VERTICES AND EDGES
We will have n nodes and an edge directed from node i to node j,
if the element at i'th index must be present at j’th index in the sorted array.

A simple path is like this: i -> i - k -> i - k -k.

The problem is it may not be able to traverse all the nodes, because there are
maybe more than one cycles in the dependency graph!
Doesn't work?

Well we can begin dfs at each number if it's not filled with new value yet.
How to decide whether a position is visited or not?
1) We can know that with extra storage by keeping track of visit state of nodes.
2) After first traversal starting at index 0, if adjacent 1 is visited,
then all is visited. So if there are other nodes not visited, they must be
accessible by visiting cycles starting at j where j in [1, k-1].

All in another perspective, start at i, stop when i + pk >= n, then at most
n/k elements are visited. We need to repeat for at most k-1 times.

[1, 2, 3], k = 2: 1 -> 3 -> 2 -> 1
[1, 2, 3, 4], k = 2: 1 -> 3 -> 1
If we start at index i, the paths are composed of (i + mk) % n, where k in [0, n-1].

4. Reverse by swap
Reverse is an operation we can carry out inplace.

Suppose we will shift the array to the left by k steps.
Divide the array into two parts AB, where A = arr[0..k-1] and B = arr[k..n-1].
Then Input is AB, after rotating, it must be BA.

The idea of the algorithm is:

- Reverse A to get ArB, where Ar is reverse of A.
- Reverse B to get ArBr, where Br is reverse of B.
- Reverse all to get (ArBr) r = BA.

(ArBr)r = BA is the key property of reverse operation.

A[0] -> A[-k] -> A[n-k].
A[n-k] symmetric to A[k].
And A[0] is symmetric to A[k].

Reference:
https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/

5. Block swap

Reference:
https://www.geeksforgeeks.org/block-swap-algorithm-for-array-rotation/



Related problem:
Reverse Words in a String II
Rotate Image

================================================================================
FOLLOW UP
1. Minimum swaps to make array sorted
Graph cycle dependency.

 *
 */
#include <debug.hpp>

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        cout << nums << " " << k;
        //rotateCopy(nums, k);
        //rotateReverse(nums, k);
        rotateDependencyGraphCycle(nums, k);
        cout << " => " << nums << endl;
    }

    void rotateCopy(vector<int>& nums, int k) {
        int n = nums.size();
        if (!n) return;
        vector<int> nums0 = nums;
        for (int i = 0; i < (int)nums.size(); ++i) {
            nums[(i+k) % n] = nums0[i];
        }
    }

    void rotateReverse(vector<int>& nums, int k) {
        int n = nums.size();
        if (!n) return;

        k %= n;
        reverse(nums.begin(), nums.begin() + n - k); // left n - k
        reverse(nums.begin() + n - k, nums.end()); // right k
        reverse(nums.begin(), nums.end());
    }

    void rotateDependencyGraphCycle(vector<int>& nums, int k) {
        int n = nums.size();
        if (!n) return;
        k %= n;
        int remaining = n;
        for (int i = 0; i < k && remaining; ++i) { // cycle entries are in continuous region of subspace in [0, k-1].
            int u = i; // cycle entry
            int value = nums[u];
            do {
                int v = (u + k) % n;
                swap(nums[v], value); // put previous value to position, backup original value
                u = v;
                --remaining;
            } while (u != i); // visited a cycle
        }
    }
};

int test() {

    vector<int> nums;
    vector<int> output;
    int k;

    Solution solution;

    nums = {};
    k = 0;
    output = {};
    solution.rotate(nums, k);
    assert(nums == output);

    nums = {1};
    k = 1;
    output = {1};
    solution.rotate(nums, k);
    assert(nums == output);

    nums = {1, 2, 3, 4, 5, 6, 7};
    k = 3;
    output = {5, 6, 7, 1, 2, 3, 4};
    solution.rotate(nums, k);
    assert(nums == output);

    cout << "test passed" << endl;

    return 0;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
