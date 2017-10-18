# -*-coding:utf-8 -*-

'''
88. Merge Sorted Array

Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
You may assume that A has enough space (size that is greater or equal to m + n) to hold
additional elements from B. The number of elements initialized in A and B are m and n respectively.


'''


class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing

    def merge(self, A, m, B, n):
        i = 0
        j = 0
        while i < m and j < n:
            if A[i] <= B[j]:
                i = i + 1
            elif A[i] > B[j]:
                A.insert(i, B[j])
                m = m + 1
                i = i + 1
                j = j + 1

        if i < m:
            pass
        if j < n:
            while j < n:
                A.insert(i, B[j])
                m = m + 1
                i = i + 1
                j = j + 1

        return A

if __name__ == "__main__":
    print(Solution().merge([1, 3, 5], 3, [2, 4, 6, 8], 4))
