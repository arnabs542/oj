'''
137. Single Number II

Given an array of integers, every element appears three times except for one.
Find that single one.

Note:
    Your algorithm should have a linear runtime complexity.
    Could you implement it without using extra memory?

==============================================================================================
SOLUTION

1. Naive number count.
Time complexity: O(N), Space complexity: O(N).

2. Count in a BITWISE PERSPECTIVE.
Count with respect to bits.

Set up an array count[] of size equal to integer bits length, assuming 32.
Let count[i] denote the occurrence count of 1 on ith bit, i starting with 0.

To differentiate the single bits, we only need to store the bit occurrence count modulo by
3 in count[].

Then jth bit appears in the single number if and only if count[j] = 1, j starting with 0.

There are 32 bits to count respectively, so 32 integers are needed to record it.

Time complexity: O(N)
Space complexity: 32 integers corresponding to 32 bits' occurrence count. O(32) = O(1).

3. Space optimization: store bitwise count MODULO by 3

Then, for each bit count modulo by 3, only two bits are needed, totally 32*2=64 bits.

The idea is similar to circuit design where we manipulate bits to represent numbers, and
design a Finite State Machine to transit states.

Because the occurrence count will never exceed 3, 2=ceil(log3) bits can store STATE
representing  a specific bit's occurrence count. And there are 32 bits in an integer, so the
auxiliary space is bit[32][2], i.e. int32[2].

Now we have hierarchical state, forming a Finite State Machine(Hierarchical State Machine).

For a ith bit, denote bit[i][0], bit[i][1] by b, a respectively.
State transition table:
________________________
current     input   next
a b            c    a' b'
0 0            0    0  0
0 0            1    0  1
0 1            0    0  1
0 1            1    1  0
1 0            0    1  0
1 0            1    0  0
1 1 NA(no such state)
1 1 NA

The state transition closed-form formula:
    a' = a&~b&~c + ~a&b&c  = a&() = a^(b&c),
    b' = ~a&b&~c + ~a&~b&c = ~a&(b&~c + ~b&c) = ~a&(b^c),
i.e.:
    b' = ~a&b&~c + ~a&~b&c = ~a&(b^c),
    a' = ~b'&a&~c + ~b'&~a&c = ~b'&(a^c).

After the numbers stream are processed, count[i] = 1 if and only if those ith bit
appear in the single number. Thus, the

As for counting bit occurrence, we can use XOR operation to simplify that. Since 0^1 = 1,
1^1 = 0, count[i] = 1 indicates that the bit occurrence's modulo by 2 is 1.
So, the state transition function can be formulated by XOR operation.

Time complexity: O(N)
Space complexity: Only ceil(log₂3)=2 integers, O(1)

==============================================================================================
Follow up
1. When every one occurs K times except one occurs M times, where M is a multiple of K.

Answer:
    we can't take modulo operation with K, because M % K = 0 = K % K, not differentiable.
The divisor P can be chosen in range [max(K, M), ∞].
And the number of hierarchical bits we need is ceil(log₂(P)).

'''

class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self.singleNumberBitCount(nums)
        return self.singleNumberXOR(nums)

    def singleNumberBitCount(self, nums):
        '''
        3 states.
        '''
        # initialization
        # each number storing count of occurrence of corresponding bit 1
        count = [0] * 32
        # maintenance: state transition
        for i in range(32):
            mask = 1 << i
            for _, n in enumerate(nums):
                if n & mask != 0:
                    count[i] = (count[i] + 1) % 3
        single = 0
        for i in range(32):
            single |= (1 << i) if count[i] else 0
        return single

    def singleNumberXOR(self, nums):
        ones = twos = 0
        for i in nums:
            ones = ~twos & (ones ^ i)
            twos = ~ones & (twos ^ i)

        return ones

def test():
    solution = Solution()

    assert Solution().singleNumber([1]) == 1
    assert Solution().singleNumber([3, 3, 2, 3]) == 2
    assert Solution().singleNumber([3, 3, -1, 3]) == -1

    print("self test passed")

if __name__ == "__main__":
    test()
