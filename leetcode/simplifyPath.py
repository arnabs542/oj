#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
71. Simplify Path

Total Accepted: 68595
Total Submissions: 289928
Difficulty: Medium
Contributors: Admin

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

==============================================================================================
SOLUTION

Split string into a list of tokens.
Scan the list, and push tokens into a STACK:
1)    '.', '':ignore
2)    '..': POP previous(if exists) token
3)    else: PUSH

'''

class Solution(object):

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = path.split('/')
        i = 0
        while i < len(stack):
            if not stack[i] or stack[i] == '.':
                stack.pop(i)
            elif stack[i] == '..':
                stack.pop(i)
                if i:
                    i -= 1
                    stack.pop(i)
            else:
                i += 1

        print(stack)
        return '/{}'.format('/'.join(stack))


def test():
    solution = Solution()

    assert solution.simplifyPath('') == '/'
    assert solution.simplifyPath('/home/') == '/home'
    assert solution.simplifyPath('/a/./b/../../c/') == '/c'
    assert solution.simplifyPath('/../') == '/'
    assert solution.simplifyPath('/home//foo/') == '/home/foo'

    print('self test passed')

if __name__ == '__main__':
    test()
