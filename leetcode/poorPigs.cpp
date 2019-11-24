/**
 *
458. Poor Pigs
Hard

There are 1000 buckets, one and only one of them is poisonous, while the rest are filled with water. They all look identical. If a pig drinks the poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out which bucket is poisonous within one hour?

Answer this question, and write an algorithm for the general case.



General case:

If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out the poisonous bucket within p minutes? There is exactly one bucket with poison.



Note:

A pig can be allowed to drink simultaneously on as many buckets as one would like, and the feeding takes no time.
After a pig has instantly finished drinking buckets, there has to be a cool down time of m minutes. During this time, only observation is allowed and no feedings at all.
Any given bucket can be sampled an infinite number of times (by an unlimited number of pigs).

Accepted
17.1K
Submissions
36.7K

Hint 1: What if you only have one shot? Eg. 4 buckets, 15 mins to die, and 15 mins to test.
Hint 2: How many states can we generate with x pigs and T tests?
Hint 3: Find minimum x such that (T+1)^x >= N

SOLUTION
================================================================================

A brute force method is to use n pigs, each one corresponds to a bucket.
Or we can use one pig and test n times.

"Within p minutes" means we can test multiple rounds, means we can have fewer pigs
for test.
Then for each round, we can evenly divide the search space by two, a.k.a BINARY SEARCH.

Then for the last round, the problem is reduced to:
    Least number of pigs needed to test n buckets for just one round.

Approach 1 - binary search and binary representation - with x pigs and T tests.
---------
So we have x pigs, and how many states can it represent after one round of test?
2^x states for binary representation!

2^x >= N/(2^T)

Approach 2 - base k representation with x pigs and T tests.
----------
Represent buckets ID with k based numbers representation.
But since a pig has only two states (die or survive) after each round of feed,
how to carry out the tests with T based number representation?
How about the state of the round of pig dying?
We test each pig T times, then we have T+1 states:

0 survive
1 dies after 1st test
2 dies after 2nd test
...
T dies after T-th test

Then x pigs with T tests can represent (T+1)^x states!
But how to carry out the tests?

At i-th round of test:
- Represent the bucket id p with T+1 based number,
where p = a_1*(T+1)^0 + a_2*(T+1)^1 + ... + a_x*(T+1)^(x-1).
- For every bit, a_j feed pig j if and only if a_j is equal i.

Then after T rounds of tests, every a_j is known.

Objective:
    find minimum x such that (T+1)^x >= n.
So x = ceil(ln(n)/ln(T+1))

This is is optimal solution, since it divides the search space
with logarithm base (T+1) >= 2, which is binary search in approach 1.



 *
 */

#include <debug.hpp>

class Solution {
public:
    int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        int result = poorPigsKBasedRepresentation(buckets, minutesToDie, minutesToTest);

        cout << buckets << " " << minutesToDie << " " << minutesToTest << endl;

        return result;
    }

    int poorPigsKBasedRepresentation(int buckets, int minutesToDie, int minutesToTest) {
        int &n = buckets;
        int t = (minutesToTest / minutesToDie); // t tests
        return std::ceil(std::log(n)/std::log(t+1));
    }
};

int test() {
    Solution solution;
    int buckets, minutesToDie, minutesToTest;
    int result = 0;

    buckets = 1000;
    minutesToDie = 15;
    minutesToTest = 15;
    result = 10;
    assert(solution.poorPigs(buckets, minutesToDie, minutesToTest) == result);

    buckets = 1000;
    minutesToDie = 15;
    minutesToTest = 60;
    result = 5;
    assert(solution.poorPigs(buckets, minutesToDie, minutesToTest) == result);

    cout << "self test pased!" << endl;

    return 0;
}

int main(int argc, char *argv[])
{
    return test();
}
