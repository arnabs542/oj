#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
68. Text Justification
Hard

Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

Corner Cases:
A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.

================================================================================
SOLUTION

1. Linear scan and greedy
How about "divide evenly?"

Divide m spaces evenly to n groups. Then there are at most two groups with number
of spaces difference by 1.
The each group has at most x = ceil(m / n) spaces. The other groups may have
x - 1 spaces. Assume a groups of x, b groups of x - 1, then we have:
    m + b = nx
    a + b = n
So,
    b = nx - m
    a = n - b

Just don't forget edge cases.

"""

import math

class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = self._fullJustifyGreedy(words, maxWidth)

        print(words, maxWidth, "=>", result)

        return result

    def _fullJustifyGreedy(self, words, maxWidth):
        result = []
        i = 0
        while i < len(words):
            l = 0
            nWords = 0
            while i < len(words) and l + nWords + len(words[i]) <= maxWidth: # greedy match
                l += len(words[i])
                nWords += 1
                i += 1
            if nWords == 0 and i < len(words):
                print("very long word", maxWidth)
                return [] # long word
            nBlank = nWords - 1
            totalPadding = maxWidth - l

            line = ""
            j = i - nWords
            if i == len(words): # last line
                for _ in range(nWords):
                    line += (' ' if j > i - nWords else '') + words[j]
                    j += 1
                line += ' ' * (totalPadding - nWords + 1)
            elif nWords == 1: # only one word
                line += words[j] + " " * totalPadding
            else: # more than two words
                x = math.ceil(totalPadding / nBlank)
                b = nBlank * x - totalPadding
                a = nBlank - b
                for _ in range(a):
                    line += words[j] + ' ' * x
                    j += 1
                for _ in range(b):
                    line += words[j] + ' ' * (x - 1)
                    j += 1
                line += words[j]
            result.append(line)
        return result


def test():
    solution = Solution()

    assert solution.fullJustify([], 0) == []
    assert solution.fullJustify([""], 0) == [""]
    assert solution.fullJustify(["", "", "", ""], 0) == ["", "", "", ""]
    assert solution.fullJustify(["", "", " ", ""], 1) == [" ", " ", " "]
    assert solution.fullJustify(
        ["This", "is", "an", "example", "of", "text", "justification."],
        16
    ) == ["This    is    an",
          "example  of text",
          "justification.  "
         ]
    assert solution.fullJustify(
        ["This", "is", "an", "example", "of", "text", "justification.    "],
        16
    ) == []

    assert solution.fullJustify(["What","must","be","shall","be."], 12) == ["What must be","shall be.   "]

    print("self test passed")

if __name__ == '__main__':
    test()
