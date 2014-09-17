'''
Single Number II

Given an array of integers, every element appears three times except for one.
Find that single one.

Note:
    Your algorithm should have a linear runtime complexity.
    Could you implement it without using extra memory?

'''


class Solution:
    # @param A,a list of integers
    # @return an integer

    def singleNumber(self, A):
        ones = 0
        twos = 0
        for i in A:
            twos ^= (ones & i)
            ones ^= i
            mask = ~(ones & twos)
            twos &= mask
            ones &= mask

        return ones

if __name__ == "__main__":
    print Solution().singleNumber([3, 3, 2, 3])
