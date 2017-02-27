#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
412. Fizz Buzz Add to List

Total Accepted: 46210
Total Submissions: 79051
Difficulty: Easy
Contributors: Admin

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples
of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

==============================================================================================
SOLUTION


'''

class Solution(object):

    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.fizzBuzzLoop(n)

    def fizzBuzzLoop(self, n):
        return list(map(lambda x: str(x) if x % 3 and x % 5 else (
            "Fizz" if x % 5 else ("Buzz" if x % 3 else "FizzBuzz")), range(1, n + 1)))

def test():
    solution = Solution()

    assert solution.fizzBuzz(15) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ]

    print("self test passed")

if __name__ == '__main__':
    test()
