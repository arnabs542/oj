/**
 *
363. Max Sum of Rectangle No Larger Than K
Hard

Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:

Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).
Note:

The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?


Accepted
32.9K
Submissions
91.7K

SOLUTION
================================================================================

1. Brute force

Search space of a rectangle represented with 4-tuple (x1, y1, x2, y2) is O(m²n²).
Complexity: O(m²n²)

Reduce to a simpler situation
-----------------------------
How about a 1D max subarray sum no larger than k?
This is a follow up of 'max subarray sum', which can be transformed to
find RANGE SUM, then to finding PREFIX SUM. And it can be solved with finding
lower bound in a self-balancing binary search tree storing prefix sums, with
complexity: O(NlogN).

How to generalize it to a 2d version?

2. Prefix sum - 2d binary search tree lower bound
To compute sum of a rectangle range, we can compute a 2D prefix sum array ps first.
But how to find the max sum of a range no larger than k?
For arbitrary i ∈ [1, N], we need to find such minimum ps[j] that ps[i] - ps[j] <= k.
This is equivalent to find minimum ps[j] that ps[j] >= ps[i]-k.
Then it is transformed to finding a lower bound of (ps[i] - k) in binary search tree.

XXX:
But how to build a binary search tree in a rectangle while scanning 2-dimensional matrix?

Seems like we can't...
Complexity: O(MNLog(MN))

3. Prefix sum - 1d binary search tree

We can reduce it to a 1d max range sum no larger than k, by exhausting all possible
rectangle width/height in one dimension!

It takes O(N²) to exhaust all possible widths, and O(MlogM) to to find max sum
given a specific rectangle left and right side.

Complexity: O(N²MlogM)

4. Prefix sum - range sum - merge sort
This problem can be transformed to range sum smaller than k.
Then it's similar to 'count of range sum'.

A RANGE SUM PROBLEM CAN BE TRANSFORMED INTO PREFIX SUM, AND THEN TO
RANGE QUERY, BINARY SEARCH TREE OR MERGE SORT.

Merge sort process along rows is O(MlogM).

TODO: merge sort solution
Complexity: O(N²MlogM)

FOLLOW UP
================================================================================
1. Max sum of square no larger than k
1) Brute force: O(N²) squares represented with 3-tuple (x, y, h).


2. Max sum of square

 *
 *
 */

#include <debug.hpp>

class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        int result = maxSumSubmatrixPrefixSumLowerBound1D(matrix, k);

        cout << matrix << ", " << k << " => " << result << endl;

        return result;
    }

    int maxSumSubmatrixPrefixSumLowerBound1D(vector<vector<int>> &matrix, int k) {
        int result = std::numeric_limits<int>::min(); // XXX: initialization
        if (matrix.size() == 0) return 0;

        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<int>> ps(m + 1, vector<int>(n + 1, 0));

        for (int i = 1; i <= m; ++i) { // build prefix sum array
            for(int j = 1; j <= n; ++j) {
                ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + matrix[i-1][j-1];
            }
        }
        // build binary search tree along one dimension and find lower bound of prefix sum
        for (int l = 1; l <= n; ++l) { // left side of rectangle
            for (int r = l; r <= n; ++r) { // right side of rectangle
                // TODO: early stop
                if (result == k) return k;
                set<int> previousSums; // build a binary search along one dimension (row)
                previousSums.insert(0);
                for (int i = 1; i <= m; ++i) {
                    // TODO: try dynamic programming if range sum no larger than k?
                    // TODO: space optimize with rolling prefix sum array?
                    int s = ps[i][r] - ps[i][l-1];
                    auto it = std::lower_bound(previousSums.begin(), previousSums.end(), s - k);
                    if (it != previousSums.end()) {
                        result = std::max(result, s - *it);
                    }
                    previousSums.insert(s);

                }
            }
        }

        return result;
    }
};

int test() {
    vector<vector<int>> matrix;
    int k;
    int result;

    Solution solution;

    matrix = {
    };
    k = 9;
    result = 0;
    assert(solution.maxSumSubmatrix(matrix, k) == result);

    matrix = {
        {1, 0, 1},
        {0, -2, 3},
    };
    // {1, 1, 2}, {1, -1, 3}
    k = 2;
    result = 2;
    assert(solution.maxSumSubmatrix(matrix, k) == result);

    matrix = {{2, 2, -1}};
    k = 0;
    result = -1;
    assert(solution.maxSumSubmatrix(matrix, k) == result);

    matrix = {
        {5,-4,-3,4},
        {-3,-4,4,5},
        {5,1,5,-4}
    };
    // {5, 1, -2, 4}, {}
    k = 8;
    result = 8;
    assert(solution.maxSumSubmatrix(matrix, k) == result);


    cout << "self test passed!" << endl;

    return 0;
}

int main(int argc, char **argv) {

    test();
    return 0;
}
