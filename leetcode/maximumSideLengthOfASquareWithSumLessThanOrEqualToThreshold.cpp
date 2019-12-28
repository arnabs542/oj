/**
 *
 * 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
 Medium

 Given a m x n matrix mat and an integer threshold. Return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.



 Example 1:


Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
Example 2:

Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0
Example 3:

Input: mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
Output: 3
Example 4:

Input: mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
Output: 2


Constraints:

1 <= m, n <= 300
m == mat.length
n == mat[i].length
0 <= mat[i][j] <= 10000
0 <= threshold <= 10^5

SOLUTION
================================================================================

If there is no constraints that 0 <= mat[i][j], then the problem can be solved by
transforming it to "max sum of rectangle no larger than k", in O(NlogN) with
prefix sum binary search tree lower bound.

1. Brute force

A square is represented with 3-tuple (x, y, l), where l is the side length.
To exhaust all of them, it takes O(N³).

Complexity: O(N³)

--------------------------------------------------------------------------------
If we build a prefix sum array 2D, then the PREFIX SUM ARRAY IS MONOTONIC because
numbers in the matrix are no less than 0!

2. Binary search on length l

Complexity: O(NMlogMIN(M,N))

3. Sliding window on diagonal direction
This problem can be transformed into 1D "longest subarray with sum no larger than K"
given an array of positive numbers.
And such problem can be solved in O(N) with sliding window.

How to reduce 2D to 1D?
Traverse diagonally to expand or shrink the sliding window!

Enumerating all points in the matrix in one pass.

Complexity: O((M+N)min(M,N))=O(MN)


 *
 */

#include <debug.hpp>

class Solution {
    public:
        int maxSideLength(vector<vector<int>>& mat, int threshold) {
            int result = maxSideLengthSlidingWindow(mat, threshold);

            cout << mat << " " << threshold << " " << result << endl;

            return result;
        }

        int maxSideLengthSlidingWindow(vector<vector<int>>& mat, int threshold) {
            if (mat.size() == 0 || mat[0].size() == 0 || threshold < 0) return 0;

            int m = mat.size(), n = mat[0].size();
            // build prefix sum array
            vector<vector<int>> ps(m+1, vector<int>(n+1, 0));
            for (int i = 1; i <= m; ++i) {
                for (int j = 1; j <= n; ++j) {
                    ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + mat[i-1][j-1];
                }
            }

            int result = 0;
            int sum = 0;

            //cout << "m: " << m << " n: " << n << endl;

            // diagonal, starting from left side
            for (int i0 = 0; i0 < m; ++i0) {
                int k = 0; // side length. XXX: fatal! Initialize k in every outer loop
                for(int i = i0, j =0; i < m && j < n; ++i, ++j) {
                    ++k;
                    while((ps[i+1][j+1] + ps[i+1-k][j+1-k] - ps[i+1][j+1-k] - ps[i+1-k][j+1])
                            > threshold) {
                        --k;
                    };
                    result = std::max(k, result); // max side length ending here
                }
            }

            // diagonal, starting from top side
            for (int j0 = 0; j0 < n; ++j0) {
                int k = 0; // side length
                for (int i = 0, j = j0; i < m && j < n; ++i, ++j) {
                    ++k;
                    while((sum = ps[i+1][j+1] + ps[i+1-k][j+1-k] - ps[i+1][j+1-k] - ps[i+1-k][j+1])
                            > threshold) {
                        --k;
                    };
                    result = std::max(k, result); // max side length ending here
                }
            }

            return result;
        }


};

int test() {

    Solution solution;


    vector<vector<int>> matrix;
    int threshold;
    int answer;

    matrix = {};
    threshold = 100;
    answer = 0;
    assert(solution.maxSideLength(matrix, threshold) == answer);

    matrix = {{1}};
    threshold = 1;
    answer = 1;
    assert(solution.maxSideLength(matrix, threshold) == answer);

    matrix = {
        {1, 1},
        {1, 1},
    };
    threshold = 1;
    answer = 1;
    assert(solution.maxSideLength(matrix, threshold) == answer);

    matrix = {
        {1, 1},
        {1, 1},
    };
    threshold = 4;
    answer = 2;
    assert(solution.maxSideLength(matrix, threshold) == answer);

    matrix = {
        {1,1,3,2,4,3,2},
        {1,1,3,2,4,3,2},
        {1,1,3,2,4,3,2}
    };
    threshold = 4;
    answer = 2;
    assert(solution.maxSideLength(matrix, threshold) == answer);

    matrix = {
        {9, 1, 1},
        {9, 1, 1},
        {3, 3, 3},
        {2, 2, 2},
        {4, 4, 4},
        {3, 3, 3},
        {2, 2, 2}
    };
    threshold = 4;
    answer = 2;
    assert(solution.maxSideLength(matrix, threshold) == answer);

    matrix = {
        {2,2,2,2,2},
        {2,2,2,2,2},
        {2,2,2,2,2},
        {2,2,2,2,2},
        {2,2,2,2,2}
    };
    threshold = 1;
    answer = 0;
    assert(solution.maxSideLength(matrix, threshold) == answer);

    matrix = {
        {1,1,1,1},
        {1,0,0,0},
        {1,0,0,0},
        {1,0,0,0}
    };
    threshold = 6;
    answer = 3;
    assert(solution.maxSideLength(matrix, threshold) == answer);

    matrix = {
        {18,70},
        {61,1},
        {25,85},
        {14,40},
        {11,96},
        {97,96},
        {63,45}
    };
    threshold = 40184;
    answer = 2;
    assert(solution.maxSideLength(matrix, threshold) == answer);

    cout << "test passed!";
    return 0;
}

int main() {

    // TODO: submit

    return test();
}
