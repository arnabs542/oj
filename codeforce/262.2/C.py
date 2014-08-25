# -*- coding:utf-8 -*-

'''
C. Present
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Little beaver is a beginner programmer, so informatics is his favorite subject. Soon his informatics teacher is going to have a birthday and the beaver has decided to prepare a present for her. He planted n flowers in a row on his windowsill and started waiting for them to grow. However, after some time the beaver noticed that the flowers stopped growing. The beaver thinks it is bad manners to present little flowers. So he decided to come up with some solutions.

There are m days left to the birthday. The height of the i-th flower (assume that the flowers in the row are numbered from 1 to n from left to right) is equal to ai at the moment. At each of the remaining m days the beaver can take a special watering and water w contiguous flowers (he can do that only once at a day). At that each watered flower grows by one height unit on that day. The beaver wants the height of the smallest flower be as large as possible in the end. What maximum height of the smallest flower can he get?

Input
The first line contains space-separated integers n, m and w (1 ≤ w ≤ n ≤ 105; 1 ≤ m ≤ 105). The second line contains space-separated integers a1, a2, ..., an (1 ≤ ai ≤ 109).

Output
Print a single integer — the maximum final height of the smallest flower.

Sample test(s)
input
6 2 3
2 2 2 2 1 1
output
2
input
2 5 1
5 8
output
9
Note
In the first sample beaver can water the last 3 flowers at the first day. On the next day he may not to water flowers at all. In the end he will get the following heights: [2, 2, 2, 3, 2, 2]. The smallest flower has height equal to 2. It's impossible to get height 3 in this test.
'''

'''
Editorial:
    Note,that answer is positive integer not greater than 109 + 105. Using
binary search on answer, we will find answer. Really, we can check in O(n)
if some height is achievable. We go from left to right. For current flower
we calculate how much times it need to be watered to stand not lower than
checking value. If cuurent flower need to be watered for h times, we will
star h segments in current flower. We would keep array, in which st[i] —
number of segments, which starts in i-th flower. Also, we will keep
variable, in which we will keep number of segments, which cover current
flower. This variable could be updated at O(1). Really, to get new value
we just need to subtract st[i  -  w], and, if we create new segments, to
add st[i]

Also, it can be proved that simple greedy algorithm works. At every of m
iterations we can find the leftmost flower with the smallest height and
water the segment, which begins in it. Primitive realisation works at
O(nm), so you need to use data structure, which can add on segment and
find minimum at segment. For example, you can use segment tree with lazy
updation or sqrt-decomposition. Such solutions works longer, but faster
than TL

Prove: Consider any optimal sequence of moves (using which max. answer
reachs). Consider initially the leftmost smallest flower, and suppose all
segments which covers it.(suppose, there are at least 1 segment, because
else answer is initial height of this flower, so we can put a segment to
start in this flower, and answer would not change). Suppose that there are
no segments, which starts from current flower. Consider the rightests of
segments.(If there are more than one, than any of them). Than, we can move
this segment to start in the initially leftmost smallest flower, and the
answer would not change. Really, flowers, which earlier was at this
segments were higher, than leftmost smallest, and were watered not least
times. So, after we moved the answer had not decreased. So, new sequence
is also optimal. So, there is sequence of moves, which consists the
segment, which starts at the initially leftmost smallest flower. So, let
use this. Similary to other of m days, and it would be optimally.
    '''
'''
BINARY SEARCH,GREEDY
'''

import sys


def input():
    Read = lambda: map(int, raw_input().split())
    (n, m, w), a = Read(), Read()
    l, st = min(a), [0] * n
    r = l + m

    while l <= r:
        h = l + r >> 1
        stcurr = 0
        moves = 0
        st = [0] * n
        for i in range(n):
            if i - w >= 0:
                stcurr = stcurr - st[i - w]

            # if a[i] + stcurr < h:
            # must initialize array st in each while loop
            st[i] = max(h - a[i] - stcurr, 0)
            stcurr += st[i]
            moves += st[i]

            if moves > m:
                r = h - 1
                break
        else:
            l = h + 1

    return r


if __name__ == "__main__":
    print input()
