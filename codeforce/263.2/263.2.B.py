class Solution:

    def maxCoins(self):
        n, k = raw_input().split()
        n = int(n)
        k = int(k)
        cards = list(raw_input())
        dic = {}
        for i in cards:
            if dic.has_key(i):
                dic[i] += 1
            else:
                dic[i] = 1

        nums = dic.values()
        nums.sort(reverse=True)
        i = 0
        v = 0
        # print nums
        while i < k and len(nums) > 0:
            if nums[0] <= k - i:
                v += nums[0] * nums[0]
                i += nums.pop(0)
            else:
                n = k - i
                nums.pop(0)
                v += n * n
                i += n
        return v

if __name__ == "__main__":
    print Solution().maxCoins()
