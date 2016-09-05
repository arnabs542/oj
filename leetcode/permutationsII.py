# -*-coding:utf-8 -*-
'''
Permutations II

Given a collection of numbers that might contain duplicates, return all
possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
    [1,1,2], [1,2,1], and [2,1,1].

'''


class Solution:
    # @param num,a list of integer
    # @return a list of lists of integers

    def permuteUnique(self, num):
        Solution.res = []
        self.permute(num)
        return self.res

    def permute(self, num, start=0):
        ''' Method 1:

        Backtracking with DEPTH-FIRST SEARCH. But while swapping the element on ith
        index with another element of index j, check for duplicates in range [i, j].
        If there are duplicates, then don't swap to produce duplicate permutations.
        '''
        n = len(num)

        if start == n - 1:
            self.res.append(list(num))
        else:
            for i in range(start, n, 1):
                dup = 0
                # NOTE: when start == i, this loop will not execute
                for j in range(start, i):
                    if num[j] == num[i]:
                        dup = 1
                        break

                if not dup:
                    pass
                    # swap
                    num[start], num[i] = num[i], num[start]
                    self.permute(num, start + 1)
                    # unswap
                    num[start], num[i] = num[i], num[start]

        return self.res

if __name__ == "__main__":
    print(Solution().permuteUnique([1, 1, 2, 2]))
    print(Solution().permuteUnique([1, 2, 3]))
    print(Solution().permuteUnique([1, 1]))
