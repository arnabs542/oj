#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
316. Remove Duplicate Letters

Total Accepted: 22381
Total Submissions: 79923
Difficulty: Hard
Contributors: Admin

Given a string which contains only lowercase letters, remove duplicate letters so that every
letter appear once and only once. You must make sure your result is the smallest in
lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"


================================================================================
SOLUTION

To remove is straightforward, the problem is to make it as small as possible.
And there are many to remove, a little bit complex.

The problem is the locally optimal choices don't always yield globally optimal.


1. Brute force - depth first search - Cartesian product

Complexity: O((n/26)^26) in worst case, where n is the string length.

2. Greedy strategy when adding letters

Thinking backward, in the complement situation, it's  mush easier to add!
Wrong answer...

Get a list of character indices, choose one place to add.
Where to add depends on...

Binary search to get lower bound where to insert?
The problem is, the letters added after may change the previous optimal solution.
This approach doesn't illustrate non-aftereffect property.

3. Monotone stack
In theory, lexicographically smallest sequence is the increasing sequence.
Then maintain a monotone stack, containing monotonically increasing sequence
of letters.
For each new letter, decide whether to push or pop, depending on:
    1) whether it's already in the stack
    2) if already in stack, continue
    3) if not in stack, pop out stack top, if stack top has another occurrence
after
    4) push into the new letter

Complexity: O(N)

'''


from collections import Counter, defaultdict

class Solution(object):

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # result = self._removeDuplicateLetters(s)
        # result = self._removeDuplicateLettersGreedyAdd(s)
        # result = self._removeDuplicateLettersMonotoneStack(s)
        result = self._removeDuplicateLettersMonotoneStackOpt(s)

        print(s, ' => ', result)

        return result

    def _removeDuplicateLetters(self, s):
        # FIXME: wrong answer for some test cases?
        chars = list(s)
        ch2idx = {}
        for i in range(len(chars) - 1, -1, -1):
            if chars[i] in ch2idx:
                j = ch2idx[chars[i]]
                remove = i if chars[i + 1:j + 1] < chars[i:j] else j
                ch2idx[chars[i]] = remove ^ i ^ j
                chars[remove] = ''
            else:
                ch2idx[chars[i]] = i

        chars1 = chars

        chars = list(s)
        ch2idx = {}
        for i in range(len(chars)):
            if chars[i] in ch2idx:
                j = ch2idx[chars[i]]
                remove = i if ''.join(chars[j:i]) < ''.join(chars[j + 1:i + 1]) else j
                ch2idx[chars[i]] = remove ^ i ^ j
                chars[remove] = ''
            else:
                ch2idx[chars[i]] = i

        print(s, chars)
        print(min(''.join(chars1), ''.join(chars)))

        return min(''.join(chars1), ''.join(chars))

    def _removeDuplicateLettersGreedyAdd(self, s):
        chars = ['' for _ in range(len(s))]

        char2indices = defaultdict(list)
        char2idx = {}
        for i, c in enumerate(s):
            char2indices[c].append(i)

        for i in range(26):
            c = chr(ord('a') + i)
            if c not in char2indices:
                continue

            indices = char2indices[c]

            j = 0
            # check smaller characters between current and largest index.
            for k in char2idx.values():
                while indices[j] < k < indices[-1] and j < len(indices) - 1:
                        j += 1
                if j == len(indices) - 1: break
            char2idx[c] = indices[j]
            chars[indices[j]] = c

        return ''.join(chars)

    def _removeDuplicateLettersMonotoneStack(self, s):
        stack = []
        indices = defaultdict(list)
        for i, c in enumerate(s):
            indices[c].append(i)
        for i, c in enumerate(s):
            if c not in stack:
                while stack and stack[-1] >= c and indices[stack[-1]]:
                    stack.pop()
                stack.append(c)
            indices[c].pop(0)

        return ''.join(stack)

    def _removeDuplicateLettersMonotoneStackOpt(self, s):
        stack = []
        maxIndex = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            if c not in stack:
                while stack and stack[-1] >= c and maxIndex.get(stack[-1], -1) > i:
                    stack.pop()
                stack.append(c)

        return ''.join(stack)


def test():
    solution = Solution()

    assert solution.removeDuplicateLetters('') == ''
    assert solution.removeDuplicateLetters('a') == 'a'
    assert solution.removeDuplicateLetters('bcabc') == 'abc'
    assert solution.removeDuplicateLetters('cbacdcbc') == 'acdb'
    assert solution.removeDuplicateLetters('abacb') == 'abc'

    print('self test passed')

if __name__ == '__main__':
    test()
