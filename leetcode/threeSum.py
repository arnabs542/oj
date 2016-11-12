'''
15. 3Sum  Question

Total Accepted: 149341
Total Submissions: 741192
Difficulty: Medium

Given an array S of n integers, are there elements a, b, c in S such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of
zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

SOLUTION:
    Two pointers scan an array from two sides to middle.
'''

class Solution(object):

    def twoSum(self, nums, s):
        nums_len = len(nums)
        i, j = 0, nums_len - 1
        while i < j:
            curr_sum = nums[i] + nums[j]
            # print('two sum', i, j, curr_sum, s)
            if curr_sum < s:
                i += 1
            elif curr_sum == s:
                yield (nums[i], nums[j])
                while i < j and nums[i] == nums[i + 1]:
                    i += 1
                while i < j and nums[j] == nums[j - 1]:
                    j -= 1
                i += 1
                j -= 1
            else:
                j -= 1
        return

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        results = []
        if len(nums) < 3:
            return results

        nums = sorted(nums)
        # TODO: the set data structure could be eliminated by increasing the
        # pointer if two adjacent elements in the sorted array are the same
        used = set()

        for (i, num) in enumerate(nums[:-2]):
            # print(i, num)
            if num > 0:
                return results
            if num in used:
                continue
            used.add(num)

            for t in self.twoSum(nums[i + 1:], -num):
                results.append((num, ) + t)
        return results

def test():
    solution = Solution()
    print(solution.threeSum([-1, -4]))
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
    print(solution.threeSum([-2, 0, 0, 2, 2]))
    print(solution.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))

if __name__ == '__main__':
    test()
