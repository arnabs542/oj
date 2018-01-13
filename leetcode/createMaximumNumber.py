#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
321. Create Maximum Number

Total Accepted: 11779
Total Submissions: 51050
Difficulty: Hard
Contributors: Admin

Given two arrays of length m and n with digits 0-9 representing two numbers.
Create the maximum number of length k <= m + n from digits of the two. The
relative order of the digits from the same array must be preserved. Return an
array of the k digits. You should try to optimize your time and space complexity.

Example 1:
  nums1 = [3, 4, 6, 5]
  nums2 = [9, 1, 2, 5, 8, 3]
  k = 5
  return [9, 8, 6, 5, 3]

Example 2:
  nums1 = [6, 7]
  nums2 = [6, 0, 4]
  k = 5
  return [6, 7, 6, 0, 4]

Example 3:
  nums1 = [3, 9]
  nums2 = [8, 9]
  k = 3
  return [9, 8, 9]

================================================================================
SOLUTION

1. Brute force - combination - depth first search

k = 0 + k = 1 + k - 1 + 2 + k - 2 = ... = k + 0

Create number of i digits from nums1, and j digits from nums2, where i + j = k.
Exhaust all combination and return the maximum.

Define state as a tuple of (
    x: nums1 starting index,
    y: nums2 starting index,
    k: number of digits to create,
) to search the graph.

Then the state transition will follow path

Complexity:
\sum_i{C(m, i)*C(n, k - i)}

With memoization, the complexity will be reduced to O(mnk).

2. Depth first search with greedy strategy

When creating number for a significant position, use one as large as possible
in range, because there is a greedy property when it comes to significant positions.

Complexity: O(k(m+n)), worst case is O(mnk). And the recursive implementation
exceeds the recursion depth.

The worst case occurs when the available maximum number from both lists
are the same. Then we need to consider both situation:
    1) choose the number from list 1 at this significant position
    2) choose the number from list 2 at this significant position

Two search branches means we need to search, maybe in a depth first way!

Maybe iterative solution?


3. Dynamic Programming - eliminate overlapping subproblems

Utilize the RECURSIVE FORMULA to solve the maximum available number of two given arrays
problem.

A MEMOIZED RECURSIVE version will reduce the exponential time complexity but would consume
lot of memory.

And, it still involves many unnecessary computations.

Complexity: O(mnk)

4. Reduce to one list - greedy strategy - two to one & sequence to array

Two lists COMBINATORIAL SEQUENCE choices involves GRAPH SEARCH.
The graph search method involves recursive depth first search, which may exceed limits.

Another perspective: how many digits need to be chosen from one list?
Reduce the problem into one list, and create maximum numbers from two lists separately!

Back to the brute force method, we need to choose i digits from nums1 and k - i digits
from nums2.
Instead of choosing digits simultaneously from two lists, choosing digits from one
list seems much easier.

--------------------------------------------------------------------------------
Why don't we create maximum number of certain digits from two lists separately and merge?

Two lists problem is reduced to one list.
Sequence choice is reduced to array merge.

Then each list has greedy strategy.
Create MAXIMUM number from a list with MONOTONE STACK is O(n).

In the merge process, the problem is still how to choose digit from each of them if
two lists offer same digit.
Greedy strategy: comparing lists, since we are using the whole array, not sequence!

There are k combinations of number of digits, k = 0 + k = 1 + k - 1 = ... = k + 0.

Merge two lists is O(k) on average, but O(k²) on worst case.
Complexity: O(k())

'''

from _decorators import memoize, memoizeMethod, timeit

class Solution(object):

    @timeit
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        print(nums1, nums2, k)
        # result = self._maxNumberDfs(nums1, nums2, k)
        result = self._maxNumberReduceToOneList(nums1, nums2, k)

        print(nums1, nums2, k, ' => ', result)

        return result

    def _maxNumberDfs(self, nums1, nums2, k0):
        m, n = len(nums1), len(nums2)
        @memoize
        def dfs(x, y, k):
            # FIXME: too many unnecessary search, see below implementation
            """
            Brute force combination.

            O(mnk)
            """
            if k == 0: return [], 1
            if k > m - x + n - y: return [], -1

            result = []
            for i in range(x, m):
                d = nums1[i]
                if result and result[0] >= d: continue # prune
                if i < m - 1 and d < nums1[i + 1] and m - i - 1 + n - y >= k: continue # prune
                suffix, err = dfs(i + 1, y, k - 1)

                if err == -1: break # short of numbers
                val = [d] + suffix
                result = max(result, val)

            result1, result = result, []
            for j in range(y, n):
                d = nums2[j]
                if result and result[0] >= d: continue
                if result1 and result1[0] > d: continue
                if j < n - 1 and d < nums2[j + 1] and m - x + n - j - 1 >= k: continue
                suffix, err = dfs(x, j + 1, k - 1)

                if err == -1: break # short of numbers
                val = [d] + suffix
                result = max(result, val)

            result = max(result, result1)
            # print(x, y, k, result)
            return result, 0 if len(result) == k else -1

        argmax = lambda l: max(range(len(l)), key=lambda x: (l[x], -x)) if l else float('-inf')

        @memoize
        def dfs(x, y, k):
            """
            Depth first search with greedy strategy to prune: try to choose maximum digits

            Worst case complexity is: O(mnk), best case is O(k(m+n))
            The worst case is there are many same numbers between two lists, resulting in
            massive(combinatorial) search space.

            """
            if k == 0: return [], 1
            m1 = m - x
            n1 = n - y
            if k > m1 + n1: return [], -1

            result = []
            iMax = x + argmax(nums1[x:x + m1-(k-n1) + 1])
            jMax = y + argmax(nums2[y:y + n1-(k-m1) + 1])
            # print('x, y, imax, jmax: ', x, y, k, iMax, jMax)

            if n1 <= 0:
                result += [nums1[iMax]] + dfs(iMax + 1, y, k - 1)[0]
            elif m1 <= 0:
                result += [nums2[jMax]] + dfs(x, jMax + 1, k - 1)[0]
            elif n1 <= 0 or nums1[iMax] > nums2[jMax]:
                result += [nums1[iMax]] + dfs(iMax + 1, y, k - 1)[0]
            elif m1 <= 0 or nums1[iMax] < nums2[jMax]:
                result += [nums2[jMax]] + dfs(x, jMax + 1, k - 1)[0]
            else:
                result = [nums1[iMax]] + max(
                    dfs(iMax + 1, y, k - 1)[0], dfs(x, jMax + 1, k - 1)[0])

            # print(x, y, k, result)
            return result, 0

        # @memoize
        def dfs1(x, y, k):
            """
            WRONG ANSWER

            Since choosing digits sequence, can't use list comparison to determine
            the greedy strategy.
            """
            m, n = len(nums1), len(nums2)
            if k == 0: return [], 1
            result = []
            while k > 0:
                m1 = m - x
                n1 = n - y
                if k > m1 + n1: return [], -1

                iMax = x + argmax(nums1[x:x + m1-(k-n1) + 1])
                jMax = y + argmax(nums2[y:y + n1-(k-m1) + 1])
                # print('x, y, k, iMax, jMax', x, y, k, iMax, jMax)

                if n1 <= 0:
                    # result += [nums1[iMax]] + dfs(iMax + 1, y, k - 1)[0]
                    result.append(nums1[iMax])
                    x = iMax + 1
                elif m1 <= 0:
                    # result += [nums2[jMax]] + dfs(x, jMax + 1, k - 1)[0]
                    result.append(nums2[jMax])
                    y = jMax + 1
                elif n1 <= 0 or nums1[iMax] > nums2[jMax]:
                    # result += [nums1[iMax]] + dfs(iMax + 1, y, k - 1)[0]
                    result.append(nums1[iMax])
                    x = iMax + 1
                elif m1 <= 0 or nums1[iMax] < nums2[jMax]:
                    # result += [nums2[jMax]] + dfs(x, jMax + 1, k - 1)[0]
                    result.append(nums2[jMax])
                    y = jMax + 1
                else:
                    result.append(nums1[iMax])
                    if nums1[iMax + 1:] >= nums2[jMax + 1:]:
                        # use 1
                        x = iMax + 1
                    else:
                        y = jMax + 1
                        # use 2
                    # result = [nums1[iMax]] + max(
                        # dfs(iMax + 1, y, k - 1)[0], dfs(x, jMax + 1, k - 1)[0])
                k -= 1

            # print(x, y, k, result)
            return result, 0


        print(len(nums1), len(nums2), k0)
        nums1[:], _ = dfs(0, len(nums2), min(k0, len(nums1)))
        nums2[:], _ = dfs(len(nums1), 0, min(k0, len(nums2)))
        print('reduced nums1, nums2, ', nums1, nums2, k0)
        ret, _ = dfs(0, 0, k0)
        return ret

    def _maxNumberReduceToOneList(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        maxNum = []
        def createMax(arr, p): # create maximum number of k digits, with monotone STACK
            if p > len(arr): return []
            stack = []
            for i, x in enumerate(arr):
                while stack and stack[-1] < x and len(arr) - 1 - i + len(stack) >= p:
                    stack.pop() # whether can pop depends on elements after it
                stack.append(x)

            return stack[:p]

        def merge(l1, l2):
            l = []
            i, j = 0, 0
            while i < len(l1) and j < len(l2):
                if l1[i] > l2[j]:
                    l.append(l1[i])
                    i += 1
                elif l1[i] < l2[j]:
                    l.append(l2[j])
                    j += 1
                else:
                    # greater list for greedy strategy
                    if l1[i + 1:] > l2[j + 1:]:
                        # use 1
                        l.append(l1[i])
                        i += 1
                    else:
                        # use 2
                        l.append(l2[j])
                        j += 1

            l += l1[i:]
            l += l2[j:]

            return l

        for i in range(k + 1):
            p = min(i, len(nums1))
            if i > len(nums1) or k - i > len(nums2): continue
            a = createMax(nums1, p)
            b = createMax(nums2, k - p)
            maxNum = max(maxNum, merge(a, b))
            print('reduced: ', a, b, merge(a, b))

        return maxNum


def test():

    solution = Solution()

    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5
    assert solution.maxNumber(nums1, nums2, k) == [9, 8, 6, 5, 3]

    nums1 = [6, 7]
    nums2 = [6, 0, 4]
    k = 5
    assert solution.maxNumber(nums1, nums2, k) == [6, 7, 6, 0, 4]

    nums1 = [6, 7]
    nums2 = [6, 6, 7]
    k = 4
    assert solution.maxNumber(nums1, nums2, k) == [7, 6, 6, 7]

    nums1 = [6, 7]
    nums2 = [6, 6, 7]
    k = 5
    assert solution.maxNumber(nums1, nums2, k) == [6, 7, 6, 6, 7]

    nums1 = [6, 0]
    nums2 = [6, 7, 4]
    k = 5
    assert solution.maxNumber(nums1, nums2, k) == [6, 7, 6, 4, 0]

    nums1 = [3, 9]
    nums2 = [8, 9]
    k = 3
    assert solution.maxNumber(nums1, nums2, k) == [9, 8, 9]

    nums1 = []
    nums2 = [8, 9, 3, 9]
    k = 3
    assert solution.maxNumber(nums1, nums2, k) == [9, 3, 9]

    nums1 = [6, 7, 5]
    nums2 = [4, 8, 1]
    k = 3
    assert solution.maxNumber(nums1, nums2, k) == [8, 7, 5]

    nums1 = [6, 4, 7, 8, 6, 5, 5, 3, 1, 7, 4, 9, 9, 5, 9, 6, 1, 7, 1, 3, 6, 3, 0, 8, 2, 1, 8, 0, 0, 7, 3, 9, 3, 1, 3, 7, 5, 9, 4, 3, 5, 8, 1, 9, 5, 6, 5, 7, 8, 6, 6, 2, 0, 9, 7, 1, 2, 1, 7, 0, 6, 8, 5, 8, 1, 6, 1, 5, 8, 4]
    nums2 = [3, 0, 0, 1, 4, 3, 4, 0, 8, 5, 9, 1, 5, 9, 4, 4, 4, 8, 0, 5, 5, 8, 4, 9, 8, 3, 1, 3, 4, 8, 9, 4, 9, 9, 6, 6, 2, 8, 9, 0, 8, 0, 0, 0, 1, 4, 8, 9, 7, 6, 2, 1, 8, 7, 0, 6, 4, 1, 8, 1, 3, 2, 4, 5, 7, 7, 0, 4, 8, 4]
    k = 70
    assert solution.maxNumber(nums1, nums2, k) == [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5, 6, 5, 7, 8, 6, 6, 2, 0, 9, 7, 1, 2, 1, 7, 0, 8, 0, 6, 8, 5, 8, 1, 6, 1, 5, 8, 4, 0, 0, 0, 1, 4, 8, 9, 7, 6, 2, 1, 8, 7, 0, 6, 4, 1, 8, 1, 3, 2, 4, 5, 7, 7, 0, 4, 8, 4]

    import sys
    # sys.setrecursionlimit(6000)
    import yaml
    with open("./createMaximumNumber.json", 'r') as f:
        data = yaml.load(f)
    for r in data:
        assert solution.maxNumber(*r['input']) == r['output']

    print('self test passed')

if __name__ == '__main__':
    test()
