'''
NSum  Question
Generalization of Two Sum, Three Sum, ...

Total Accepted: 89873
Total Submissions: 358826
Difficulty: Medium

Given an array S of n integers, are there N elements a_1, a_2, ..., a_n in S such
that a_1 + a_2 + ... + a_n = target? Find all unique quadruplets in the array which
gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and N = r, target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
  ]
'''

class Solution(object):

    def nSum(self, nums, target, n=2, sort=False):
        """
        :param nums: List[int]
        :param target: int
        :param n: int
        :param sort: bool

        :return: List[List[int]]

        n = 4, 112ms, 95.70%, 2016-10-07 18:09
        """
        if sort:
            # only sort once
            nums.sort()
        if n < 2 or len(nums) < n or target < nums[
                0] * n or target > nums[-1] * n:
            # XXX: early stop, important for optimization for large data
            # without solutions
            return
        if n == 2:
            # TODO(done): two pointers algorithm when n is 2
            low, high = 0, len(nums) - 1
            while low < high:
                curr_sum = nums[low] + nums[high]
                if curr_sum < target:
                    low += 1
                elif curr_sum == target:
                    yield (nums[low], nums[high])
                    while low < high:
                        if nums[low] == nums[low + 1]:
                            low += 1
                        elif nums[high] == nums[high - 1]:
                            high -= 1
                        else:
                            break
                    low += 1
                    high -= 1
                else:
                    high -= 1
        else:
            for i in range(len(nums) - n + 1):
                if i and nums[i] == nums[i - 1]:
                    # avoid duplicate tuples
                    continue
                # XXX: RECURSIVELY reduce n by 1
                for t in self.nSum(nums[i + 1:], target - nums[i], n - 1):
                    yield (nums[i],) + t

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        return list(self.nSum(nums, target, n=4, sort=True))

def test():
    solution = Solution()
    print(list(solution.nSum([-1, -4], -5, 2, sort=True)))
    print(list(solution.nSum([-1, 0, 1, 2, -1, -4], 0, 3, sort=True)))
    print(list(solution.nSum([-2, 0, 0, 2, 2], 0, 3, sort=True)))
    print(list(solution.nSum([
        -4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6], 0, 3, sort=True)))
    print(list(solution.fourSum([1, 0, -1, 0, -2, 2], 0)))

if __name__ == '__main__':
    test()
