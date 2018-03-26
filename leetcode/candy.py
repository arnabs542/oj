# -*- encoding:utf-8 -*-
'''
135. Candy

Total Accepted: 61755
Total Submissions: 259593
Difficulty: Hard
Contributors: Admin

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

==============================================================================================
Solution

VALUE COMPARISON involved, analyze the ORDERING / MONOTONICITY and EXTREMUM.

Divide the array into groups of MONOTONIC (increasing or decreasing) subarray. And we
consider those EXTREMA.

For ascending subarray, increase #candy by 1 for each element. And for decreasing sequence,
decrease #candy by 1 sequentially. For a equal element with previous one, assign 1 candy.

1. One pass

Notation
    candy[i]:the ith child's candy number.
    len_desc[i]:the length of the longest descending subarray ending here.

Scan the array from left to right, for non-descending sequences, just carry out the normal
strategy above, for descending subarray, we need to take care of the last element(
local minimum), since it may have #candy less or more than 1.
    1) If it has #candy less than 1, the total candies needed should be increased by
(1 - candy[i]) * (length[i] + 1).
    2) If candy[i] > 1,the candies needed should be increased by (1 - candy[i]) * length[i].
We can't reduce the #candy of a previous local maximum since it has children with lower
rating before.

Time complexity: O(N), space complexity: O(N) or O(1).

2. Two passes
Forward and backward scanning.

################################################################################
FOLLOW UP

1. Can this be solved with mathematical optimization (convex optimization)?
Denote ratings vector as r, let vector x be candies assigned to each children.

Then the objective is to:
    minimize \sum{x}
    subject to: x >= 1(elementwise inequality),
                (x_i - x_{i+1})*(r_i - r_{i+1}) >= 0 ?

'''


class Solution(object):

    def candy(self, ratings: list):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # return self.candyOnePass(ratings)
        return self.candyOnePassOpt(ratings)

    def candyOnePassOpt(self, ratings: list) -> int:
        candy, candies, len_desc = 0, 0, 0
        for i, _ in enumerate(ratings):
            if i == 0 or ratings[i] > ratings[i - 1]:
                candy += 1
                candies += candy
            elif ratings[i] == ratings[i - 1]:
                candy = 1
                candies += candy
            else: # deal with descending sequence
                candy -= 1
                candies += candy
                len_desc = max(2, len_desc + 1)
                if i == len(ratings) - 1 or ratings[i + 1] >= ratings[i]:
                    # local minimum: add difference
                    diff = 1 - candy
                    if diff > 0:
                        candies += diff * len_desc
                    else:
                        candies += diff * (len_desc - 1)
                    candy, len_desc = 1, 0

        print(candies)
        return candies

    def candyOnePass(self, ratings: list) -> int:
        candy = [0 for i in range(len(ratings) + 1)]
        len_desc = [0 for i in range(len(ratings) + 1)]  # decreasing length ending here
        candies = 0
        for i in range(1, len(ratings) + 1):
            if i == 1 or ratings[i - 1] > ratings[i - 2]:
                candy[i] = candy[i - 1] + 1
                candies += candy[i]
            elif ratings[i - 1] == ratings[i - 2]:
                candy[i] = 1
                candies += candy[i]
            else:
                # same complex logic in one place
                candy[i] = candy[i - 1] - 1
                len_desc[i] = len_desc[i - 1] + 1
                candies += candy[i]
                # check local minimum
                if i == len(ratings) or ratings[i] >= ratings[i - 1]:
                    diff = 1 - candy[i]
                    candy[i] = 1
                    if diff > 0:
                        candies += diff * (len_desc[i] + 1)
                    else:
                        candies += diff * (len_desc[i])
        print(candy, candies)
        return candies

    def candyTwoPass(self, ratings: list) -> int:
        # TODO: forward and backward scanning
        pass

    # TODO: mathematical optimization

def test():
    assert Solution().candy([]) == 0
    assert Solution().candy([0]) == 1
    assert Solution().candy([1, 1, 1, 1]) == 4
    assert Solution().candy([1, 2, 3, 4, 4, 3, 2, 2, 1]) == 19
    assert Solution().candy([1, 0, 2]) == 5
    assert Solution().candy([4, 2, 3, 4, 1]) == 9

    print('self test passed')

if __name__ == "__main__":
    test()
