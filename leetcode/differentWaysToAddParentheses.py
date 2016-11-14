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

==============================================================================================
SOLUTION:
Analyze:
Number of parentheses should be equal to th number of operators, since the operators are
binary operators.
Take an expression composed of 4 factors for example:
    ((ab)c)d     (a(bc))d     (ab)(cd)     a((bc)d)     a(b(cd))
i.e.
    (((ab)c)d)   ((a(bc))d)   ((ab)(cd))   (a((bc)d))   (a(b(cd)))

Actually, This is a combinatorial mathematics problem, known as Catalan Number
(https://en.wikipedia.org/wiki/Catalan_number).
$C_{0}=1\quad {\text{and}}
\quad C_{n+1}=\sum _{i=0}^{n}C_{i}\,C_{n-i}\quad {\text{for }}n\geq 0$.
There is a similar problem in CLRS, 3rd: matrix chain multiplication.

1. Treat is as a GRAPH problem, and use BREADTH-FIRST SEARCH or DEPTH-FIRST SEARCH.
Generate well-formed parentheses one by one. The number of factors inside a pair of
parentheses must be two. Then if we have determined these open parentheses, close
parentheses are deterministic.

2. Take advantage of RECURRENCE RELATION of catalan number problems:
f(N)= f(0, N) = f(1, n-1) + f(2, n-2) + ... + f(n-1, 1)

DIVIDE AND CONQUER or DYNAMIC PROGRAMMING?
'''

class memoize(dict):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kw):
        return self[args]

    def __missing__(self, key):
        ret = self[key] = self.func(*key)
        return ret

class Solution(object):

    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        if not expression:
            return []
        tokens = self.parse(expression)
        added = self.addParenthesesDFS(tokens)
        values = list(map(lambda x: eval(x), added))
        print(added, '\n', values, '\n')
        return added

    def parse(self, expression: str):
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

        tokens.append(buf)
        return tokens

    def addParenthesesDFS(self, tokens):
        '''
        Add divide the expression with GRAPH search algorithms(BFS/DFS).

        DEFINE STATE properly to get CLEAR STATE TRANSITION.

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
            num_ops = (end - start) // 2
            s = ''.join(tokens[start:end])
            if not num_ops:
                return [s]
            for i in range(start, end):
                if tokens[i] in ('+', '-', '*', '/'):
                    left, right = dfs(start, i), dfs(i + 1, end)
                    for l in left:
                        for r in right:
                            result.append('({}{}{})'.format(l, tokens[i], r))
            return result

        res = dfs(0, len(tokens))
        return (res)

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
    solution.diffWaysToCompute(expression)

    expression = "2-1"
    solution.diffWaysToCompute(expression)

    expression = "2-1-1"
    solution.diffWaysToCompute(expression)

    expression = "2*3-4*5"
    solution.diffWaysToCompute(expression)

    print('self test passed')

test()
