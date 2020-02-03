/**
 *
406. Queue Reconstruction by Height

Total Accepted: 8375
Total Submissions: 15557
Difficulty: Medium
Contributors: Admin

Suppose you have a random list of people standing in a queue. Each person is described
by a pair of integers (h, k), where h is the height of the person and k is the number
of people in front of this person who have a height greater than or equal to h. Write
an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


Hints:
What can you say about the position of the shortest person?
If the position of the shortest person is i, how many people would be in front of the shortest person?

Once you fix the position of the shortest person, what can you say about the position of the second shortest person?

================================================================================
SOLUTION

This problem has "larger than and before relation" involved.

1. Brute-force - permutation
Exhaust all permutations and verify.
Complexity is O(N!).
We can use height k to prune.

VALUE COMPARISON involved, consider the ORDERING / MONOTONICITY and EXTREMUM.
PROCESS THE HEIGHTS IN AN SORTED ORDER.

2. Sort and insert - backward, decreasing order

Process the list backward, in a descending height order.
Add the elements into the result array. Then each element already in the result
array is greater than or equal to the current one to insert.

In another word, for current (h, k), k is the position to insert it!

Complexity: O(n²), O(n)

3. Sort and insert - increasing order

We can sort the array with height first, and then insert in an increasing order.
For the first element, k is its index in output array.
An increasing order, empty slots indicates larger or equal elements coming after.
So, for each element (h, k), it should be placed at the kth EMPTY SLOT.

How about elements with same height?
Insert one with larger k first will be easier since same h with smaller k can
take empty slots before larger k!

And finding such empty slots takes O(n).

Complexity: O(N²), O(N²)

RANDOM ACCESS LIST INSERT OPTIMIZATION
--------------------------------------------------------------------------------
4. Sort and insert - increasing order - binary search - range sum as count
The above solution takes O(N) to find right empty slot position.
Can we use binary search to speed up?
To use binary search, we need to know how many positions are taken before,
for each index i in [0,n-1].
And, this is RANGE QUERY! We can count as sum, with range query data structure!
We can use a binary indexed tree to store range sum(count of take positions).

Then for each element, finding an empty slot to insert takes O(log²N).

Complexity: O(Nlog²N)

3. Optimizing inserting with order statistics tree

To enable O(logn) insert, we can augment a balanced binary search tree
as order statistics tree.

But the implementation is absolutely nontrivial.

Complexity: O(nlogn), O(n)

4. Sort and insert backward - SQUARE ROOT DECOMPOSITION

Inserting an element at a index in the list is O(N). And this why the "sort and insert"
takes O(N²).

How to optimize it?

Well, the trick is to SQUARE ROOT DECOMPOSE the list into blocks.
Inserting takes O(N) because there are average N elements to move when inserting.
But how to keep the buckets balanced?

Decompose given array into small chunks specifically of size sqrt(n)!

Complexity: O(n sqrtn) = O(n√n)

5. Divide and conquer - merge sort - number of larger elements before self

Complexity: O(nlogn)

 *
 */

#include <debug.hpp>

class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        vector<vector<int>> result;

        //result = reconstructQueueSortAndInsertForward(people);
        result = reconstructQueueSortAndInsertBackward(people);

        cout << people << " => " << result << endl;

        return result;
    }

    vector<vector<int>> reconstructQueueSortAndInsertForward(vector<vector<int>> &people) {
        sort(people.begin(), people.end(), [](vector<int> &a, vector<int> &b) {
                return (vector<int>{a[0], -a[1]} < vector<int>{b[0], -b[1]}); // {h, -k}
                });
        int n = people.size();
        vector<vector<int>> result(n, {}); // empty seats are equal or larger

        for (int i = 0; i < n; ++i) {
            int idx = 0;
            int k = people[i][1];
            for (int j = 0; j < n; ++j) {
                if (result[j].size()) continue; // slot taken are smaller larger
                if (k == 0) {
                    idx = j;
                    break;
                }
                --k;
            }
            result[idx] = people[i];
        }

        return result;
    }

    vector<vector<int>> reconstructQueueSortAndInsertBackward(vector<vector<int>> &people) {
        sort(people.begin(), people.end(), [](vector<int> &a, vector<int> b) {
                return vector<int>{a[0], -a[1]} < vector<int>{b[0], -b[1]};
                });

        int n = people.size();
        vector<vector<int>> result;
        for (int i = n - 1; i >= 0; --i) {
            int k = people[i][1];
            result.insert(result.begin() + k, people[i]);
        }

        return result;
    }

    vector<vector<int>> reconstructQueueSortAndInsertForwardSqrtDecomposition(vector<vector<int>> &people) {
        sort(people.begin(), people.end(), [](vector<int> &a, vector<int> b) {
                return vector<int>{a[0], -a[1]} < vector<int>{b[0], -b[1]};
                });

        int n = people.size();
        int m = std::ceil(std::sqrt(n));
        vector<vector<vector<int>>> buckets; // square root decomposed buckets
        buckets.reserve(n);
        buckets.resize(1);
        for (int i = n - 1; i >= 0; --i) {
            int k = people[i][1];
            auto rit = buckets.rend();

            rit = buckets.rend();
            int idx = k - (buckets.size() - 1) * m;

            if (rit->size() >= m) {
                buckets.push_back(vector<vector<int>>());
            }
            //result.insert(result.begin() + k, people[i]);
        }

        vector<vector<int>> result;
        return result;
    }

    vector<vector<int>> reconstructQueueSortAndInsertForwardRangeSumQueryBinarySearch(vector<vector<int>> &people) {
    }
};

int test() {
    Solution solution;
    vector<vector<int>> people;
    vector<vector<int>> output;

    people = {};
    output = {};
    assert (solution.reconstructQueue(people) == output);

    people = {{1, 0}};
    output = {{1, 0}};
    assert (solution.reconstructQueue(people) == output);

    people = {{1, 0}, {2, 0}};
    output = {{1, 0}, {2, 0}};
    assert (solution.reconstructQueue(people) == output);

    people = {{1, 1}, {2, 0}};
    output = {{2, 0}, {1, 1}};
    assert (solution.reconstructQueue(people) == output);

    people = {{7, 0}, {4, 4}, {7, 1}, {5, 0}, {6, 1}, {5, 2}};
    output = {{5, 0, }, {7, 0, }, {5, 2, }, {6, 1, }, {4, 4, }, {7, 1, }, };
    assert (solution.reconstructQueue(people) == output);

    cout << "self test passed" << endl;

    //# Generate a large test case and time it.
    //from bisect import bisect
    //from random import randint, shuffle
    //from timeit import timeit
    //n = 300000
    //heights = [randint(1, n) for _ in range(n)]
    //standing = []
    //people = []
    //for h in heights:
        //i = bisect(standing, -h)
        //standing.insert(i, -h)
        //people.append([h, i])
    //shuffle(people)
    //for solution in solution._reconstructQueueByHeightSortAndInsert, solution._reconstructQueueByHeightSortAndInsertWithSqrtDecomposition:
        //print(timeit(lambda: solution(people), number=1))
    return 0;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
