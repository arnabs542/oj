class Letter:

    def solve(self):
        n = int(raw_input())
        line = raw_input()
        arr = [int(i) for i in line.split()]
        num_opt = 0
        for i in xrange(n):
            if arr[i] == 1:
                break
        for j in xrange(n - 1, -1, -1):
            if arr[j] == 1:
                break
        for i in xrange(i, j + 1):
            if arr[i] == 1:
                num_opt += 1
            else:
                if arr[i - 1] == 1:
                    num_opt += 1
            # print i
        return num_opt

if __name__ == "__main__":
    print Letter().solve()
