/**
 *
 *
835. Image Overlap
Medium

Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
Notes:

1 <= A.length = A[0].length = B.length = B[0].length <= 30
0 <= A[i][j], B[i][j] <= 1
Accepted
15.1K
Submissions
27.3K

================================================================================
SOLUTION

The process is like convolution.
How to compute the maximum convolution?

1. Brute force convolution

How to design the algorithm
1) Analyze a SPECIFIC CASE of translating
2) Quantify the situation: translating vector id (dx, dy)
3) Generalize to the GENERAL CASE formula
4) Determine the bounds of (dx, dy)

The key is to implement the sliding algorithm.
Think in a way of initialization, maintenance, termination.
For each coordinate (x, y) in matrix A, we need to compute associated
convolution A[x][y] * B[x+dx][y+dy], where (dx, dy) is the shift vector.

Then iterate combinations of (dx, dy), and compute maximum convolution.

Complexity: O(n⁴)

2. Brute force convolution with pruning
Coordinates can't go out of bound of matrices. We can use that for  pruning.

0 <= x <= n-1
0 <= y <= n-1
0 <= x + dx <= n-1
0 <= y + dy <= n-1
So,
0 <= x <= min(n-1, n-1-dx)
0 <= y <= min(n-1, n-1-dy)

3. Fast Fourier Transform

TODO:
Complexity: O(N³logN)

4. Bit representation

5. Sparse matrix convolution with sparse representation

TODO:
https://leetcode.com/problems/image-overlap/discuss/130623/C%2B%2BJavaPython-Straight-Forward

The problem with brute force convolution method is high complexity for sparse matrices.
For sparse matrix, we can reduce complexity by storing only non-zero values.
The objective is to find max convolution in Cartesian product space (dx, dy).

To exhaust (dx, dy), we can generate the Cartesian product with two loops.
But since matrices are sparse, we can generate sparse Cartesian product:
 (dx, dy) is the vector difference of coordinates in A and B.

To optimize even more, we can hash the matrix coordinates to speed up sparse representation access.

Complexity: O(pq), worst O(n⁴), where p, q are number of non-zero values in A, B.


 *
 */

#include <debug.hpp>

class Solution {
public:
    int largestOverlap(vector<vector<int>>& A, vector<vector<int>>& B) {
        int result;
        //result = largestOverlapBruteForce(A, B);
        //result = largestOverlapSparseConvolution(A, B);
        result = largestOverlapSparseConvolution2(A, B);

        cout << A << " " << B << " => " << result <<endl;

        return result;
    }

    int largestOverlapBruteForce(vector<vector<int>>& A, vector<vector<int>>& B) {
        //int result = std::numeric_limits<int>::min();
        int result = 0;
        int n = A.size();
        if (!n) return 0;
        for (int dx = 1-n; dx < n; ++dx) {
            for (int dy = 1-n; dy < n; ++dy) { // A[i][j] * B[i+dx][j+dy];
                int conv = 0; // 0
                //for (int i = 0; i < n; ++i) { // TODO: can we do better
                    //for (int j = 0; j < n; ++j) {
                for (int i = 0; i < min(n, n-dx); ++i) { // optimization by pruning
                    for (int j = 0; j < min(n, n-dy); ++j) {
                        int ib = i + dx, jb = j + dy; // 0 <= ib < n => -dx <= i < n-dx
                        if (ib >= 0 &&  ib<n && jb >= 0 && jb < n) {
                            conv += A[i][j]*B[ib][jb];
                        }
                    }
                }
                result = std::max(result, conv);
            }
        }

        return result;
    }

    int largestOverlapSparseConvolution(vector<vector<int>> &A, vector<vector<int>> &B) {
        // init
        int n = (int)A.size();
        vector<pair<int, int>> sa, sb; // sparse matrix representation of A, B
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (A[i][j]) sa.push_back({i, j});
                if (B[i][j]) sb.push_back({i, j}); // XXX: can use hashing
            }
        }
        // maintenance
        map<pair<int, int>, int> shiftToConv; // shift vector to convolution.
        for (auto ij0: sa) {
            for (auto ij1: sb) {
                int dx, dy;
                std::tie(dx, dy) = make_tuple(ij0.first - ij1.first, ij0.second-ij1.second);
                //dx = ij0.first - ij1.first;
                //dy = ij0.second- ij1.second;
                ++shiftToConv[{dx, dy}]; // compute convolution given (dx, dy).
            }
        }
        // termination
        int result = 0;
        for (auto ijc: shiftToConv) {
            result = std::max(result, ijc.second);
        }
        return result;
    }

    int largestOverlapSparseConvolution2(vector<vector<int>> &A, vector<vector<int>> &B) {
        int n = (int)A.size();
        vector<int> sa, sb; // sparse matrix representation of A, B
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (A[i][j]) sa.push_back(100*i+j); // hashing of coordinate (i, j)
                if (B[i][j]) sb.push_back(100*i+j);
            }
        }
        // maintenance
        unordered_map<int, int> shiftToConv; // shift vector to convolution
        for (auto ij0: sa) {
            for (auto ij1: sb) {
                ++shiftToConv[ij0-ij1]; // compute convolution given (dx, dy).
            }
        }
        int result = 0;        // termination
        for (auto ijc: shiftToConv) {
            result = std::max(result, ijc.second);
        }
        return result;
    }
};

int test() {
    Solution solution;

    vector<vector<int>> A, B;
    int output;

    A = {}, B = {};
    output = 0;
    assert(solution.largestOverlap(A, B) == output);

    A = {{1}}, B = {{1}};
    output = 1;
    assert(solution.largestOverlap(A, B) == output);

    A = {
        {1,1,0},
        {0,1,0},
        {0,1,0}
    };
    B = {
        {0,0,0},
        {0,1,1},
        {0,0,1}
    };
    output = 3;
    assert(solution.largestOverlap(A, B) == output);

    cout << "test passed"<<endl;
    return 0;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
