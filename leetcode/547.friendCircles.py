#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
547. Friend Circles
Medium

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
    Input:
    [[1,1,0],
     [1,1,0],
     [0,0,1]]
    Output: 2
    Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
    The 2nd student himself is in a friend circle. So return 2.

Example 2:
    Input:
    [[1,1,0],
     [1,1,1],
     [0,1,1]]
    Output: 1
    Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
    so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.

================================================================================
SOLUTION

Many to Many connections: GRAPH problem!

In this undirected graph problem, we need to find connected components.

Finding connected components in undirected graph can be achieved by graph seach
or union find.

1. Graph search - breadth first or depth first

Connected components can be found by dfs or bfs.

Complexity: O(N)


2. Union find

"""

class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        result = self._findCircleNumDfs(M)

        print(M, result)

        return result

    def _findCircleNumDfs(self, M):
        def dfs(x):
            visited[x] = True
            for j in range(m):
                if visited[j]: continue
                if M[x][j] == 0: continue
                dfs(j)
            pass
        m = len(M)
        nCircle = 0
        visited = [0 for _ in range(m)]
        for i in range(m):
            if visited[i]: continue
            nCircle += 1
            dfs(i)
        return nCircle

    # TODO: union find solution

def test():
    solution = Solution()

    M = []
    assert solution.findCircleNum(M) == 0

    M = [[1]]
    assert solution.findCircleNum(M) == 1

    M = [
        [1,1,0],
        [1,1,0],
        [0,0,1]]
    assert solution.findCircleNum(M) == 2

    M = [[1,1,0],
         [1,1,1],
         [0,1,1]]
    assert solution.findCircleNum(M) == 1

    print("self test passed")

if __name__ == '__main__':
    test()
