class Solution:

    def __init__(self):
        self.sum = 0

    def solve(self):
        n = int(raw_input())
        a = [int(x) for x in raw_input().split()]
        a.sort()
        self.divideAndConquer(a, 0, n - 1)
        return self.sum

    def divideAndConquer(self, a, left, right):
        n = right - left + 1
        for i in range(left, right + 1):
            self.sum += a[i]
        if n == 1:
            return
        else:
            md = (right + left) >> 1
            if (md << 1) < right + left:
                self.divideAndConquer(a, left, md)
                self.divideAndConquer(a, md + 1, right)
            else:
                self.divideAndConquer(a, left, md - 1)
                self.divideAndConquer(a, md, right)


if __name__ == "__main__":
    print Solution().solve()
