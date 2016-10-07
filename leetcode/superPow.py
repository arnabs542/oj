'''
372. Super Pow

Total Accepted: 8672
Total Submissions: 27002
Difficulty: Medium

Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example1:

  a = 2
  b = [3]

  Result: 8
Example2:

  a = 2
  b = [1,0]

  Result: 1024

SOLUTION:
    This is a similar problem to pow(x, n), we can decompose the order of power to a sum of
power based on n(2 for binary, 10 for decimal). Latex formula:

    \because b = \sum_{k = 0}^{m-1} b_k \times 10^{k} \\
    \therefore a ^ b = \prod_{k = 0}^{m-1} a^{b_k \times 10^k} \\
          = \prod_{k = 0}^{m-1} {(a^{10^k})} ^ {b_k}
    n1*n2 % 1337 == (n1 % 1337)\times(n2 % 1337) % 1337

  For modular operation, we could just keep the remainder of each factor in the product. The
rule applies to power arithmetic too.
  During the iteration we just need to keep track of $r = a^{10^k} % 1337$ and
$ar = (a^{10^k})^{b_k} % 1337$
'''

class Solution(object):

    def superPowRecursive(self, a, b):
        '''
        n1*n2 % 1337 == (n1 % 1337)*(n2 % 1337) % 1337
        If b = m*10 + d, we have a**b == (a**d)*(a**10)**m

        125ms, 65.77%, faster than iterative ones
        '''
        if not b:
            return 1
        return pow(a, b.pop(), 1337) * \
            self.superPowRecursive(pow(a, 10, 1337), b) % 1337
        pass

    def superPowIterative(self, a, b):
        """
        :type a: int
        :rtype: int
        """

        bk = b[-1]
        r = a % 1337
        ar = a ** bk % 1337

        for bk in reversed(b[:-1]):
            ar_old = ar
            r = r ** 10 % 1337  # the recursive formula
            ar = r ** bk % 1337
            if not ar:
                return 0
            ar = ar * ar_old % 1337
        return ar

    def superPow(self, a, b):
        return self.superPowIterative(a, b)

def test():
    solution = Solution()
    print(solution.superPow(2, [3]))
    print(solution.superPow(2, [1, 0]))
    print(solution.superPowRecursive(2, [1, 0]))

if __name__ == '__main__':
    test()
