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

Variant: with duplicate elements? Like 1,1,2, 2,3,2, ...
    Solution: while checking validation, count in an element's maximum appearance times

Variant: arrangements of m of n numbers. ( m <= n)
"""


class Solution(object):

    def __init__(self):
        pass

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        # solutions = self.permuteBacktrack(nums)
        solutions = self.permuteDP(nums)
        # solutions = self.permuteDPRollingArray(nums)
        return solutions

    def permuteDP(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Dynamic Programming solution to permutations problem
        state transition relationship:
            permutations[n] = n * permutations[n - 1]

        performance: 98.06%, 2016-09-04 18:32 CST
        """
        permutations = []

        if not nums:
            return []
        permutations.append([[nums[0]]])
        # the dynamic programming
        for i in range(1, len(nums)):
            permutations_i = []
            permutations.append(permutations_i)
            #  state transition process
            for permutation_previous in permutations[i - 1]:
                for j in range(i + 1):
                    permutation = list(permutation_previous)
                    permutation.insert(j, nums[i])
                    permutations_i.append(permutation)
        return permutations[-1]

    def permuteDPRollingArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Dynamic Programming solution to permutations problem
        state transition relationship:
            permutations[n] = n * permutations[n - 1]

        This is a dynamic programming solution with optimized space complexity. We are
        using rolling array here, so we don't have to store all those 1! + 2! + ... + (n - 1)!
        partial solutions

        Runtime performance:  beats 100.00%. 2016-09-05 14:33, CST
        """

        if not nums:
            return []

        permutations_curr = []
        permutations_curr.append([nums[0]])
        # the dynamic programming
        for i in range(1, len(nums)):
            permutations_prev = permutations_curr
            permutations_curr = []
            #  state transition process
            for permutation_prev in permutations_prev:
                for j in range(i + 1):
                    permutation = list(permutation_prev)
                    permutation.insert(j, nums[i])
                    permutations_curr.append(permutation)
        return permutations_curr

    def permuteBacktrack(self, nums, start=0):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if not hasattr(self, 'permutations'):
            self.permutations = []
        n = len(nums)

        if n - 1 <= start:
            self.permutations.append(list(nums))
        else:
            for i in range(start, n):
                self._swap(start, i, nums)
                self.permuteBacktrack(nums, start + 1)
                self._swap(start, i, nums)

        if not start:
            # only return in the top case
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

        permutations = []
        n = len(nums)

        if not nums:
            return []

        class StackFrame(object):

            def __init__(self, start=-1, current=-1):
                self.start   = start
                self.current = current

        stack = []
        stack.append(StackFrame(0, 0))
        # when to POP or PUSH, when to swap and unswap
        while stack:
            frame = stack[-1]
            # generate and so on ...
            # the STACK POP operation
            if frame.start < n and frame.current < n:
                # the STACK PUSH operation is trivial, and it's the POP BACKTRACKING that matters
                # swap to push down
                self._swap(frame.start, frame.current, nums)
                # new stack frame
                stack_new = StackFrame(frame.start + 1, frame.start + 1)
                stack.append(stack_new)
            else:
                if frame.start == n:
                    # found one solution at the end
                    permutations.append(list(nums))
                stack.pop()
                # not only to POP from stack, but also to backtrack to
                # modify the stack's top element's state
                # In another word, to do the staff that we have to do AFTER
                # the CORRESPONDING RECURSIVE PROCEDURE
                if stack:
                    frame = stack[-1]
                    # unswap to restore state
                    self._swap(frame.start, frame.current, nums)
                    frame.current += 1
        pass
        return permutations

    def permuteNextLexicographic(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Method:
            Generate next lexicographical increasing arrangement in a iterative way until
        it reaches the highest(decreasing order) permutation.
        """
        pass

    # TODO: k-permutations of n(arrangement of k numbers from n). DONE!
    # 1. Dynamic Programming approach: denote number of arrangements of k given n by A[n, k].
    # The structure of this problem resembles the 0-1 knapsack problem.
    # then we have:
    #   A[n, k] = #arrangements containing mth number + #arrangements not with mth number
    #           = A[n - 1, k - 1] * k + A[n - 1, k],
    # 2. backtracking with depth-first search
    # 3. lexicographical order next permutation.
    # we add one
    def permuteKofNDP(self, k, n):
        """
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k < 1 or n < 1 or k > n:
            return []
        # initialization
        perms = [[[[]] if not j else []
                  for j in range(k + 1)]
                 for i in range(n + 1)]
        # bottom of the dynamic programming process
        # for i in range(n + 1):
            # perms[i][0].append([])
        for j in range(1, k + 1):
            for i in range(j,n + 1):
                # A[n - 1, k]
                perms[i][j].extend(perms[i -1][j])

                # A[n - 1, k - 1] * k
                for arrangement in perms[i - 1][j - 1]:
                    for idx in range(len(arrangement) + 1):
                        arrangement_new = list(arrangement)
                        arrangement_new.insert(idx, i)
                        perms[i][j].append(arrangement_new)

        return sorted(perms[n][k])

    # TODO: how about arrangement of m from n objects, involving duplicate ones?
    # treat those duplicate objects individually. In another word, assign different index for
    # all candidates, so that we only use those indices to finish the dynamic programming state
    # transition process. When it comes to the recursion formula with A[n, k] and A[n -1, k - 1],
    # be careful while inserting the mth object not to produce duplicate arrangement
    def permuteMofNWithDup(self, k, iterable):
        """
        :type m: int
        :type iterable: iterable
        :rtype: List[List[object]]
        """
        pass

def test():
    for nums in [
            [1, 2, 3],
            [1],
            [],
    ]:
        # print(Solution().permuteBacktrack(nums))
        # print(Solution().permuteDP(nums))
        print(Solution().permuteDPRollingArray(nums))
        # print(Solution().permuteBacktrackIterative(nums))

    # test permutations of m given n
    print(Solution().permuteKofNDP(3, 3))
    print(Solution().permuteKofNDP(2, 3))
    print(Solution().permuteKofNDP(1, 3))

if __name__ == '__main__':
    test()
