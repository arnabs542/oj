/**
 *
54. Spiral Matrix
Medium

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Accepted
304.8K
Submissions
939.2K

Hints

Well for some problems, the best way really is to come up with some algorithms for simulation. Basically, you need to simulate what the problem asks us to do.
We go boundary by boundary and move inwards. That is the essential operation. First row, last column, last row, first column and then we move inwards by 1 and then repeat. That's all, that is all the simulation that we need.
Think about when you want to switch the progress on one of the indexes. If you progress on
i
out of
[i, j]
, you'd be shifting in the same column. Similarly, by changing values for
j
, you'd be shifting in the same row. Also, keep track of the end of a boundary so that you can move inwards and then keep repeating. It's always best to run the simulation on edge cases like a single column or a single row to see if anything breaks or not.



================================================================================
SOLUTION

1. Rule based

1) Write out four directions directly
2) Use  directions vectors.

But this is more error-prone, especially when it comes to the termination state!

Complexity: O(N)

2. State machine based
Complexity: O(N), O(N) or O(1)



 *
 */
#include <debug.hpp>

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> result;
        result = spiralOrderRule(matrix);

        cout << matrix << " => " << result << endl;

        return result;
    }

    vector<int> spiralOrderRule(vector<vector<int>> &matrix) {
        vector<int> result;

        uint m = matrix.size();
        if (!m) return result;
        uint n = matrix[0].size();

        int s1 = n, s2 = m - 1, s3 = n - 1, s4 = m - 2; // XXX: careful not to use uint.
        s2 = s1 > 0 ? s2:0;
        s3 = s2 > 0 ? s3:0;
        s4 = s3 > 0 ? s4:0;
        int i = 0, j = -1;
        // XXX: termination state. Counting, or go right (then down)
        while (result.size() < m*n) {
            for (int k = 0; k < s1; ++k) { // right
                //cout << i << " 1 " << j << endl;
                result.push_back(matrix[i][++j]);
            }
            //if (s1 == 0) break;
            for (int k = 0; k < s2; ++k) { // down
                //cout << i << " 2 " << j << endl;
                result.push_back(matrix[++i][j]);
            }
            //if (s2 == 0) break;
            for (int k = 0; k < s3; ++k) { // left
                //cout << i << " 3 " << j << endl;
                result.push_back(matrix[i][--j]);
            }
            //if (s3 == 0) break;
            for (int k = 0; k < s4; ++k) { // up
                //cout << i << " 4 " << j << endl;
                result.push_back(matrix[--i][j]);
            }
            //++i; ++j;
            s1 -= 2; s2 -= 2; s3 -= 2; s4 -= 2; // beware unsigned int underflow!
            s2 = s1 > 0 ? s2:0;
            s3 = s2 > 0 ? s3:0;
            s4 = s3 > 0 ? s4:0;
            //cout << result << endl;
            cout << "steps: " <<  s1 << " " << s2 << "  " << s3 << " " << s4 << endl;
        }

        return result;
    }
};

int test() {
    Solution solution;

    vector<vector<int>> input;
    vector<int> output;

    input = {
        { 1, 2, 3 },
        { 4, 5, 6 },
        { 7, 8, 9 },
    };
    output = {1,2,3,6,9,8,7,4,5};
    assert(solution.spiralOrder(input) == output);

    input = { };
    output = {};
    assert(solution.spiralOrder(input) == output);

    input = {{1}};
    output = {1};
    assert(solution.spiralOrder(input) == output);

    input = {{1}, {2}, {3}};
    output = {1, 2, 3};
    assert(solution.spiralOrder(input) == output);

    input = {
        {1,2,3,4},
        {5,6,7,8},
        {9,10,11,12}
    };
    output = {1,2,3,4,8,12,11,10,9,5,6,7};
    assert(solution.spiralOrder(input) == output);

    cout << "test passed!" << endl;
    return 0;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
