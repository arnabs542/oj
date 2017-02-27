'''
136. Single Number

Total Accepted: 193278
Total Submissions: 363994
Difficulty: Easy
Contributors: Admin

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using
extra memory?

==============================================================================================
SOLUTION

1. Naive counting method. Use a hash table storing each number' occurrence count.

2. Counting in a BITWISE PERSPECTIVE.
Count with respect to bits.
Set up an array count[] of size equal to integer bits length, assuming 32.
Let count[i] denote the occurrence count of 1 on ith bit, i starting with 0.
Then count[j] is odd if the single number's jth bit is 1. And the rest count[k] are all even.

Space Complexity: O(32N).

3. Bit representing hierarchical states
Because the occurrence count will never exceed 2, we can just use 1 bit to record such
state. And there are 32 bits in an integer, so the auxiliary space is bit[32], i.e. int32,
to record the bit occurrence count.

To distinguish the single bits from those occurs twice, we only need to store the occurrence
count modulo by 1. Then the state is the bit 1 occurrence count modulo by 2.

State transition:
      |Input 0  1
State |____________
0     |      0  1
1     |      1  0

state' = ~state & input + state & ~input = state ^ input.

(As for counting bit occurrence, we can use XOR operation to simplify that. Since 0^1 = 1,
1^1 = 0, count[i] = 1 indicates that the bit occurrence's modulo by 2 is 1.)

So, the state transition function can be formulated by XOR operation.

4. Final version: XOR bit manipulation.
Time complexity: O(n)
    x XOR x == 0

Space complexity: O(N).
'''

class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self.singleNumberBitCounting(nums)
        return self.singleNumberXOR(nums)

    def singleNumberBitCounting(self, nums):
        # TODO: won't work for negative numbers, for Python's integer have infinite bits
        count = [0] * 32
        for i in range(32):
            mask = 1 << i
            for n in nums:
                count[i] ^= (n & mask != 0)

        y = 0
        for i in range(32):
            y |= (count[i] << i)
        print(count, y)
        return y

    def singleNumberXOR(self, nums):
        x = 0
        for i in nums:
            x ^= i

        return x

def test():
    solution = Solution()

    assert solution.singleNumber([-1]) == -1
    assert solution.singleNumber([0]) == 0
    assert solution.singleNumber([9]) == 9
    assert solution.singleNumber([2, 3, 2]) == 3

    print("self test passed")

if __name__ == "__main__":
    test()
