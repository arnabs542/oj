'''
1. Two Sum

Total Accepted: 350333
Total Submissions: 1228763
Difficulty: Easy
Contributors: Admin

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

===============================================================================================
Solution

1. brute-force

Complexity: O(N²)

2. hash: (key=element, value=element's position/index)

Complexity: O(N), O(N)

3. sort: two pointers, move index from two ends to center

Complexity: O(nlogn), O(1)

'''

class Solution(object):
    # @return a tuple (index1,index2)

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = self._twoSumHash(nums, target)

        print(nums, target, result)

        return result

    def _twoSumHash(self, nums, target):
        mapping = dict()
        for k, v in enumerate(nums):
            if target - v in mapping and mapping[target - v] != k:
                return sorted([k, mapping[target - v]])
            mapping[v] = k
        return []

if __name__ == "__main__":
    assert (Solution().twoSum([3, 2, 4], 6)) == [1, 2]
    assert (Solution().twoSum([2, 7, 11, 15], 9)) == [0, 1]

    print("self test passed!")
