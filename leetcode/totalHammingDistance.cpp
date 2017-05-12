/*
477. Total Hamming Distance

Total Accepted: 7479
Total Submissions: 16326
Difficulty: Medium
Contributors: kevin.xinzhao@gmail.com

The Hamming distance between two integers is the number of positions at which the
corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
    HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

Note:
Elements of the given array are in the range of 0 to 10^9
Length of the array will not exceed 10^4.

==============================================================================================
SOLUTION

1. Brute-force. Compute pairwise distance metrics for O(N²) pairs, time complexity is O(N²).

2.

Denote the distance metric function as f(x, y). Then analyze:

4  = 0100
14 = 1110
2  = 0010

f(4, 14) = 2, f(4, 2) = 2, f(14, 2) = 2
And we have (a ^ b) ^ (a ^ c) = b ^ c

4  = 0100
10 = 1010
5  = 0101
f(4, 10) = 3, f(4, 5) = 1, f(10, 5) = 4, Total = 3 + 1 + 4 = 8

The above calculation is performed in a perspective of pairs.

If we exploit the array in a bit-wise way, we can come up with that, for a specific bit,
the total hamming distance is #(numbers with this bit of 1) * #(numbers with this bit of 0).

In this bit-wise approach, we can do this in O(N * #(integer bits)) = O(N).
*/

#include <iostream>
#include <vector>
#include <assert.h>
#include <memory>

using namespace std;

class Solution {
public:
    int totalHammingDistance(vector<int>& nums)
    {
        int count = this->totalHammingDistanceBitwise(nums);
        cout << "distance: " << count << endl;
        return count;
    }

    int totalHammingDistanceBitwise(vector<int> &nums)
    {
        cout << nums.size() << " numbers: " << nums[0] << ", " << nums[1] << ", " << nums[2] << endl;
        int count = 0, mask = 0x1;
        for (int i = 0; i < 30; i++){
            int c0 = 0, c1 = 0; // count of zeros and ones on this bit
            for (int j = 0; j < (int)nums.size(); j++) {
                c1 += (nums[j] & mask) >> i;
            }
            c0 = nums.size() - c1;
            //cout << "zeros: "<< c0 << ", ones: "<< c1 << endl;
            count += c0 * c1;
            mask <<= 1;
        }
        return count;
    }
};

void test()
{

    Solution solution;
    vector<int> nums;
    shared_ptr<int> arr_ptr;
    int *arr;

    arr_ptr = shared_ptr<int>(new int[3]{1, 2, 3}, [](int*p){delete[] p;});

    arr = new int[3]{4, 14, 2};
    arr_ptr = shared_ptr<int>(arr);
    nums = vector<int>(arr, arr + 3);
    assert (solution.totalHammingDistance(nums) == 6);
    //nums.clear();

    arr = new int[3]{4, 10, 5};
    arr_ptr = shared_ptr<int>(arr);
    nums = vector<int>(arr, arr + 3);
    assert (solution.totalHammingDistance(nums) == 8);
    //assert (solution.totalHammingDistance({ -1, 2, 3 }) == 60);

    std::cout << "self test passed" << std::endl;
}

int main()
{
    test();
}
