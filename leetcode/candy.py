# -*- encoding:utf-8 -*-
'''
Candy

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
'''

'''
Solution:Scan from start to end,divide the array into list of increasing
or decreasing sublist.
    In increasing list:increase candy by one iteratively.
    For decreasing list:Decrease one by one iteratively.
    candy[i]:the ith child's candy number.
    length[i]:the length of the longest decreasing list ending here.
    Then check the last element of the decreasing list,if it has candies
less than 1,the total candies needed should be increased by
    (1-candy[i])*(length[i]+1),length[i] is the longest strictly decreasing
    list.If candy[i] > 1,the candies needed should be decreased by
    (candy[i]-1)*length[i]

'''


class Solution:
    # @param ratings,a list of integer
    # @return an integer

    def candy(self, ratings):
        n = len(ratings)
        if n == 0:
            return 0
        candy = [1 for i in xrange(n)]
        length = [0 for i in xrange(n)]  # decreasing length ending here
        candies = 1
        for i in xrange(1, n):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
                candies += candy[i]
            elif ratings[i] == ratings[i - 1]:
                candy[i] = 1
                candies += candy[i]
                # length[i] = 0
            else:
                candy[i] = candy[i - 1] - 1
                length[i] = length[i - 1] + 1
                candies += candy[i]
                if i == n - 1 or ratings[i + 1] >= ratings[i]:
                    dif = 1 - candy[i]
                    candy[i] = 1
                    if dif > 0:
                        candies += dif * (length[i] + 1)
                    else:
                        candies += dif * (length[i])
        # print candy
        return candies

if __name__ == "__main__":
    # print Solution().candy([1, 1, 1, 1])
    # print Solution().candy([1, 2, 3, 4, 4, 3, 2, 2, 1])
    print Solution().candy([1, 0, 2])
    print Solution().candy([4, 2, 3, 4, 1])
