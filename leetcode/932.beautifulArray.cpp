/**
 *
 *
932. Beautiful Array
Medium

For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:

For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].

Given N, return any beautiful array A.  (It is guaranteed that one exists.)



Example 1:

Input: 4
Output: [2,1,4,3]
Example 2:

Input: 5
Output: [3,1,2,5,4]


Note:

1 <= N <= 1000

Accepted
7.6K
Submissions
13.8K

SOLUTION
================================================================================

1. Brute force dfs

Complexity is exponential..

Sort? Partition? Even and Odd? Construct?

2. Divide and conquer - recurrence relation - partition by even and odd numbers

If a[i]+a[j] = 2a[k], then a[i] + a[j] must be even number.
Can we partition even and odd numbers?
Then there are four kind of combinations of i and j:
1) both odd
2) nums[i] is odd and nums[j] is even number
3) both even

Case 2) will not break condition (a[i]+a[j] != 2*a[k]).
Then we need to ensure odd parts and even parts will not break condition.

And even parts can be reduced to problem of N/2 by dividing them by 2.
How about odd parts?
Odd parts can be converted to even numbers by subtracting every number by 1!
And even numbers can be reduced to f(N/2)..
Note that (a[i]-1) + (a[j]-1]) = 2*(a[k]-1) <=> a[i] + a[j] = 2*a[k], equivalent!

Yes, the equality condition is linear transform invariant!

T(N) = 2T(N/2)+N
Complexity: O(NlogN)

3. Divide and conquer - optimized
We can reduce one recursive call, and the idea is similar to memoization!
T(N) = T(N/2) + N

Complexity: O(N)

4. Divide and conquer to iterative generation

Based on above optimization, the recursive call can be converted to iterative.

TODO:

Complexity: O(N)

4:  [2,1,4,3]
5:  [3,1,2,5,4], [1,5,3,2,4]
6:  [1,5,3,2,6,4]
7:  [1,5,3,7,2,6,4]
8:  [1,5,3,7,2,6,4,8]
9:  [1,9,5,3,7,2,6,4,8]
10: [1,9,5,3,7,2,10,6,4,8]
20: [1,17,9,5,13,3,19,11,7,15,2,18,10,6,14,4,20,12,8,16]


6: 1,2,3,4,5,6 => 1,3,5 2,4,6 => 1,2,3, 1,2,3

//              2x[1,5, 3,2,4] => [1,3,5], 4x[1,2]
//
//    [1,3,5] => [1,5,3]
//    [1,3,5,7] => [1,5,3,7]
//    [0,2,4,6]
//    [1,3,5,7,9]
//

 *
 */

#include <debug.hpp>

class Solution {
public:
    vector<int> beautifulArray(int N) {
        vector<int> result = beautifulArrayDivideAndConquer(N);

        cout << N << " " << result<< endl;
        return result;
    }

    void dfs(vector<int> &arr, int startIdx, int n) {

        if (n == 1) {
            arr[startIdx] = 1;
            return;
        }
        int nOdds = (n+1)/2;
        int nEvens = (n)/2;

        dfs(arr, startIdx + 0, nOdds); // 1, 3 -> 2, 4 -> 1, 2
        dfs(arr, startIdx + nOdds, nEvens); // 2, 4 -> 1, 2
        // XXX: duplicate calculation can be optimized
        for (int i = startIdx; i < startIdx + nOdds; ++i) {
            arr[i] = 2 * arr[i] - 1;
        }
        for (int i = startIdx + nOdds; i < startIdx + n; ++i) arr[i] *= 2;
    }

    void dfsOneFewRecursion(vector<int> &arr, int startIdx, int n) {

        if (n == 1) {
            arr[startIdx] = 1;
            return;
        }
        int nOdds = (n+1)/2;
        //int nEvens = (n)/2;

        dfsOneFewRecursion(arr, startIdx + 0, nOdds); // 1, 3 -> 2, 4 -> 1, 2
        //dfs(arr, startIdx + nOdds, nEvens); // 2, 4 -> 1, 2
        for (int i = startIdx; i < startIdx + nOdds; ++i) {
            arr[i] = 2 * arr[i] - 1;
        }
        int j = startIdx + nOdds;
        for (int i = startIdx; i < startIdx + nOdds && j < startIdx + n; ++i) {
            if (arr[i] + 1 <= n) {
                arr[j++] = arr[i] + 1;
            }
        }

    }

    vector<int> beautifulArrayDivideAndConquer(int N) {
        vector<int> result(N, 0);

        //dfs(result, 0, N);
        dfsOneFewRecursion(result, 0, N);

        return result;
    }

    vector<int> beautifulArrayIterative(int N) {
        // TODO: dynamic programming. F(N) => F(N/2)
        // f(n) = {2x-1 for x in f(n/2), 2x for x in f(n/2)}
    }

};

int test() {
    Solution solution;
    int N;
    vector<int> result ;

    N = 1;
    result = {1};
    assert(solution.beautifulArray(N) == result);

    N = 2;
    result = {1,2};
    assert(solution.beautifulArray(N) == result);

    N = 3;
    result = {1,3,2};
    assert(solution.beautifulArray(N) == result);

    N = 4;
    result = {1,3,2,4};
    assert(solution.beautifulArray(N) == result);

    N = 5;
    result = {1, 5, 3, 2, 4, };
    assert(solution.beautifulArray(N) == result);

    N = 6;
    result = {1, 5, 3, 2, 6, 4, };
    assert(solution.beautifulArray(N) == result);

    N = 7;
    result = {1, 5, 3, 7, 2, 6, 4, };
    assert(solution.beautifulArray(N) == result);

    N = 8;
    result = {1, 5, 3, 7, 2, 6, 4, 8, };
    assert(solution.beautifulArray(N) == result);
    N = 9;
    result = {1, 9, 5, 3, 7, 2, 6, 4, 8, };
    assert(solution.beautifulArray(N) == result);

    N = 10;
    result = {1, 9, 5, 3, 7, 2, 10, 6, 4, 8, };
    assert(solution.beautifulArray(N) == result);

    N = 20;
    result = {1, 17, 9, 5, 13, 3, 19, 11, 7, 15, 2, 18, 10, 6, 14, 4, 20, 12, 8, 16, };
    assert(solution.beautifulArray(N) == result);

    cout << "test passed" << endl;

    return 0;
}

int main(int argc, char *argv[])
{
    test();
    return 0;
}
