#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
447. Number of Boomerangs

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of
points (i, j, k) such that the distance between i and j equals the distance between i
and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates
of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]


==============================================================================================
SOLUTION

1. Brute force
Enumerate all possible three-tuples in a three level nested for loop.

Complexity: O(C(N, 3)) = O(N³), O(1)

2. Time space trade-off
Computation of all possible pairs' distance is of time complexity O(N²).

Cache the computation result in a hash table.

GROUP BY DISTANCE AND CENTER POINT.

And since we want retrieve tuples of same distance efficiently, we can group by distances
between points. So the keys will the distances.

But, how about the structure of the hash table's values?
There might be multiple tuples containing point j, of same distance.

Since we need to construct the solution tuples, it's better to group by center point.
<distance: <point j: list of points of same distance to point j>>

Solution can be constructed in two steps. First enumerate all possible center points, then
all possible tuples, filling the tuple elements one by one.
But we only need to know the number of tuples, so there is no need to construct the solution,
which could be of time complexity: O(N²). The number can be given by a closed form formula.

If a center point have a list of points, of size m, then the number of possible boomerangs is:
    (m) * (m - 1) * 2

Complexity: O(N²), O(N)

'''

from _decorators import timeit

class Solution(object):

    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # result = self._numberOfBoomerangsHash(points)
        # result = self._numberOfBoomerangsHash2(points)
        result = self._numberOfBoomerangsHash3(points)
        print(result)
        return result

    @timeit
    def _numberOfBoomerangsHash(self, points):
        # FIXME: TIME LIMIT EXCEEDED and MEMORY LIMIT EXCEEDED
        boomerangs = []
        num = 0

        distanceMap = {}
        fun_distance = lambda x, y: (
            x[0] - y[0])**2 + (x[1] - y[1])**2  # square of distance
        for i, point in enumerate(points):
            for j in range(len(points)):
                if i == j:
                    continue
                d = fun_distance(points[i], points[j])
                distanceMap.setdefault(d, {})
                distanceMap[d].setdefault(i, [])
                distanceMap[d][i].append(j)
            pass

        print(distanceMap)
        # step 2, construct solution
        for d, v in distanceMap.items():
            # point j and its points list with same distance
            for j, l in v.items():
                for i in l:
                    for k in l:
                        if i == k:
                            continue
                        num += 1
                        # boomerangs.append([i, j, k,])
        # print(boomerangs)
        return num

    @timeit
    def _numberOfBoomerangsHash2(self, points):
        '''
        Don't construct the solution, only count the number
        '''
        num = 0

        distanceMap = {}
        # square of distance
        f_distance = lambda x, y: (x[0] - y[0])**2 + (x[1] - y[1])**2
        for i, _ in enumerate(points):
            for j in range(len(points)):
                if i == j: continue
                d = f_distance(points[i], points[j])
                distanceMap.setdefault(d, {})
                distanceMap[d][i] = distanceMap[d].get(i, 0) + 1

        # step 2, construct solution
        for d, v in distanceMap.items():
            # point j and its points list with same distance
            for j, m in v.items():
                num += m * (m - 1)
        return num

    @timeit
    def _numberOfBoomerangsHash3(self, points):
        '''
        Don't construct the solution, only count the number
        '''
        num = 0

        distanceMap = {}
        # square of distance
        f_distance = lambda x, y: (x[0] - y[0])**2 + (x[1] - y[1])**2
        for i, _ in enumerate(points):
            for j in range(len(points)):
                if i == j: continue
                d = f_distance(points[i], points[j])
                distanceMap[d] = distanceMap.get(d, 0) + 1
                # incremental counting
                num += 2 * distanceMap[d] - 2
            distanceMap.clear()

        return num

def test():
    solution = Solution()

    points = []
    assert solution.numberOfBoomerangs(points) == 0

    points = [[0, 0]]
    assert solution.numberOfBoomerangs(points) == 0

    points = [[0, 0], [0, 1]]
    assert solution.numberOfBoomerangs(points) == 0

    points = [[0, 0], [1, 0], [2, 0]]
    assert solution.numberOfBoomerangs(points) == 2

    points = [[-1, 0], [0, 0], [1, 0], [0, 1], [0, -1]]
    assert solution.numberOfBoomerangs(points) == 4 * 3 + 4 * 2

    import yaml

    with open("./numberOfBoomerangs.json", "r+") as f:
        cases = yaml.load(f)
    for case in cases:
        points = case['input']
        assert solution.numberOfBoomerangs(points) == case['output']

    print("self test passed")

if __name__ == '__main__':
    test()
