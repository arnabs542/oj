"""
46. Permutations

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

Follow up: with duplicate elements? Like 1,1,2, 2,3,2, ...
    Solution: while checking validation, count in an element's maximum appearance times

Follow up: arrangements of m of n numbers. ( m <= n)

==============================================================================================
SOLUTION:

For a general partial permutation problem, we have several ways to define STATES, thus giving
several approaches.

1. Dynamic Programming

Define the state f[n, k] as number of PARTIAL ARRANGEMENTS of k given n.

The structure of this problem resembles the 0-1 knapsack problem.
then we have:
  f[n, k] = #arrangements containing mth number + #arrangements not with mth number
          = f[n - 1, k - 1] * k + f[n - 1, k],

2. Dynamic GRAPH: dfs/bfs
Use BACKTRACKING with DEPTH-FIRST SEARCH or Breadth First Search.

A Dynamic Graph is a graph with dynamic connectivity. Connectivity is represented with the
edges set. In a dynamic graph, its vertices or edges are dynamic. One connection/edge may
be cut during the graph construction, thus forming a backtracking scenario: we need to
restore those states after a dfs subroutine returns. Also, we can pass copies of states/
edges so that we have separate sets of edges at each vertex of the dynamic graph.

In this dynamic graph, the VERTICES are PARTIAL PERMUTATIONS, and the EDGES are distinct
numbers. We generate the permutations by adding numbers one by one to transit from one
vertex to another through an edge.

Define the state f(k) as a partial arrangement of k numbers, where k = 0, 1, ..., K.
Then there always exists such transition from f(k - 1) that

    f(k) = f(k - 1) + [available/non-duplicate number].

In another word, f(k -1) is of the first k - 1 elements in f(k).

Then the graph traversal process is like this:
    Fill the K slots/positions one by one, at each step/depth, we have multiple edges/branches.
Each partial permutation is a VERTEX state, and each available candidate number forms
an EDGE connection.

Both dfs/bfs will do the job.

To sum it up, we have to search algorithms: dfs and bfs. For dfs, we can:
    1) Pass copies of states
    2) Pass indices, for states represented with large objects
    2) Backtrack: mutate state in place, do dfs, restore when dfs subroutine returns.

3. Generative method: Lexicographical order next permutation
Define the state as one possible partial permutation of K numbers. Then at each time we find
the next Lexicographically larger permutation.

==============================================================================================
RECURSIVE CALL TO ITERATIVE

To convert recursive depth-first search call to iterative, we have two
difference implementations.

1. ADAPT BREADTH-FIRST SEARCH process.

Change the search FRONTIER behaviour from QUEUE to STACK, and the rest
is the same with BREADTH-FIRST SEARCH. We PUSH states into the search
frontier, and pop them out, then explore adjacent vertices(states). In
this way, we are pushing all adjacent vertices at the same time.

2. EMULATE THE RECURSIVE CALL mechanism with STACK.

We gather the state composed of function INPUT PARAMETER, VARIABLES USED
AFTER RECURSIVE CALL, recursive call RETURN VALUE and store them as STACK
FRAME. Then for each frame, we determine whether to PUSH or POP.

Then general algorithm procedure skeleton for this would be
1) PUSH state until some condition(STOP CRITERION)
2) POP state until another CONDITION, maybe RESTORING states meanwhile
3) Repeat 1) and 2)

----------------------------------------------------------------------------------------------
Note that the variables used after recursive call contain necessary
information to backtrack(restore states).

The only difference between two version is whether to push adjacent
vertices(states) at one time or one by one.

For DYNAMIC GRAPH, where the edges or vertexes are dynamic, if we want to backtrack (
restoring states after descendants have been visited), we adopt Stack Emulated Recursion
approach.
Otherwise, we need to pass copies of states to avoid backtrack, in order to do
it with the first manner.
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
            result = []
        else:
            # result = self._permuteDFSCopyState(nums)
            result = self._permuteDFSBacktrack(nums)
            # result = self._permuteDFSBacktrackOpt(nums)
            # result = self._permuteDFSBacktrackIterativeOpt(nums)
            # result = self._permuteDP(nums)
            # result = self._permuteDPRollingArray(nums)
        print(result)
        return result

    def _permuteDP(self, nums):
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

    def _permuteDPRollingArray(self, nums):
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

    def _permuteDFSCopyState(self, nums):
        '''
        Pass copies of states
        '''
        def dfs(p, l):
            '''
            Inputs:
            - p: current permutation, vertex state
            - l: available numbers, edge connection

            Outputs:
                None
            '''
            if len(p) == len(nums):
                result.append(p)
                return
            for i in range(len(l)):
                # copy states
                l1 = list(l)
                p1 = list(p)
                p1.append(l[i])
                l1.pop(i)

                dfs(p1, l1)
        result = []
        dfs([], list(nums))
        return result

    def _permuteDFSBacktrack(self, nums):
        '''
        Mutate state inplace by marking edges availability, then backtrack to restore states.
        Optimizing with respect to space complexity: modify inplace, and restore state later
        '''
        def dfs(permutation):
            if len(permutation) == len(nums):
                result.append(list(permutation))
                return
            for i, n in enumerate(nums):
                if n == '#': continue
                nums[i] = '#'
                permutation.append(n)
                dfs(permutation)
                nums[i] = n
                permutation.pop()

        result = []
        dfs([])
        return result

    def _permuteDFSBacktrackOpt(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Dynamic Graph: Backtrack with DEPTH-FIRST SEARCH!

        Optimized backtracking solution by inplace representation.

        The key idea is to partition the edges set by swapping to separate unavailable
        edges/candidates from available ones.

        This is a similar idea to partititoning in quick sort: partition the list into
        two parts of different classes.

        Grow the permutation inplace, position by position. At ith step, we find fill
        this position with an element. And unavailable elements are already placed before
        this position, so current index i serves as a partition point by which available
        elements are separated. Then we can eliminate the extra auxiliary space.

        """
        permutations = []
        def dfs(start):
            if start == len(nums) - 1:
                permutations.append(list(nums))
                return
            for i in range(start, len(nums)):
                # state transition by placing different elements in a slot
                self._swap(start, i, nums)
                dfs(start + 1)
                self._swap(start, i, nums)
        dfs(0)
        return permutations

    @classmethod
    def _swap(cls, i, j, nums):
        nums[i], nums[j] = nums[j], nums[i]

    def _permuteDFSBacktrackIterative(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        permutations = []

        if not nums:
            return []

        # TODO: the stack frame can be reduced to a single number representing
        # the target, because the it's index in the stack already indicates its
        # position
        class StackFrame(object):

            def __init__(self, position=-1, target=-1):
                self.position = position
                self.target   = target

        stack = []
        stack.append(StackFrame(0, 0))
        # when to PUSH or POP, when to swap and unswap
        while stack:
            frame = stack[-1]
            # generate and so on ...
            if frame.position < len(nums) and frame.target < len(nums):
                # the STACK PUSH operation is trivial, and it's the POP BACKTRACKING that matters
                # pushing down: swap to push the target in position
                self._swap(frame.position, frame.target, nums)
                # new stack frame
                stack_new = StackFrame(frame.position + 1, frame.position + 1)
                stack.append(stack_new)
            else:
                # the STACK POP operation
                if frame.position == len(nums):
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
                    self._swap(frame.position, frame.target, nums)
                    frame.target += 1
        pass
        return permutations

    def _permuteDFSBacktrackIterativeOpt(self, nums):
        result = []
        stack = [(0, 0)]
        while stack:
            start, i = stack[-1]
            if len(stack) == len(nums) or i > len(nums) - 1:
                # pop to emulate recursive call returning
                if len(stack) == len(nums): result.append(list(nums))
                stack.pop()
                if stack:
                    start, i = stack.pop()
                    nums[start], nums[i] = nums[i], nums[start] # restore state
                    stack.append((start, i + 1))
            else: # push stack to emulate recursive call
                nums[start], nums[i] = nums[i], nums[start] # mutate state
                stack.append((start + 1, start + 1))
        return result

    def _permuteBFS(self, nums):
        # TODO: breadth-first search approach
        pass

    def _permuteNextLexicographic(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Method:
            Generate next lexicographical increasing arrangement in a iterative way until
        it reaches the highest(decreasing order) permutation.
        """
        pass

    def _permuteKofN(self, k, n):
        # result = self.permuteKofNDP(k, n)
        result = self.permuteKofNDFS(k, n)
        print(result)
        return result

    # DONE: (partial permutation) K-permutations of N(arrangement of K numbers from N).
    def _permuteKofNDP(self, k, n):
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
                # f[n - 1, k]
                perms[i][j].extend(perms[i -1][j])

                # f[n - 1, k - 1] * k
                for arrangement in perms[i - 1][j - 1]:
                    for idx in range(len(arrangement) + 1):
                        arrangement_new = list(arrangement)
                        arrangement_new.insert(idx, i)
                        perms[i][j].append(arrangement_new)

        return sorted(perms[n][k])

    def _permuteKofNDFS(self, k, n):
        '''
        Iterative depth-first search solution
        '''
        result = []
        nums = list(range(1, n + 1))
        stack = [(0, 0)]
        while stack:
            start, i = stack[-1]
            if len(stack) == k or i >= n:
                if i >= n:
                    stack.pop() # recursive call returns
                    if not stack: break
                else:
                    nums[start], nums[i] = nums[i], nums[start]
                    result.append(list(nums[:k]))
                start, i = stack.pop() # recursive call returns
                nums[start], nums[i] = nums[i], nums[start] # restore state
                # print('pushing', (start, i + 1), stack)
                stack.append((start, i + 1))
            else:
                nums[start], nums[i] = nums[i], nums[start] # mutate state
                stack.append((start + 1, start + 1)) # recursive call
        return result

    # TODO: how about arrangement of m from n objects, involving duplicate ones?
    # treat those duplicate objects individually. In another word, assign different index for
    # all candidates, so that we only use those indices to finish the dynamic programming state
    # transition process. When it comes to the recursion formula with f[n, k] and f[n -1, k - 1],
    # be careful while inserting the mth object not to produce duplicate arrangement
    def _permuteMofNWithDup(self, k, iterable):
        """
        :type m: int
        :type iterable: iterable
        :rtype: List[List[object]]
        """
        pass

def test():
    print('permutations')
    assert sorted(Solution().permute([])) == []
    assert sorted(Solution().permute([1])) == [[1]]
    assert sorted(Solution().permute([1, 2])) == [[1, 2], [2, 1]]
    assert sorted(Solution().permute([1, 2, 3])) == [
        [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    # test permutations of m given n
    print('partial permutations')
    assert sorted(Solution()._permuteKofN(1, 3)) == [[1], [2], [3]]
    assert sorted(Solution()._permuteKofN(3, 3)) == [
        [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert sorted(Solution()._permuteKofN(2, 3)) == [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]

if __name__ == '__main__':
    test()
