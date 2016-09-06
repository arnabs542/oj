"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

SOLUTION:
    brute-force: TLE...
    lexicographical order:
        Find the first pair of two successive ascending numbers a[i] and a[i−1], from the right,
        which satisfy a[i] > a[i-1].
        Swap a[j] and a[i-1] where a[j]>a[i-1] and j >= i, a[j+1] < a[i-1].
        Reverse a[i:].

VARIANT:
    How about permutations of m given n numbers? A_{4}^{2}
    1,2,3 → 1,2,4
    1,3,2 → 1,3,4
    1,3,4 → 1,4,2

"""


class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        exist = False
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                exist = True
                index_j = i
                # find the smallest a[j] that is larger than a[i-1]
                for j in range(i, n):
                    if nums[j] > nums[i-1]:
                        index_j = j
                    else:
                        break
                nums[i - 1], nums[index_j] = nums[index_j], nums[i - 1]
                nums[i:] = reversed(nums[i:])
                break
                pass
            pass
        if not exist:
            nums[:] = reversed(nums)
        pass

def test():
    for nums in [
        [1, 2, 3],
        [3, 2, 1],
        [1, 1, 5],
    ]:
        Solution().nextPermutation(nums)
        print(nums)
    pass

if __name__ == '__main__':
    test()
