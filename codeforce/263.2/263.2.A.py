# -*- coding:utf-8 -*-

'''
                    A. Appleman and Easy Task
Toastman came up with a very easy task. He gives it to Appleman, but Appleman doesn't know how to solve it. Can you help him?

Given a n × n checkerboard. Each cell of the board has either character 'x', or character 'o'. Is it true that each cell of the board has even number of adjacent cells with 'o'? Two cells of the board are adjacent if they share a side.

Input
The first line contains an integer n (1 ≤ n ≤ 100). Then n lines follow containing the description of the checkerboard. Each of them contains n characters (either 'x' or 'o') without spaces.

Output
Print "YES" or "NO" (without the quotes) depending on the answer to the problem.

Sample test(s)
input
3
xxo
xox
oxx
output
YES
input
4
xxxo
xoxo
oxox
xxxx
output
NO

'''


class Solution:

    def input(self):
        n = int(raw_input())
        board = [['O' for i in range(n + 2)]for j in range(n + 2)]
        for i in range(n):
            line = list(raw_input())
            board[i + 1][1:n + 1] = line

        if self.solve(board):
            print "YES"
        else:
            print "NO"

    def solve(self, board):
        N = len(board)
        # for i in range(N):
            # print board[i]
        n = N - 2
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                num = 0
                if board[i - 1][j] == 'o':
                    num += 1
                if board[i + 1][j] == 'o':
                    num += 1
                if board[i][j - 1] == 'o':
                    num += 1
                if board[i][j + 1] == 'o':
                    num += 1
                if num % 2 != 0:
                    # print board[i]
                    return False
        return True

if __name__ == "__main__":
    Solution().input()
