#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
401. Binary Watch

Total Accepted: 21304
Total Submissions: 48287
Difficulty: Easy
Contributors: Admin

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs
on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently
on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

Note:
1. The order of output does not matter.
2. The hour must not contain a leading zero, for example "01:00" is not valid, it
should be "1:00".
3. The minute must be consist of two digits and may contain a leading zero, for
example "10:2" is not valid, it should be "10:02".

==============================================================================================
SOLUTION

1. Backtracking.

The intermediate result can be represented by bits in a number.
Hour: _ _ _ _
Minute: _ _ _ _ _ _

Define state:
    State = (start index, #remaining ones)

Use an integer array of size 2 to store hours and minutes.

2. Brute force. Just to through all possible time combinations and filter...

'''

class Solution(object):

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return self.readBinaryWatchDFS(num)

    def readBinaryWatchDFS(self, num):
        def dfs(state):
            start, n = state
            if n == 0:
                result.append(list(time))
                return
            for i in range(start, 11 - n):
                div, mod = divmod(i, 6)
                time[1 - div] |= (1 << mod) # set bit to 1
                if time[0] <= 11 and time[1] <= 59:
                    dfs((i + 1, n - 1))
                time[1 - div] ^= (1 << mod) # reset bit to 0

        time = [0, 0]
        result = []
        dfs((0, num))
        result = list(map(lambda t: '%d:%02d' % (t[0], t[1]), sorted(result)))
        print(result)

        return result

def test():
    solution = Solution()

    assert solution.readBinaryWatch(0) == ["0:00"]
    assert solution.readBinaryWatch(1) == [
        "0:01", "0:02", "0:04",
        "0:08", "0:16", "0:32",
        "1:00", "2:00", "4:00",
        "8:00"
    ]
    assert solution.readBinaryWatch(8) == [
        "7:31", "7:47", "7:55",
        "7:59", "11:31", "11:47",
        "11:55", "11:59"
    ]

    print("self test passed")

if __name__ == '__main__':
    test()
