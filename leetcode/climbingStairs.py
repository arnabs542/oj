# -*- encoding:utf-8 -*-
'''
Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can
you climb to the top?

'''

'''
Solution:
    Fibonacci problem,Dynamic Programming.
    Best algorithm is to use matrix recurrence.
    F[n] = F[n-1] + F[n-2],F[0] = 1,F[1] = 1
'''


class Solution:
    # @param n,an interger
    # @return an integer

    def __init__(self):
        self.seed = [[1, 1]]
        self.transion_matrix = [[1, 1],
                                [1, 0]]

    def matrix_multiply(self, mat1, mat2):
        # print "{}*{}".format(mat1, mat2)
        m = len(mat1)
        if m == 0:
            return None
        n = len(mat1[0])

        if n != len(mat2):
            # print mat1, "*", mat2
            return None
        p = len(mat2[0])

        res = [[0 for i in range(p)] for j in range(m)]

         # print res

        for i in range(m):
            for j in range(p):
                for k in range(n):
                    res[i][j] += mat1[i][k] * mat2[k][j]

        # print "result matrix is :", res
        return res

    def matrix_power(self, mat, n):
        order = n
        m = len(mat)

        # identity matrix
        res = [[0 for i in range(m)] for j in range(m)]
        for i in range(m):
            res[i][i] = 1

        while order != 0:
            curr_res = mat
            k = 1
            while k <= order >> 1:
                k = k << 1
                curr_res = self.matrix_multiply(curr_res, curr_res)
            res = self.matrix_multiply(res, curr_res)
            order -= k

        return res

    def climbStairs(self, n):
        if n <= 2:
            return n
        trans = self.matrix_power(self.transion_matrix, n - 1)
        res = self.matrix_multiply(self.seed, trans)
        return res[0][0]

if __name__ == "__main__":
    # print Solution().climbStairs(0)
    # print Solution().climbStairs(2)
    print(Solution().climbStairs(3))
    print(Solution().climbStairs(8))
    print(Solution().climbStairs(50))
