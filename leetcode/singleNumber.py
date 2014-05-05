'''
Single Number

Given an array of integers, every element appears twice except for one.
Find that single one.

Note:
    Your algorithm should have a linear runtime complexity.
    Could you implement it without using extra memory?
    '''

'''
Solution:
    XOR bit manipulation.
    x xor x == 0
    '''

class Solution:
    # @param A,a list of integer
    # @returns an integer
    def singleNumber(self,A):
        x = A[0]
        for i in A[1:]:
            x ^= i

        return x

if __name__ == "__main__":
    pass
