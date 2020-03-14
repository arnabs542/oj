#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
22. Generate Parentheses

Total Accepted: 115999
Total Submissions: 283473
Difficulty: Medium
Contributors: Admin

Given n pairs of parentheses, write a function to generate all combinations of well-formed
parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

SOLUTION
================================================================================
Treated as a GRAPH problem, it can be solved with BREADTH-FIRST SEARCH or
DEPTH-FIRST SEARCH. The key is to define proper state with RECURRENCE RELATION.

BUILD GRAPH:
  in a POSITION PERSPECTIVE, instead of element perspective which is to add
a new pair of parentheses every time.

1. Depth first search - bottom up filling positions
There are two approaches:
1) Bottom up adding new element approach
The well-formed combination is a string of length 2n. Then the process is to
generate 2n symbols.

Define state(vertex):
    (current string of parentheses, number of open and close parenthesis)
State transition: adding a new symbol '(' or ')'.

At each time, there are two BRANCHES: generate open '(' or close parenthesis ')'.
And the number of ')' can not be more than #'(' at any position.

2) Top down decomposing approach
Problem of N pairs can be decomposed into n different subproblems:
  n -> 1 + n-1, 2 + n-2, ..., n-1 + 1.
A divide and conquer approach, and this catalan number:
  C(n) = Σ{i=0,n-1}C(i)C(n-i).


Define state vertex: set of n pairs of parentheses.
State transition: decomposition like above.

2. Breadth first search
Define state:
  (current partial combination, number of open parentheses, number of close parentheses)

Time Complexity: Catalan number.

3. Top down depth first search - top down dividing n
n = (0+n) = (1+(n-1)) = 2 + (n-2) = ... = (n-1) + 1


'''

class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = self.generateParenthesisBFS(n)
        # result = self.generateParenthesisDFS(n)
        print(result)
        return result

    def generateParenthesisBFS(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        state = (n, n, '')  # state = (#'(', #')', current output string)
        frontier = [state]
        while frontier:
            state = frontier.pop(0)
            if state[0] == state[1] == 0:
                result.append(state[-1])
            else:
                for neighbor in ((state[0] - 1, state[1], state[-1] + '('),
                                 (state[0], state[1] - 1, state[-1] + ')')):
                    if neighbor[1] < neighbor[0] or \
                       neighbor[0] < 0 or neighbor[1] < 0:
                        continue
                    frontier.append(neighbor)
                    pass
                pass
            pass

        return result

    def generateParenthesisDFS(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def dfs(state):
            if state[0] == state[1] == 0:
                result.append(state[-1])
            for neighbor in ((state[0] - 1, state[1], state[-1] + '('),
                             (state[0], state[1] - 1, state[-1] + ')')):
                if neighbor[1] < neighbor[0] or \
                   neighbor[0] < 0 or neighbor[1] < 0:
                    continue
                dfs(neighbor)
        state = (n, n, '')
        dfs(state)

        return result

    def generateParenthesisDP(self, n):
        """
        :type n: int
        :rtype: List[str]

        Harness the recurrence relation:
            f(n) = f(0,n) + f(1, n - 1) + ... + f(n - 1, 1)
        e.g. n = 3: f(3) = 1 + 2 + 2 = 5

        But a single variable state won't suffice to build up the transition
        process.

        We need two variables to form a tuple state:
          (number of open parenthesis, # close parentheses)
        """
        # TODO: dynamic programming

def test():
    solution = Solution()

    assert solution.generateParenthesis(0) == [''] # 1
    assert solution.generateParenthesis(1) == ['()'] # 1
    assert solution.generateParenthesis(2) # 2
    assert solution.generateParenthesis(3) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ] # 1
    assert solution.generateParenthesis(5)
    print('self test passed')
    pass

test()
