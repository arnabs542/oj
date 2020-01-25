/**
 *
 *
710. Random Pick with Blacklist
Hard

Given a blacklist B containing unique integers from [0, N), write a function to return a uniform random integer from [0, N) which is NOT in B.

Optimize it such that it minimizes the call to system’s Math.random().

Note:

1 <= N <= 1000000000
0 <= B.length < min(100000, N)
[0, N) does NOT include N. See interval notation.
Example 1:

Input:
["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
Output: [null,0,0,0]
Example 2:

Input:
["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
Output: [null,1,1,1]
Example 3:

Input:
["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
Output: [null,0,0,2]
Example 4:

Input:
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
Output: [null,1,3,1]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, N and the blacklist B. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.

Accepted
10K
Submissions
30.7K

================================================================================
SOLUTION

1. Brute force - resample
The brute force way is to re-sample if blacklist is hit, giving high time complexity.

Complexity: TODO

2. Mapping from continuous space - transform to continuous range
Maintain a mapping from [0, N-b) to [0, N), and sample in space of [0, N-b).
Build a prefix sum array along with its corresponding index array, which are
not blacklisted.

But the indices array will exceed the memory limit.

Complexity: O(logN)

3. Build weight prefix sum array with zero weights for blacklisted numbers.
The idea is to sample in range of prefix sum array [1, max sum].
But how to find the corresponding number that's not blacklisted?

Objective:
    find such i that ps[i-k] <= target < ps[i], where target is sampled value.

Time and memory limit exceeded.

Complexity: O(logN)

4. Build weight prefix sum with zero weights, represented by blacklist
To save space, we can store information in sparse representation.

Prefix sum: 1,2,3,...,k1,k1,k1,...,k2,k2,...,N-B. Size is N
Sample v in [0, N-B-1], find its upper bound.

Maintain a weight prefix sum of blacklist size.
Still, sample target in range [1, N-B], find upper bound i in the prefix sum array.
Then the real index is (target-1 + i).

Complexity: O(b)

================================================================================
What if we have dynamic black list?
For range query sum, we can build binary indexed tree to update range sum.
And to search for upper bound, it takes O(log²n)

Complexity: O(log²N)

 *
 */

#include <debug.hpp>
#include <random>

class Solution {
public:
    Solution(int N, vector<int>& blacklist) {
    }

    int pick() {

    }
};

class SolutionMapping {
public:
    SolutionMapping(int N, vector<int>& blacklist) {
        sort(blacklist.begin(), blacklist.end());
        int ib = 0;
        for (int i = 0; i < N; ++i) {
            if (ib < (int)blacklist.size() && blacklist[ib] == i) {
                ++ib;
                continue;
            }
            indices.push_back(i);
            // ps.push_back((ps.empty() ? 0:ps.back()) + 1); // weight 1
        }
    }

    int pick() {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> dis(0, ps.back()-1); // [1, max sum].
        int v = dis(gen);
        auto itr = upper_bound(ps.begin(), ps.end(), v); // XXX: weights are all 1, no need to binary search
        int idx = itr - ps.begin();
        return indices[idx];
    }

    int pickFaster() {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> dis(0, indices.size() - 1); // [1, max sum].
        int v = dis(gen);
        // auto itr = upper_bound(ps.begin(), ps.end(), v);
        // int idx = itr - ps.begin();
        return indices[v]; // XXX: indices memory limit exceeded
    }

    vector<int> ps; // prefix sum
    vector<int> indices; // valid indices, [0, N-1]
};

class SolutionWeightPrefixuSumBinarySearchOnBlacklist {
public:
    SolutionWeightPrefixuSumBinarySearchOnBlacklist(int N, vector<int>& blacklist) {
        sort(blacklist.begin(), blacklist.end()); // 0, N-1
        for (int i = 0; i < (int) blacklist.size(); ++i) {
            ps.push_back(blacklist[i]+1 - (i+1)); // -1, N
        }
        n = N;

        // uniform distributed random number generator
        std::random_device rd;
        gen = std::mt19937(rd());
        dis = std::uniform_int_distribution<>(0, n-ps.size()-1); // target range: [0, N-B)

    }

    int pick() {
        int v = dis(gen); // sample in [0, n - 1]
        int offset = upper_bound(ps.begin(), ps.end(), v)-ps.begin(); // v == ps[i]?

        return v + offset; // offset: number of blacklist numbers less than v
    }

    vector<int> ps; // prefix sum, [0, N-B-1]
    int n;

    std::mt19937 gen;
    std::uniform_int_distribution<> dis;
};


/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(N, blacklist);
 * int param_1 = obj->pick();
 */

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(N, blacklist);
 * int param_1 = obj->pick();
 */


int test() {
    return 0;
}

int main(int argc, char **argv) {
    test();
    return 0;
}

