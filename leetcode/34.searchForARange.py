'''
34. Search for a Range

Total Accepted: 103256
Total Submissions: 340059
Difficulty: Medium

Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

'''

class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low, high = 0, len(nums) - 1
        start, end = -1, -1
        while low <= high:
            mid = (low + high) >> 1
            print('mid start', mid, low, high)
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                high = mid - 1
                start = mid

        low, high = max(start, 0), len(nums) - 1
        while low <= high:
            print('mid end', mid, low, high)
            mid = (low + high) >> 1
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                end = mid

        return (start, end)

def test():
    solution = Solution()
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))
    pass

if __name__ == '__main__':
    test()
