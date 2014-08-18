import sys


class Solution:

    def scalarProduct(self, v1, v2):
        v1.sort()
        v2.sort()
        n = len(v1)
        res = 0
        for i in range(n):
            res += v1[i] * v2[n - 1 - i]

        return res

    def getInput(self):
        # with open(sys.stdin) as fin:
        fin = sys.stdin
        line = fin.readline()
        n_cases = int(line)
        for i in range(n_cases):
            n = int(fin.readline())
            sv1 = fin.readline().split()
            sv2 = fin.readline().split()
            for j in range(n):
                sv1[j] = int(sv1[j])
                sv2[j] = int(sv2[j])

            print 'Case #{}: {}'.format(i + 1, self.scalarProduct(sv1, sv2))

if __name__ == "__main__":
    Solution().getInput()
