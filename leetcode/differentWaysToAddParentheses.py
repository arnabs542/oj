#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
241. Different Ways to Add Parentheses

Total Accepted: 32442
Total Submissions: 81467
Difficulty: Medium
Contributors: Admin

Given a string of numbers and operators, return all possible results from computing all
the different possible ways to group numbers and operators. The valid operators
are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]

================================================================================
SOLUTION

Analyze
-------
Number of parentheses should be equal to the number of operators, since the operators are
binary operators, and parentheses group operations.

Take an expression composed of 4 factors for example:
    ((ab)c)d     (a(bc))d     (ab)(cd)     a((bc)d)     a(b(cd))
i.e.
    (((ab)c)d)   ((a(bc))d)   ((ab)(cd))   (a((bc)d))   (a(b(cd)))

Actually, This is a combinatorial mathematics problem, known as Catalan Number
(https://en.wikipedia.org/wiki/Catalan_number).
n = 1 + n - 1 = 2 + n - 2 = ... = n - 1 + 1.
And the combinations are not symmetrically identical.

$C_{0}=1\quad {\text{and}}
\quad C_{n+1}=\sum _{i=0}^{n}C_{i}\,C_{n-i}\quad {\text{for }}n\geq 0$.
There is a similar problem in CLRS, 3rd: matrix chain multiplication.

1. Divide and conquer - graph search - dfs - range state
The problem can be reduced to subproblems by fixing the last operation to
carry out.

Treat it as a GRAPH problem, and use BREADTH-FIRST SEARCH or DEPTH-FIRST SEARCH.

Define state as a tuple:
(
    i: expression starting index
    j: expression ending index,
    list of possible expressions with added parentheses,
)

The problem can be thought of a graph traversal problem, where each vertex is
a range of expression, and each edge is an operator that divides the
expression into two subproblems.

For each split, we have multiple choices, because of multiple operators.
Then it shall be done with dfs or bfs.

Complexity: O(2ⁿ) without memoization, O(N²) with memoization.

2. DIVIDE AND CONQUER with more optimization

Instead of generating expressions and compute, accumulate results while
traversing the graph.

Complexity: O(2ⁿ) or O(n²)


3. Take advantage of RECURRENCE RELATION of catalan number problems:
f(N)= f(0, N) = f(1, n-1) + f(2, n-2) + ... + f(n-1, 1)

4. Or DYNAMIC PROGRAMMING?

'''

from _decorators import memoize, timeit

class Solution(object):

    @timeit
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        # result = self._addParenthesesDivideAndConquer(expression)
        result = self._addParenthesesDivideAndConquer2(expression)

        print(expression, " => ", result)

        return result

    def _parse(self, expression: str):
        '''
        parse expression into a list of operators and operands
        '''
        # NOTE: this could be done with re.split('(\D+)', expression)
        tokens = []
        buf = ''
        for c in expression:
            if c.isspace():
                continue
            elif c in ('+', '-', '*', '/'):
                tokens.append(buf)
                tokens.append(c)
                buf = ''
            else:
                buf += c

        if buf: tokens.append(buf)
        return tokens

    def _addParenthesesDivideAndConquer(self, expression):
        '''
        Divide the expression with GRAPH search algorithms(BFS/DFS),
        with backward induction: fixing the last operator.

        DEFINE STATE wisely to exploit STATE TRANSITION.

        Here, we use a tuple(start, end) as the search state, which indicates
        the expression tokens slice[start, end]. Keep dividing the expression
        by an operator while searching.
        '''
        @memoize
        def dfs(start, end):
            '''
            divide with depth-first search.
            '''
            # print('dfs', tokens[start:end], start, end)
            result = []
            num_ops = (end - start) // 2 # should be at least 1
            s = ''.join(tokens[start:end])
            if not num_ops:
                return [s]
            for i in range(start, end):
                if tokens[i] in ('+', '-', '*', '/'): # current operator is the last one
                    left, right = dfs(start, i), dfs(i + 1, end)
                    for l in left:
                        for r in right:
                            result.append('({}{}{})'.format(l, tokens[i], r))
            return result


        if not expression:
            return []
        tokens = self._parse(expression)
        added = dfs(0, len(tokens))
        values = list(map(lambda x: eval(x), added))
        print(added, '\n', values, '\n')
        return (values)

    # DONE: without storing all the expressions with parentheses, instead,
    # compute the result on the go may be faster.
    def _addParenthesesDivideAndConquer2(self, expression):
        """
        Same divide and conquer graph state transition with respect to
        range state.

        The difference is now we're not generating the actual expressions,
        but computing values in one pass.
        """
        tokens = self._parse(expression)
        fOps = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
        }
        @memoize
        def dfs(start, end):
            result = []
            if start > end: return []
            if start == end: return [int(tokens[start])] # base cases
            for i in range(start + 1, end, 2): # divide
                left = dfs(start, i - 1) # conquer subproblems
                right = dfs(i + 1, end) # conquer subproblems
                result += [fOps[tokens[i]](l, r) for l in left for r in right] # combine results
            # print(result)
            return result
        return dfs(0, len(tokens) - 1)

    def addParenthesesBFS(self, tokens):
        '''
        Add divide the expression with GRAPH search algorithms(BFS/DFS).

        DEFINE STATE properly to get CLEAR STATE TRANSITION.

        Can we do it with breadth-first search? Because we need to construct solutions
        from bottom up, it seems tricky to maintain such state that we can backtrack
        with BFS.
        '''
        # TODO: breadth-first solution
        pass

    def addParenthesesDP(self, tokens):
        '''
        different ways to add parentheses with Dynamic Programming

        For overlapping optimal substructures, we consider dynamic programming.
        '''
        # TODO: dynamic programming solution
        pass

def test():
    solution = Solution()

    expression = ""
    assert solution.diffWaysToCompute(expression) == []

    expression = "2-1"
    assert solution.diffWaysToCompute(expression) == [1]

    expression = "2-1-1"
    assert solution.diffWaysToCompute(expression) == [2, 0]

    expression = "2*3-4*5"
    assert solution.diffWaysToCompute(expression) == [-34, -10, -14, -10, 10]

    print('self test passed')

test()
