#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
393. UTF-8 Validation

Total Accepted: 10530
Total Submissions: 29839
Difficulty: Medium
Contributors: Admin

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed
by n-1 bytes with most significant 2 bits being 10.

This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

Note:
The input is an array of integers. Only the least significant 8 bits of each integer
is used to store the data. This means each integer represents only 1 byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.

==============================================================================================
SOLUTION

This problem involves many states, indicating that maybe a Finite State Machine can make the
STATE TRANSITION relation clear.

Define state: (iob, n).
Where iob denotes the Beginning, inside, (where outside is meaningless). And n is the remaining
number of bytes of the current possible UTF8 character, including the current byte.

Then we can construct the State Transition Relation according to each byte's leading bits.

Leading bits:
    0: n = 1
    110: n = 2
    1110: n = 3
    11110: n = 4
    10: Invalid after (n = 1)

State Transition Matrix kernel K is as follows.
K[0] = {0: 1, 0b110: 2, 0b1110: 3, 0b11110: 4}
K[1] = {0:1, 0b110: 2, 0b1110: 3, 0b11110: 4}
K[2] = {10: 1}
K[3] = {10: 2}
K[4] = {10: 3}

And of course, the state machine stuff can be simplified to if-else statements here.

'''

class Solution(object):

    masks = {
        0b10000000: 0,
        0b11000000: 0b10000000,
        0b11100000: 0b11000000,
        0b11110000: 0b11100000,
        0b11111000: 0b11110000,
    }

    kernel = [
        {0: 1, 0b11000000: 2, 0b11100000: 3, 0b11110000: 4},  # 0
        {0: 1, 0b11000000: 2, 0b11100000: 3, 0b11110000: 4},  # 1
        {0b10000000: 1},  # 2
        {0b10000000: 2},  # 3
        {0b10000000: 3},  # 4
    ]

    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        return self.validUtf8FSM(data)

    def beginWith(self, a):
        for mask, prefix in self.masks.items():
            if a & mask == prefix:
                return prefix
        return -1

    def validUtf8FSM(self, data):
        state = 0
        for num in data:
            if num >= 256:
                return False

            prefix = self.beginWith(num)
            print("state", state, "number", bin(num), "prefix", bin(prefix))
            state = self.kernel[state].get(prefix)
            if state is None:
                return False

        return state <= 1

def test():
    solution = Solution()

    assert solution.validUtf8([])
    assert solution.validUtf8([1, 1, 1])
    assert solution.validUtf8([197, 130, 1])
    assert not solution.validUtf8([235, 140, 4])
    assert not solution.validUtf8([297, 130, 1])
    assert not solution.validUtf8([237])

    print('self test passed')

if __name__ == '__main__':
    test()
