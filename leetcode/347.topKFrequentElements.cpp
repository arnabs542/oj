/**
 *
 *
347. Top K Frequent Elements

Total Accepted: 44317
Total Submissions: 96835
Difficulty: Medium
Contributors: Admin

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the
array's size.

================================================================================
SOLUTION

1. Hash to store elements' occurrence frequency. And, for top K problem, use HEAP.

Complexity: O(n + nlogk)

2. Hash and sort according to occurrence count.

Complexity: O(NlogN)

3. Bucket - separate chaining in hash table collision resolution method
The possible values for the occurrence are in range [0, n].
Maintain the occurrence count in the buckets, and get the largest k buckets.

4. Separate chaining on data stream - one pass

To do this in O(n) time, we need to maintain
1) mapping from number to occurrence count
2) mapping from occurrence count to chained elements list
3) chained elements list, supporting O(1) insert and delete. Set or doubly linked list?

================================================================================
FOLLOW UP
1. Top k frequent elements in data stream?
Solution: separate chaining, like least frequently used cache implementation.
Refer to the cpp implementation.




 *
 */
#include <debug.hpp>

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> result;
        result = topKFrequentSeparateChain(nums, k);

        cout << nums << " " << k << " => "  << result << endl;

        return result;
    }

    vector<int> topKFrequentSeparateChain(vector<int> &nums, int k) {
        vector<int> result;
        vector<unordered_set<int>> buckets(nums.size()+1); // map occurrence to chain list, [0, n]
        unordered_map<int, int> num2count;

        for (int e: nums) { // build buckets of separate chain list
            if (num2count.count(e)) {
                buckets[num2count[e]].erase(e); // remove from old chain
            }
            ++num2count[e];
            buckets[num2count[e]].insert(e);
        }

        for (int c = nums.size(); c > 0; --c) { // accumulate result
            if (buckets[c].empty()) continue;
            result.insert(result.end(), buckets[c].begin(), buckets[c].end());
            if ((int)result.size() >= k) {
                result.resize(k);
                break;
            }
        }

        return result;
    }
};

int test() {
    Solution solution;

    vector<int> nums;
    vector<int> output;
    int k = 0;

    nums = {};
    output = {};
    k = 2;
    assert(solution.topKFrequent(nums, k) == output);

    nums = {1};
    output = {1};
    k = 1;
    assert(solution.topKFrequent(nums, k) == output);

    nums = {1};
    output = {1};
    k = 10;
    assert(solution.topKFrequent(nums, k) == output);

    nums  = {1, 1, 1, 2, 2, 3};
    output = {1, 2};
    k = 2;
    assert(solution.topKFrequent(nums, k) == output);

    nums  = {1, 1, 1, 2, 2, 3};
    output = {1, 2, 3};
    k = 3;
    assert(solution.topKFrequent(nums, k) == output);


    cout << "test passed" << endl;
    return 0;
}

int main(int argc, char **argv) {
    test();

    return 0;
}
