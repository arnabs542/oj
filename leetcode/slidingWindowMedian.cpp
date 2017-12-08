/**
 *
480. Sliding Window Median

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.


==============================================================================================
SOLUTION

Similar problem to 'Find Median from Data Stream', except that removing element is involved here.

1. Naive solution, sort every time

Complexity: O(NKlogK)

2. Weak Ordering data structure
Median is an order statistics.
Ordering related data structures are sorted list, (balanced)binary search tree.

Balanced binary search tree?
- Search: O(logK)
- Insert: O(logK)
- Remove: O(logK)

Complexity: O(NlogK)

Heaps
- Search: O(logK)
- Insert: O(logK)
- Remove: O(logK)
Complexity: O(NlogK)

 */

#include <debug.hpp>


class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        cout << "input: " << nums << endl;
        vector<double> result = _medianSlidingWindowTree(nums, k);
        cout << "result: " << result << endl;
        return result;
    }

    vector<double> _medianSlidingWindowTree(vector<int>& nums, int k) {
        vector<double> result;
        multiset<int> mset;
        multiset<int>::iterator median;
        int n = 0;
        if (k <= 0) { return result; }

        for (int i = 0; i < (int)nums.size(); ++i) {
            n = mset.size();
            // INSERT AND UPDATE median pointer
            //cout << "insert: " << nums[i] << endl;
            mset.insert(nums[i]);
            if (!n) { median = mset.begin(); }
            else if (n & 1 && nums[i] < *median) {
                --median;
            } else if (!(n&1) && nums[i] >= *median) {
                ++median;
            }

            ++n;
            // DELETE AND UPDATE median pointer
            if (n > k) {
                // update median pointers because of inserting element
                multiset<int>::iterator it = mset.lower_bound(nums[i - k]);
                if (nums[i - k] <= *median) {
                    if (n & 1) { // odd size
                        if (it == median) {
                            --median;
                        }
                    }
                    else { // even size, go right
                        ++median;
                    }
                } else { // element to erase is greater than
                    if (n & 1) {
                        --median;
                    }
                }
                mset.erase(it);
                --n;
            }
            if (n < k) { continue; }
            if (n & 1) {
                result.push_back(*median);
            } else {
                //result.push_back(0.5 * *median + 0.5 * *next(median, 1));
                result.push_back(0.5 * (0.0 + *median + *next(median, 1)));
            }
        }

        return result;
    }
};

void test() {
    Solution solution;

    vector<int> nums;
    vector<double> medians;
    int k = 0;

    nums = vector<int>({});
    k = 0;
    medians = vector<double>({});
    assert(solution.medianSlidingWindow(nums, k) == medians);

    nums =  vector<int>({1,3,-1,-3,5,3,6,7});
    medians = vector<double>({1, -1, -1, 3, 5, 6});
    k = 0;
    assert(solution.medianSlidingWindow(nums, k) == vector<double>({}));
    k = 3;
    assert(solution.medianSlidingWindow(nums, k) == medians);
    k = 4;
    medians = vector<double>({0, 1, 1, 4, 5.5});
    assert(solution.medianSlidingWindow(nums, k) == medians);

    nums = vector<int>({1, 2, 3, 4, 5, 6, 7});
    k = 2;
    medians = vector<double>({1.5, 2.5, 3.5, 4.5, 5.5, 6.5});
    assert(solution.medianSlidingWindow(nums, k) == medians);
    k = 3;
    medians = vector<double>({2, 3, 4, 5, 6,});
    assert(solution.medianSlidingWindow(nums, k) == medians);

    nums = vector<int>({7, 6, 5, 4, 3, 2, 1});
    k = 2;
    medians = vector<double>({6.5, 5.5, 4.5, 3.5, 2.5, 1.5});
    assert(solution.medianSlidingWindow(nums, k) == medians);

    // overflow
    nums = vector<int>({2147483647, 2147483647}); // 2 ^ 31 - 1
    k = 2;
    medians = vector<double>({2147483647});
    assert(solution.medianSlidingWindow(nums, k) == medians);

    nums = vector<int>({-2147483647, -2147483647}); // 2 ^ 31 - 1
    k = 2;
    medians = vector<double>({-2147483647});
    assert(solution.medianSlidingWindow(nums, k) == medians);

    cout << "self test passed!" << endl;
}

int main(int argc, char *argv[])
{
    test();

    return 0;
}

