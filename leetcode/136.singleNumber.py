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

1. Naive counting method.
Use a hash table storing each number' occurrence count.

Complexity: O(N), O(N)

2. Counting in a BITWISE PERSPECTIVE.
Count with respect to bits, and check which bits of 1 have occurred odd times.

Set up an array count[] of size equal to integer bits length, assuming 32.
Let count[i] denote the occurrence count of 1 on ith bit, i starting with 0.
Then count[j] is odd if the single number's jth bit is 1. And the rest count[k] are all even.

Time complexity: O(N),
Space Complexity: O(32) = O(1).

3. Space optimization with one BIT REPRESENTATION of state as count modulo

Instead of use occurrence count as the state, we can keep track of the count modulo by 2.
And implement a state machine with respect to state transition of count modulo by 2.

Taking occurrence count modulo by 2(2 bit integer state), we can just use 1 bit to record such
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

Complexity: O(N), O(32)=O(1)

4. XOR bit manipulation.
Time complexity: O(n)
    x XOR x == 0

Complexity: O(N), O(1).
Space complexity: O(N).

5. Binary search
All elements appear twice except for one, then the size of array must be odd. And if
the array is already SORTED, the target single number can be found by modified binary search
by comparing with adjacent numbers.

'''

class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self._singleNumberBitCounting(nums)
        return self._singleNumberXOR(nums)

    def _singleNumberBitCounting(self, nums):
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

    def _singleNumberXOR(self, nums):
        x = 0
        for i in nums:
            x ^= i

        return x

    # TODO: binary search
    def _singleNumberBinarySearch(self, nums: list):
        nums.sort()
        pass

def test():
    solution = Solution()

    assert solution.singleNumber([-1]) == -1
    assert solution.singleNumber([0]) == 0
    assert solution.singleNumber([9]) == 9
    assert solution.singleNumber([2, 3, 2]) == 3

    print("self test passed")

if __name__ == "__main__":
    test()
