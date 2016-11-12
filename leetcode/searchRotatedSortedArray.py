# -*- encoding:utf-8 -*-

'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''


class Solution:
    # @param A,a list of integers
    # @param target,an integer to be searched
    # @return an integer

    def search(self, A, target):
        n = len(A)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) >> 1
            if A[mid] == target:
                return mid
            if A[low] == target:
                return low
            if A[high] == target:
                return high

            if target < A[mid]:
                if A[mid] > A[high]:
                    # print A[mid], target
                    if A[low] < target:
                        low += 1
                        high = mid - 1
                    else:
                        low = mid + 1
                        high -= 1
                else:
                    low += 1
                    high = mid - 1
            elif target > A[mid]:
                if A[mid] > A[low]:
                    low = mid + 1
                    high -= 1
                else:
                    if A[high] > target:
                        low = mid + 1
                        high -= 1
                    else:
                        low += 1
                        high = mid - 1

        return -1

if __name__ == "__main__":
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 2))
    print(Solution().search([5, 1, 2, 3, 4], 1))
    print(Solution().search([5, 6, 7, 8, 9, 1, 2, 3, 4], 2))
