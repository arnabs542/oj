#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
455. Assign Cookies

Total Accepted: 17721
Total Submissions: 37555
Difficulty: Easy
Contributors: µsic_forever

Assume you are an awesome parent and want to give your children some cookies. But,
you should give each child at most one cookie. Each child i has a greed factor gᵢ,
which is the minimum size of a cookie that the child will be content with; and each
cookie j has a size sj. If sⱼ >= gᵢ, we can assign the cookie j to the child i, and
the child i will be content. Your goal is to maximize the number of your content
children and output the maximum number.

Note:
You may assume the greed factor is always positive.
You cannot assign more than one cookie to one child.

Example 1:
Input: [1,2,3], [1,1]

Output: 1

Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
And even though you have 2 cookies, since their size is both 1, you could only make the
child whose greed factor is 1 content.
You need to output 1.

Example 2:
Input: [1,2], [1,2,3]

Output: 2

Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
You have 3 cookies and their sizes are big enough to gratify all of the children,
You need to output 2.

==============================================================================================
SOLUTION

This is similar to ASSIGNMENT PROBLEM, one of combinatoric optimization problems. It
consists of finding a maximum weight matching (or minimum weight perfect matching) in a
WEIGHTED BIPARTITE GRAPH

1. Sort the greed factors and cookie sizes. Assign children with less greed factors first(
greedy strategy).

----------------------------------------------------------------------------------------------
SOLUTION

1. Brute force
Enumerate all possible configuration of cookie assignment. O(mⁿ), where m is the number of
children, n is the number of cookies.

2. Greedy strategy
For each child, try to assign the smallest cookie that is not smaller than the child's greed
factor.

Theorem: Let the children and cookies sorted. Assume the smallest cookie that's not smaller
than greed[0] is cookie[i], then the optimal assignment can be obtained by setting
assignment[i] = 0, meaning we assign cookie[i] to 0th child.


PROVE BY CONTRADICTION

Denote the optimal funtion by f, then the given problem's solution is:
    f(greed[0,...,m], cookie[0,...,n]).
Assume a better solution can be found by setting assignment[i] to some other value.
The current strategy yield a solution:
    f(g[0,...,m], c[0,...,n]) = 1 + f(g[1,...,m], c[i+1,...,n]) = 1 + x.
Assume f(g[1,...,m], c[i+1,...n]) = x.
If we set assignment[i] to another value j > i, the there are two scenarios:
    1) Assign another cookie to 0th child,
    2) Don't assign 0th child any cookie.

Case 1), the solution is: 1 + f(g[1,...,m], c[i,...,j-1,j+1,...,n]) <= 1 + x. This is because
cookie[j] > cookie[i], and substituting a larger cookie with a smaller one doesn't give
a better solution.
Case 2), there are 2 cases, cookie[i] assigned or not. By enumerating the cases, we can find
the solution f(g[1,...,m], c[i,...,n]) <= x + 1.
Those results are not better than the previous one. So the greedy strategy is true.

3. Dynamic programming?

4. Mathematical optimization
Linear Programming.

----------------------------------------------------------------------------------------------
Follow up
1. What if you can assign more than 1 cookie to 1 child?
Mathematical optimization? Dynamic Programming?

'''

class Solution(object):

    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        return self.findContentChildrenSort(g, s)

    def findContentChildrenSort(self, g, s):
        num = 0
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                num += 1
                i += 1
                j += 1
            else:
                j += 1
        return num

    # TODO: follow up 1, assign more than 1 cookie to 1 child

def test():
    solution = Solution()

    assert solution.findContentChildrenSort([], [1, 1]) == 0
    assert solution.findContentChildrenSort([1, 1], []) == 0
    assert solution.findContentChildrenSort([1, 2, 3], [1, 1]) == 1
    assert solution.findContentChildrenSort([1, 2], [1, 2, 3]) == 2

    print("self test passed")

if __name__ == '__main__':
    test()
