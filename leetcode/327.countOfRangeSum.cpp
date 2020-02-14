/**
 *
327. Count of Range Sum
Hard

Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.


Accepted 36,316 Submissions 107,060

SOLUTION
================================================================================
1. Brute force
Iterate all values of S(i, j) and verify.

Complexity: O(n^2)


RANGE SUM transformed to PREFIX SUM
--------------------------------------------------------------------------------
Prefix sum array can be used for range sum efficiently.
S(i, j ) = PS(j) - PS(i - 1), where PS denotes prefix sum function.

Now inspect the problem in a prefix sum array perspective.
Given the prefix sum array PS, then the objective is:
    for each i in [0, n -1], find number of such j >= i that
    sum(i, j) = PS[j] - PS[i-1] <= T,
where T is `lower - 1` or `upper`.

And WITHIN RANGE relation can be converted to SMALLER THAN relation:
Number of range sums within range[lower, upper]
  #{j| lower <= sum(i, j) <= upper} =
      #{j| sum(i, j) <= upper} - #{j| sum(i, j) < lower -1}.

Now we have a 'SMALLER THAN value and AFTER self' problem.

After transformation, mathematical objective is:
-----------------------------------------------
    for each i in range [0, n-1], we want find number of such j
that j >= i and S(i, j) in range [lower, upper].

2. Count as sum - prefix sum and range query tree for sum

"lie in [lower, upper]" involves COUNT of SMALLER THAN relation.
Building a prefix sum array doesn't just solve the problem of O(n^2),
because we still need to exhaust (i, j) pairs to verify.

Instead of exhaust and verify, can we incorporate RANGE QUERY data structure
to resolve the SMALLER THAN relation?

Build a range query tree(bit), in which prefix sum PS(i) itself is INDEX, and its
existence indicates VALUE of 1.

Then for each PS(i), we can find number of such j > i that PS(j) - P(i) <= T,
in LOGARITHM time, similar to problem 'count of smaller after self'!

Problems
-------
1) Such prefix sum array may contain negative numbers that binary index tree
can't handle negative indices.
We can add a number delta to each element of prefix sum array, so that
every element is no less than 0. And it doesn't change value of sum(i,j).
2) Prefix sum may overflow
3) Prefix sum may be very large, slowing down the algorithm.
For this problem, we can MAP SUM VALUES INTO CONTINUOUS INTEGER SPACE, so that
the prefix sum index have O(n) space.

Procedure
----------
Compute prefix sum array ps[0,...,n].
Mapping prefix sum values into finite space O(N).
For i = n, ..., 1 # length
    range query tree update (prefixSums[i])
    nUpper = range query tree query (prefixsums[i-1] + upper)
    nLower = range query tree query (prefixsums[i-1] + lower - 1)
    number of eligible ranges += (nUpper - nLower)
Return number of eligible ranges.


Complexity
O(NlogN), O(N)

3. Divide and conquer - prefix sum for range sum query - merge sort

Merge sort is stable sort.
Merge sort can be used for finding numbers SMALLER THAN AFTER self.

If we divide the array into two even subarray A and B, there are
four possible cases for range interval [i, j]:
- i, j both in A: solved in recursive subproblem
- i, j both in B: solved in recursive subproblem
- i in A, j in B: solved in the merge process
- i in B, j in A (not valid since i must no larger than j)

In the merge process, we want to find such [i, j] that
lower <= ps(j) - ps(i-1) <= upper.

And since both subarrays are already sorted, we can use the transitivity
property of inequality relation. In another word, counting process
is linear complexity since we don't need to move pointers backward!

In each stage of merging, count the ranges first then do real merge.

Procedure
- Partition prefix sum array into two even parts A and B
- merge sort two subarrays, and accumulate number of eligible ranges
- Count of number of pairs (i, j) of range sum within bound, where
i in A and j in B.
- Do real merge

Complexity
T(n) = 2T(n-1)+n
O(NlogN), O(N)

4. Divide and conquer - prefix sum - binary search tree lower bound/upper bound

Computing distance between two iterators in a binary search tree can be O(N).
Complexity: O(NlogN), worst O(N²)


 */
#include <debug.hpp>

#include "tree.hpp"

// binary indexed tree implementation: tree.hpp

class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int result = 0;
        result = countRangeSumPrefixSumAndMergeSort(nums, lower, upper);
        //result = countRangeSumPrefixSumRangeQuery(nums, lower, upper);
        cout << nums << " [" << lower << ", " << upper << "]"
            << "=> " << result << endl;
        return result;
    }

    /**
     * Divide and conquer in a merge sort way
     * Input: prefix sum array.
     */
    int divideAndConquer(vector<long> &ps, int low, int high, int lower, int upper) {
        int nRanges = 0;
        //if (low == high) return lower <= ps[low] & ps[low] <= upper; // XXX: corner case
        if (low == high) return 0;

        // divide and conquer
        int m = (low + high) >> 1;
        nRanges += divideAndConquer(ps, low, m, lower, upper); // m-low+1
        nRanges += divideAndConquer(ps, m + 1, high, lower, upper); // high-m
        // COMBINE: COUNT
        {
            int p = low, s = m + 1, t = m + 1; // [p, s] lower bound, [p, t] upper bound
            while (p <= m) {
                while (s <= high && ps[s] -  ps[p] < lower) ++s; // for j >= s, range sum >= lower
                t = s;
                while (t <= high && ps[t] - ps[p] <= upper) ++t; // for j >= t, range sum > upper
                nRanges += t - s; // #ranges = (t-s)

                ++p;
            }
        }

        // COMBINE: SORT
        //cout << vector<int>(ps.begin() + low, ps.begin() + high+1) << " in " << ps << " count: " << nRanges << endl;
        //vector<int> arr1(ps.begin() + low, ps.begin() + high + 1); // XXX: implicit cast overflow/underflow
        vector<long> arr1(ps.begin() + low, ps.begin() + high + 1);
        //cout << "merge: " << arr1 << endl;
        int p = 0, q = m+1-low; // [0, m-low], [m+1-low, high-low]
        int k = low; // [low, high]. XXX: initialization, not 0!
        while (p <= m - low && q <= high - low) {
            if (arr1[p] <= arr1[q]) { ps[k++] = arr1[p++]; }
            else { ps[k++] = arr1[q++]; }
        }
        while (p <= m - low) { ps[k++] = arr1[p++]; }
        while (q <= high - low) { ps[k++] = arr1[q++]; }
        //cout << "merge: " << arr1 << endl;

        return nRanges;
    }

    int countRangeSumPrefixSumAndMergeSort(vector<int>& nums, int lower, int upper) {
        vector<long> ps(nums.size() + 1, 0); // prefix sum array
        for (size_t i = 1; i <= nums.size(); ++i) {
            ps[i] = ps[i-1] + nums[i - 1];
        }

        //int result = 0;
        //vector<int> indices(nums.size());
        //for (int i = 0; i < (int)nums.size(); ++i) indices[i] = i;

        // TODO:
        int n = nums.size();
        int result =  divideAndConquer(ps, 0, n, lower, upper); // merge sort

        return result;

    }

    int countRangeSumPrefixSumRangeQuery(vector<int> &nums, int lower, int upper) {
        // build prefix sum
        vector<long> prefixSums(nums.size() + 1, 0); // length indexed prefix sum array
        for (uint i = 1; i <= nums.size(); ++i) {
            prefixSums[i] = prefixSums[i-1] + nums[i-1];
        }

        // buckets mapping values to finite continuous space [1, 3N].
        map<long, int> buckets; // ordered values, beware of overflow
        for (long ps: prefixSums) {
            buckets[ps] = 1;
            buckets[ps+upper] = 1;
            buckets[ps+lower-1] = 1;
        }
        int i = 1; // XXX: binary indexed tree is one-based
        for (auto it = buckets.begin(); it != buckets.end(); ++it) {
            it->second = i++;
        }

        // count as sum, range query sum
        int nRanges = 0;
        BitTree rsq(buckets.size()); // range sum query, [1, n]
        for (i = nums.size(); i >= 1;--i) {
            rsq.update(buckets.at(prefixSums[i]), 1);
            int nUpper = rsq.query(buckets.at(upper + prefixSums[i-1])); // query for number of such j that ps[j] - ps[i-1] <= upper
            int nLower = rsq.query(buckets.at(lower + prefixSums[i-1] - 1)); // query for number of such j that ps[j] - ps[i-1] < lower
            nRanges += nUpper - nLower; // number of such j that ps[j]
        }
        return nRanges;
    }


};

int main(int argc, char *argv[])
{
    Solution solution;

    vector<int> nums;
    int lower, upper;
    int result;

    nums = {};
    lower = 0; upper = 0;
    result = 0;
    assert(solution.countRangeSum(nums, lower, upper) == result);

    nums = {0};
    lower = 0; upper = 0;
    result = 1;
    assert(solution.countRangeSum(nums, lower, upper) == result);

    nums = {1};
    lower = 0; upper = 1;
    result = 1;
    assert(solution.countRangeSum(nums, lower, upper) == result);

    nums = {1, -1, 1};
    lower = -1; upper = 1;
    result = 6;
    assert(solution.countRangeSum(nums, lower, upper) == result);

    nums = {-2, 5};
    lower = -2; upper = 2;
    result = 1;
    assert(solution.countRangeSum(nums, lower, upper) == result);

    nums = {1};
    lower = -2; upper = 2;
    result = 1;
    assert(solution.countRangeSum(nums, lower, upper) == result);

    nums = {-2, 5, -1}; // {0, -2, 3, 2}; {-2, 0}, {2, 3}
    lower = -2; upper = 2;
    result = 3;
    assert(solution.countRangeSum(nums, lower, upper) == result);

    nums = {-2147483647,0,-2147483647,2147483647}; // case: overflow.
    // {0, -2147483647, -2147483647, -4294967294, -2147483647, }
    lower = -564, upper = 3864;
    result = 3;
    assert(solution.countRangeSum(nums, lower, upper) == result);

    // TODO: submit

    return 0;
}
