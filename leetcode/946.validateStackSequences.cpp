/**
 *
946. Validate Stack Sequences
Medium

Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.



Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.


Note:

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.

Accepted
24,176
Submissions
41,161

================================================================================

First understand the process.
Why is [4,3,5,1,2] is wrong?
We can simulate the process.
Because if 4 is popped out first, then stack

1. Stack simulation - scan the popped and determine whether to push or pop
Scan the popped sequence, and for each popped number, we have enough information
to maintain the stack data structure.
1) If the current popped out number is not from stack top, then it must be this process:
    keep PUSHING into the stack until the current popped is found. And the current
number is popped out immediately after pushed into the stack.
2) If the current popped out number is the stack top, just POP out the stack top.

Complexity: O(N), O(N)

2. Stack simulation - scan the pushed and determine whether to push or pop

For each element to push, we push it into the stack, and check the popped
sequence to see whether it should be popped out or not.

Complexity: O(N), O(N)

 *
 */
#include <debug.hpp>

class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        bool result;
        //result = validateStackSequencesStackScanPopped(pushed, popped);
        result = validateStackSequencesStackScanPushed(pushed, popped);

        cout << pushed << " " << popped << " => " << result << endl;
        return result;
    }

    bool validateStackSequencesStackScanPopped(vector<int>& pushed, vector<int>& popped) {
        stack<int> filo; // first in last out
        uint n = pushed.size();
        uint p = 0, q = 0; // pointer to pushed, poped

        // for each popped, push elements before it and pop it out
        while (q < n) {
            // cout << p << " " << q << " " << n << endl;
            if (!filo.empty() && filo.top() == popped[q]) {
                filo.pop(); // the popped is stack top
            } else { // pushing until the current popped
                while (p < n && pushed[p] != popped[q]) filo.push(pushed[p++]);
                if (p == n) return false; // the popped is not found
                // cout << "pushing until" << p << " " << pushed[p] << endl;
                ++p;
            }
            ++q; // pop stack top
        }

        return true;
    }

    bool validateStackSequencesStackScanPushed(vector<int>& pushed, vector<int>& popped) {
        stack<int> filo;
        uint n = pushed.size();
        uint p = 0, q = 0;
        for (p = 0; p < n; ++p) {
            filo.push(pushed[p]); // push
            while (q < n  && !filo.empty() && filo.top() == popped[q]) { // should pop now
                filo.pop();
                ++q;
            }
        }
        return filo.empty(); // should have popped out all
        //while (q < n) {
            //if (filo.empty() || filo.top() != popped[q]) {
                //return false;
            //}
            //filo.pop();
            //++q;
        //}
        //return true;
    }
};

int test() {
    Solution solution;

    vector<int> pushed, popped;
    bool output;

    pushed = {1,2,3,4,5};
    popped = {4,5,3,2,1};
    output = true;
    assert(solution.validateStackSequences(pushed, popped) == output);

    pushed = {4,5,3,2,1};
    popped = {4,5,3,2,1};
    output = true;
    assert(solution.validateStackSequences(pushed, popped) == output);

    pushed = {1,2,3};
    popped = {3,2,1};
    output = true;
    assert(solution.validateStackSequences(pushed, popped) == output);

    pushed = {1,2,3};
    popped = {3,1,2};
    output = false;
    assert(solution.validateStackSequences(pushed, popped) == output);

    pushed = {1,2,3};
    popped = {1,2,3};
    output = true;
    assert(solution.validateStackSequences(pushed, popped) == output);

    pushed = {};
    popped = {};
    output = true;
    assert(solution.validateStackSequences(pushed, popped) == output);

    pushed = {1};
    popped = {1};
    output = true;
    assert(solution.validateStackSequences(pushed, popped) == output);

    pushed = {1,2,3,4,5};
    popped = {4,3,5,1,2};
    output = false;
    assert(solution.validateStackSequences(pushed, popped) == output);

    cout << "test passed!" << endl;
    return 0;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
