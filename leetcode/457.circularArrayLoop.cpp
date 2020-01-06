/**
 *
457. Circular Array Loop
Medium

You are given a circular array nums of positive and negative integers. If a number k at an index is positive, then move forward k steps. Conversely, if it's negative (-k), move backward k steps. Since the array is circular, you may assume that the last element's next element is the first element, and the first element's previous element is the last element.

Determine if there is a loop (or a cycle) in nums. A cycle must start and end at the same index and the cycle's length > 1. Furthermore, movements in a cycle must all follow a single direction. In other words, a cycle must not consist of both forward and backward movements.



Example 1:

Input: [2,-1,1,2,2]
Output: true
Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's length is 3.
Example 2:

Input: [-1,2]
Output: false
Explanation: The movement from index 1 -> 1 -> 1 ... is not a cycle, because the cycle's length is 1. By definition the cycle's length must be greater than 1.
Example 3:

Input: [-2,1,-1,-2,-2]
Output: false
Explanation: The movement from index 1 -> 2 -> 1 -> ... is not a cycle, because movement from index 1 -> 2 is a forward movement, but movement from index 2 -> 1 is a backward movement. All movements in a cycle must follow a single direction.


Note:

-1000 ≤ nums[i] ≤ 1000
nums[i] ≠ 0
1 ≤ nums.length ≤ 5000


Follow up:

Could you solve it in O(n) time complexity and O(1) extra space complexity?


SOLUTION
================================================================================

For cycle detection, there are famous algorithm: tortoise and hare algorithm.

1. Trivial hash table

2. Tortoise and hare
- detect the cycle
- verify by traverse the cycle from arbitrary point, counting length and watch for
    numbers sign;

Corner cases:
- what if there are multiple cycles?
We have to exhaust all possible cycles, and rule out those invalid.
So this is a depth first search with tortoise and hare cycle detection procedure.
- nums[i] % n == 0

How to mark visited places in-place? Set to value 0 or nums[i] + n.

Complexity: O(N)

 *
 */

 #include <debug.hpp>

class Solution {
public:
    bool circularArrayLoop(vector<int>& nums) {
        bool result = circularArrayLoopDfsAndTortoiseAndHare(nums);
        cout << nums << " => " << result << endl;

        return result;
    }

    bool circularArrayLoopDfsAndTortoiseAndHare(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return false;
        for (int i = 0; i < n; ++i) {
            nums[i] %= n; // preprocess
        }
        auto step = [n, &nums](int x) -> int {
            x = (x + nums[x]) % n;
            if (x < 0) x += n;
            return x;
        };
        int l = 0;
        // dfs
        for (int i = 0; i < n; ++i) {
            l = 0;
            if (!nums[i] || std::abs(nums[i]) >= n) continue; // 0, or visited
            int p = i, q = i;
            do {
                if (nums[p] > 0) nums[p] += n; // mark visited
                else nums[p] -= n;

                p = step(p); // 3, 2,
                q = step(step(q));
            } while (nums[p] && p != q && l++ < n); // detect cycle with a meet point
            l = 1;
            if (!nums[p] || l >= n) { continue; }

            do // count cycle length
            {
                l += 1;
                q = step(q);
                if (nums[q] * nums[p] < 0) {
                    l = 0;
                    break;
                }
            } while(q != p);

            //cout << "i: " << i << ", l: " << l << endl;
            if(l >= 2) {
                //cout << "loop: nums[" << p << "]" << "=" << nums[p] << endl;
                break;
            }
            // TODO: set visited places to nums[i] + n
        }
        //cout << "l: " << l << endl;
        return l >= 2;
    }
};

int main(int argc, char *argv[])
{
    Solution solution;
    vector<int> nums;
    bool result;

    nums = {};
    result = false;
    assert(solution.circularArrayLoop(nums) == result);

    nums = {1};
    result = false;
    assert(solution.circularArrayLoop(nums) == result);

    nums = {2};
    result = false;
    assert(solution.circularArrayLoop(nums) == result);

    nums = {2,-1,1,2,2};
    result = true;
    assert(solution.circularArrayLoop(nums) == result);

    nums = {-1, 2};
    result = false;
    assert(solution.circularArrayLoop(nums) == result);

    nums = {-2,1,-1,-2,-2};
    result = false;
    assert(solution.circularArrayLoop(nums) == result);

    nums = {3,1,2}; // two loops: 0->0, 1->2->1, the second is valid
    result = true;
    assert(solution.circularArrayLoop(nums) == result);

    nums = {100};
    result = false;
    assert(solution.circularArrayLoop(nums) == result);

    nums = {-1,-2,-3,-4,-5};
    result = false;
    assert(solution.circularArrayLoop(nums) == result);

    nums = {2,2,2,2,2,4,7}; // {2,2,2,2,2,4,0};
    result = false;
    assert(solution.circularArrayLoop(nums) == result);

    return 0;
}
