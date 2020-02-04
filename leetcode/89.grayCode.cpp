/**
 *
89. Gray Code
Medium

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2ⁿ, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].

================================================================================
SOLUTION

1. Hamilton path - backtracking with pruning to reduce search space
Treat it as a graph, and the objective is to find a Hamilton path.

Complexity: O(n2ⁿ). NP hard problem

2. Generating
For n-th number, g(n) = n ^ (n >> 1), where n is in [0, 2^N].

Complexity: O(N)

What if we don't know the gray code generating algorithm?

3. Dynamic programming - recurrence relation f(n) = r(f(n-1))
Generate f(n) from f(n-1).

When n = 2, the sequence is:
00 -> 01 -> 11 -> 10
When n = 3, the sequence is:
000 -> 001 -> 011 -> 010 -> 110 -> 111 -> 101 -> 100
 00 ->  01 ->  11 ->  10 ->  10 ->  11 ->  01 ->  00
This is like palindrome sequence, showing symmetric property.

f(n-1):  f(n-1)[0], f(n-1)[1], ..., f(n-1)[2ⁿ-1]
f(n):  f(n-1)=f(n-1)[0], f(n-1)[1], ..., f(n-1)[2ⁿ-1], reverse f(n-1) and set bit 1 at
n-th bit from right.

Complexity: O(2ⁿ)

4. Hamilton path brute force optimized by following patterns

n = 2:
    00  -  01
     |     |
    10  -  11
Counter clockwise

n = 3:
    000 - 001
     |     |
    010 - 011
     |     |
    110 - 111
     |     |
    100 - 101

Keep track of visited, and try to flip rightmost bits.



 *
 */
#include <debug.hpp>

class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> result;

        //result = grayCodeGenerate(n);
        result = grayCodeDp(n);

        cout << n << " => " << result << endl;

        return result;
    }

    vector<int> grayCodeGenerate(int n) {
        vector<int> result(1<<n);
        for (int i = 0; i < (1<<n); ++i) {
            result[i] = (i ^ (i >> 1));
        }
        return result;
    }

    vector<int> grayCodeDp(int n) {
        vector<int> f{0};
        f.reserve(1 << n);
        for (int i  = 1; i <= n; ++i) {
            int m = f.size();
            for (int j = m-1; j >= 0; --j) {
                f.push_back(f[j] | (1 << (i-1)));
            }
        }

        return f;
    }
};

int test() {
    Solution solution;
    int n;
    vector<int> output;

    n = 0;
    output = {0};
    assert(solution.grayCode(n) == output);

    n = 2;
    output = {0,1,3,2};
    assert(solution.grayCode(n) == output);

    n = 4;
    output = {0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8};
    assert(solution.grayCode(n) == output);

    cout << "passed" << endl;
    return 0;
}

int main() {
    test();
    return 0;
}
