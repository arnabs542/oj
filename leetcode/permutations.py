"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):

    def __init__(self):
        pass

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solutions = self.permuteBacktrack(nums)
        return solutions

    def permuteDP(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Dynamic Programming solution to permutations problem
        state transition relationship:
            permutations[n] = n * permutations[n - 1]
        """
        pass

    def permuteBacktrack(self, nums, start=0):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not hasattr(self, 'permutations'):
            self.permutations = []
        if len(nums) - 1 <= start:
            self.permutations.append(list(nums))
        else:
            for i in range(start, len(nums)):
                self._swap(start, i, nums)
                self.permuteBacktrack(nums, start + 1)
                self._swap(start, i, nums)

        if not start:
            return self.permutations
        return

    @classmethod
    def _swap(cls, i, j, nums):
        nums[i], nums[j] = nums[j], nums[i]


    def permuteBacktrackIterative(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        pass

    def permuteLexicographic(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        pass

def test():
    nums = [1, 2, 3]
    print(Solution().permuteBacktrack(nums))

if __name__ == '__main__':
    test()
