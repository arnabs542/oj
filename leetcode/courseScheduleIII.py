#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
630. Course Schedule III

There are n different online courses numbered from 1 to n. Each course has some
duration(course length) t and closed on dth day. A course should be taken continuously
for t days and must be finished before or on the dth day. You will start at the 1st day.

Given n online courses represented by pairs (t,d), your task is to find the maximal
number of courses that can be taken.

Example:

Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3

Explanation:
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day.
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.


Note:
The integer 1 <= d, t, n <= 10,000.
You can't take two courses simultaneously.

==============================================================================================
SOLUTION

Interval scheduling problem.

1. Brute force PERMUTATION
Enumerate all non-overlapping interval permutations.

The ORDER of taking courses matters, so it's permutation, not combination problem!

Complexity: O(sum(A(n, k))), O(n)

2. Brute force COMBINATION

The problem here is, the order of taking courses matters.

If we define a one dimensional state, f(n). Then recurrence relation between f(n) and f(n-1)
will not be simply by deciding whether to take the last course. All it matters is what course
to take first! The last course?

Refer to below 'greedy strategy' section...

Back to the current section.
State: (start time t0, starting index i of courses to take)

Initial state = (0, 0), meaning start time is 0, and decide whether to take course 1.

Complexity: O(2ⁿ)

3. Dynamic programming - eliminate overlapping subproblems - 0-1 knapsack problem

The combination method, using depth first search on the graph still involves duplicate calculations.

Overlapping subproblems lead to duplicate computations. Dynamic programming is a method to
tackle that.

For example, we take first course, then subproblem is (t1 + 1, 1); don't take first course,
then subproblem is (0, 1).

Apparently (t1 + 1, 1) is included in (0, 1), since t1 + 1 > 0.

Note that variables are bounded! 1 <= d, t, n <= 10,000, they are all finite!!!

This means, we can enumerate the possible combination of tuple (t, n).
It's like 0-1 knapsack problem. So the overlapping combination problem can be reduced into a
dynamic programming problem!

Define state = (start time t0, starting index i).

Build the state transition table in a top down approach, from (max d, N - 1), down to (0, 0).

Complexity
O(TN), where T is the largest deadline, and N is the size of courses.

4. Greedy Strategy - REDUCE PERMUTATION to COMBINATION by RESTRICTING ORDERING - order of choice

This problem have two aspects: the ORDER of courses, and whether to take a course.
Dynamic programming is degenerated to brute force if there is no specific ORDER of taking courses.
Try to find some greedy strategies to specify the order, avoiding permutation treating.

----------------------------------------------------------------------------------------------
Derive greedy strategy: guess/assume and prove mathematically

Mathematical proof methods:
    Direct proof
    by mathematical induction
    by contraposition
    by CONTRADICTION
    by construction
    by EXHAUSTION
    Probabilistic proof
    Combinatorial proof

Greedy strategy can be proven with contradiction, induction..

Denote a course by [t, d], where t represents duration time and d for close time.

1) Take the one with shorter duration?
Consider case: [[2, 6], [3, 3]].
If we take first course first, then the 2nd can't be taken. Instead, we want to take 2nd, then 1st.

NO, this doesn't yield global optimal solution.

2) Take the one with earlier deadline?

If we have an optimal sequence of courses, can we reorder them by course deadline?

Consider a scenario of two courses [[t1, d1], [t2, d2]], and d1 <= d2.
Will choose the first course be a bad choice, meaning there is an more optimal choice?
Assume above hypothesis be true.

For two courses, the possible permutations are in 2x2=4 cases: 1, 2, 12, 21.
The order makes a difference only when trying to take both of them, like in case '12' and '21'.

If there exist such case, then we have:
    t1 <= d1,
    t2 <= d2,
    d1 < d2, // course one is earlier close time
    t1 + 1 + t2 > d2 // can't take 2nd if take first course first.
    t1 + 1 + t2 < d1 // can take 1st course if we take 2nd course first.

Apparently, there is a contradiction.

So, reordering two adjacent courses by deadline d won't make it worse choice. Even if we already
have the sequence yield the optimal solution, we can reorder them in increasing deadline order.

Lemma:
    For an compatible sequence of courses {c1, c2, ..., cn}, reordering two adjacent courses
c_i, c_{i+1}, to make them ascendingly regarding to deadline will retain the optimality.

Interchanging two adjacent courses, this can be thought as bubble sort, if repeated multiple times.
Then, finally, we can have a sequence sorted courses, ordered by deadline, and it's still compatible.

Reordering compatible courses so that courses with earlier deadline is taken first
won't change the optimality! (But, the reverse reordering may not be serve the same purpose.)

YES, strategy can yield global optimal from local optimal. Choose course with earlier finish time!

----------------------------------------------------------------------------------------------
ORDER DOESN'T MATTER proved!

This means, for the optimal sequence that we are trying to find, we can reorder the courses by
deadline d. This will reduce the permutation to combination!

----------------------------------------------------------------------------------------------
Now, we can develop a GREEDY STRATEGY of taking courses: courses that close earlier comes first!
Now, PERMUTATION IS REDUCED TO COMBINATION by RESTRICTING SPECIFIC ORDER:
    ORDER is determined, and for each course, we only binary decision need to made regarding to
whether to take a course or not!

Actually, this combination problem is similar to another combinatoric problem: 0-1 knapsack problem.
Now, the problem can be solved with graph search or dynamic programming.


5. Optimal Greedy strategy - greedy choice
This combinatorial problem is similar to 0-1 knapsack problem.

However, there is a very subtle difference: items is 0-1 knapsack problem have different VALUE GAIN!
In this course schedule problem, every item(course) has same value gain: 1.
If each course has different credits, and we want to maximize the total credits earned, then it's
knapsack problem.

Since each item has same value gain, we can develop greedy strategy with respect to choosing items!

Greedy strategy:
    Prefer courses with least cost, i.e., duration time!

Sort the courses according to the deadline, then scan the list and choose the courses while we can.
If a course can't be taken, meaning current time t0 + course duration d > course deadline, we can
make greedy strategy decision about removing a course with maximum duration.

How to prove?
Setup, we have a list of compatible courses of size k, now add an incompatible course.

Hypothesis: there won't be a better choice than removing the course with largest duration.
Removing the course with largest cost will retain size k, and have shorter time taken.

Proof
Assume above hypothesis is wrong.

Given c1=[t1, d1], c2=[t2, d2], d1 <= d2, and t1 > t2, will removing c1 be a worse choice than c2?

We have multiple choices: remove the recently added course, remove another course.

1) The recently added is the one with largest cost(duration).

2) Recently added is not the one with largest cost(duration).

Removing one course will at least retain k compatible courses, to yield better result,
to want the cost taken to be minimal.
Better result means: larger compatible courses size, shorter time taken.

TODO: explain this clearly.
A bad choice means, will t0 + t1 <= d1 and t0 + t2 > d2?

d2 >= d1 >= t1 > t2

t0 + t2 < t0 + t1 <= d1 < d2, contradiction!


Complexity: O(NlogN), O(N)

"""

import heapq

class Solution:
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        # result = self._scheduleCourseDfs(courses)
        # result = self._scheduleCourseDp(courses)
        result = self._scheduleCourseGreedyStrategy(courses)

        print(courses, " => ", result)

        return result

    def _scheduleCourseDfs(self, courses: list):
        n = len(courses)
        def dfs(t0, i):
            if i >= n: return 0
            t, d = courses[i]
            if t0 + t > d:
                return dfs(t0, i + 1) # can't take current course
            return max(dfs(t0, i + 1), 1 + dfs(t0 + t, i + 1)) # no cool down time!

        courses.sort(key=lambda x: x[1])

        return dfs(0, 0)

    def _scheduleCourseDp(self, courses: list):
        courses.sort(key=lambda x: x[1])
        N = len(courses)
        T = courses[-1][-1] if courses else 0

        dp = [[0 for _ in range(N + 1)] for _ in range(T + 1)]
        get = lambda x, y: dp[x][y] if (0 <= x < T + 1 and 0 <= y < N + 1) else 0
        for t0 in range(T, -1, -1):
            for i in range(N, 0, -1):
                t, d = courses[i - 1]
                if t0 + t > d:
                    dp[t0][i] = get(t0, i + 1) # can't take this course
                    continue
                dp[t0][i] = max(get(t0, i + 1), 1 + get(t0 + t, i + 1))
                pass
        # print(dp)
        return dp[0][min(1, N)]

    # TODO: more optimization, totally greedy strategy
    def _scheduleCourseGreedyStrategy(self, courses: list):
        """
        Greedy strategy:
        when a new course is in conflict, remove a course with highest duration time.
        """
        courses.sort(key=lambda x: x[1])

        t0 = 0
        completed = []
        for t, d in courses:
            heapq.heappush(completed, -t)
            t0 += t
            if t0 > d and completed:
                d = -heapq.heappop(completed)
                t0 -= d
        return len(completed)


def test():

    solution = Solution()

    courses = []
    assert solution.scheduleCourse(courses) == 0

    courses = [[100, 200]]
    assert solution.scheduleCourse(courses) == 1

    courses = [[1, 2], [2, 3]]
    assert solution.scheduleCourse(courses) == 2

    courses = [[1, 2], [2, 13], [10, 13], [20, 32]]
    # sorted: [[100, 200], [1000, 1250], [200, 1300], [2000, 3200]]
    assert solution.scheduleCourse(courses) == 3

    courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
    # sorted: [[100, 200], [1000, 1250], [200, 1300], [2000, 3200]]
    assert solution.scheduleCourse(courses) == 3

    courses = [[7,16],[2,3],[3,12],[3,14],[10,19],[10,16],[6,8],[6,11],[3,13],[6,16]]
    assert solution.scheduleCourse(courses) == 4

    print("self test passed!")

if __name__ == '__main__':
    test()
