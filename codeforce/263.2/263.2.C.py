# -*- encoding:utf-8 -*-
'''
Appleman and Toastman play a game. Initially Appleman gives one group of n numbers to the Toastman, then they start to complete the following tasks:

Each time Toastman gets a group of numbers, he sums up all the numbers and adds this sum to the score. Then he gives the group to the Appleman.
Each time Appleman gets a group consisting of a single number, he throws this group out. Each time Appleman gets a group consisting of more than one number, he splits the group into two non-empty groups (he can do it in any way) and gives each of them to Toastman.
After guys complete all the tasks they look at the score value. What is the maximum possible value of score they can get?

Input
The first line contains a single integer n (1 ≤ n ≤ 3·105). The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 106) — the initial group that is given to Toastman.

Output
Print a single integer — the largest possible score.

Sample test(s)
input
3
3 1 5
output
26
input
1
10
output
10
Note
Consider the following situation in the first example. Initially Toastman gets group [3, 1, 5] and adds 9 to the score, then he give the group to Appleman. Appleman splits group [3, 1, 5] into two groups: [3, 5] and [1]. Both of them should be given to Toastman. When Toastman receives group [1], he adds 1 to score and gives the group to Appleman (he will throw it out). When Toastman receives group [3, 5], he adds 8 to the score and gives the group to Appleman. Appleman splits [3, 5] in the only possible way: [5] and [3]. Then he gives both groups to Toastman. When Toastman receives [5], he adds 5 to the score and gives the group to Appleman (he will throws it out). When Toastman receives [3], he adds 3 to the score and gives the group to Appleman (he will throws it out). Finally Toastman have added 9 + 1 + 8 + 5 + 3 = 26 to the score. This is the optimal sequence of actions.
'''

'''
Solution:greedy,sorting

'''


class Solution:

    def __init__(self):
        self.sum = 0

    def solve(self):
        n = int(raw_input())
        a = [int(x) for x in raw_input().split()]
        a.sort()
        for i in xrange(n - 1):
            self.sum += (i + 2) * a[i]
        self.sum += n * a[n - 1]
        # self.divideAndConquer(a, 0, n - 1)
        return self.sum

    # def divideAndConquer(self, a, left, right):
        # if left > right:
            # return
        # n = right - left + 1
        # for i in range(left, right + 1):
            # self.sum += a[i]
        # if n == 1:
            # return
        # else:
            # md = (right + left) >> 1
            # if (md << 1) < right + left:
                # self.divideAndConquer(a, left, md)
                # self.divideAndConquer(a, md + 1, right)
            # else:
                # self.divideAndConquer(a, left, md - 1)
                # self.divideAndConquer(a, md, right)


if __name__ == "__main__":
    print Solution().solve()
