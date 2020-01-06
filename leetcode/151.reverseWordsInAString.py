#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
151. Reverse Words in a String
Medium

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

click to show clarification.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.

================================================================================
SOLUTION

1. Split into words and reverse words

Reverse can be done with recurrence relation by STACK or two pointers swap.

Stack can be treated as a one end state transition recurrence relation:
    f(n) = a[n] + f(n-1)

Two pointers swap method can be thought as two ends state transition
recurrence relation:
    f(i, j) = a[j] + f(i + 1, j - 1) + f(i)

And two pointers swap uses O(1) extra space.

To eliminate the extra spaces, use a PARTITION based method:
    Keep track of the division point

Complexity: O(N), O(N)

2. Two-pointers swap in two passes to reverse in place
1) Reverse characters of whole string in place
2) Reverse characters in each word in place

To remove extra spaces, we need to shift characters in another pass.

Complexity: O(N), O(1)

'''

class Solution:
    # @param s, a string
    # @return a string

    def reverseWords(self, s):
        # result = self._reverseWordsSplitUgly(s)
        result = self._reverseWordsSplitStack(s)

        print(s, " => ", result)

        return result

    def _reverseWordsSplitUgly(self, s):
        if not isinstance(s, str):
            raise TypeError
        #words = s.split(' ')
        words = s.split()
        j = 0
        for i in range(len(words) - 1, j, -1):
            # print '%d,words[%d] is %s' % (j,i,words[i])
            # comment out debug outputs,which may cause "Output limit exceeded"
            # error on OJ
            if i <= j:
                break
            if not words[i].isspace():
                if words[j] != ' ':
                    tmp = words[j]
                    words[j] = words[i]
                    words[i] = tmp
                    j = j + 1
                else:
                    #words.remove(' ')
                    del words[i]
            # else:
                # words.remove(' ')

        new_s = ' '.join(words)
        return new_s

    def _reverseWordsSplitStack(self, s):
        words = s.split() # white spaces are eliminated already
        result = ' '.join(reversed(words))

        return result

def test():
    a = Solution()
    assert a.reverseWords('hello world    My name is Bishop') == 'Bishop is name My world hello'
    print("self test passed")

if __name__ == "__main__":
    test()
