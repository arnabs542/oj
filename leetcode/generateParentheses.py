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
===============================================================================================
SOLUTION:
    Treated as a GRAPH problem, it can be solved with BREADTH-FIRST SEARCH or DEPTH-FIRST SEARCH.

The well-formed combination is a string of length 2n. Then we can generate a character for 2n times.
At each time, there are two BRANCHES: generate open parenthese '(' or close parenthese ')'. And the
number of ')' can not be more than #'(' in any substring starting from 0.

Time Complexity: Catalan number.
'''

class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # result = self.generateParenthesisBFS(n)
        result = self.generateParenthesisDFS(n)
        print(result)
        return result

    def generateParenthesisBFS(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        state = (n, n, '')
        frontier = [state]
        while frontier:
            state = frontier.pop(0)
            if state[0] == state[1] == 0:
                result.append(state[-1])
            else:
                for neighbor in ((state[0] - 1, state[1], state[-1] + '('),
                                 (state[0], state[1] - 1, state[-1] + ')')):
                    if neighbor[1] < neighbor[0] or neighbor[0] < 0 or neighbor[1] < 0:
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
                if neighbor[1] < neighbor[0] or neighbor[0] < 0 or neighbor[1] < 0:
                    continue
                dfs(neighbor)
        state = (n, n, '')
        dfs(state)

        return result

def test():
    solution = Solution()

    assert solution.generateParenthesis(0) == ['']
    assert solution.generateParenthesis(1) == ['()']
    assert solution.generateParenthesis(3) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ]
    print('self test passed')
    pass

test()
