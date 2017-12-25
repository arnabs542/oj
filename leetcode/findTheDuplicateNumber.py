#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
287. Find the Duplicate Number

Total Accepted: 49806
Total Submissions: 119477
Difficulty: Hard
Contributors: Admin

Given an array nums containing n + 1 integers where each integer is between 1 and n
(inclusive), prove that at least one duplicate number must exist. Assume that there
is only one duplicate number, find the duplicate one.

Note:
1. You must not modify the array (assume the array is read only).
2. You must use only constant, O(1) extra space.
3. Your runtime complexity should be less than O(n²).
4. There is only one duplicate number in the array, but it could be repeated more than once.

==============================================================================================
SOLUTION

To prove the existence of duplicate element, we can utilize pigeonhole principle.

1. Brute force method. For each number in [1, n], count its occurrence and return the one
with number of occurrence more than 1.

Complexity: O(N²), O(1)

2. Bucket
The previous solution doesn't incorporate the condition that all the integers are within
a specific RANGE [1, n]. With range defined, buckets come in handy!
But if we do it in a way like in Problem 'First Missing Positive', we need auxiliary space.

Complexity: O(N), O(N)

Can we make use of the condition that numbers are with in range [1, n] to reduce complexity?

3. Binary search
Binary search algorithm is trivial, but the key is to find the appropriate STATE to observe!

The COUNTING MODEL!

If there is not duplicates from 1 to m, then count of elements smaller than or equal to m
will be m.

Divide the array into two parts: [1, m], [m + 1, n].

Lemma
If the duplicate number is within range [1, m], then count of elements within range [1, m]
will be at least 1 + m.

Proof
Assume actual count of elements within range [1, m] is p < m + 1.

Since the array is divided into [1, m], [m + 1, n], and the duplicate is within [1, m].
So, there will be no duplicates within [m + 1, n], which can contain at most (n - m) elements.
Now, if actual count of elements within range [1, m] is p < m + 1, there will be
(n + 1 - p) > (n  + 1 - m - 1) > (n - m) elements within range [m + 1, n].

According to pigeonhole principle, there will be duplicate elements within range [m + 1, n],
which is contradict with the assumption!


With this lemme we can derive a search algorithm.
Assume there are k > (b - a + 1) elements within range [a, b]. Then divide the range [a, b],
into [a, c], [c + 1, b], where a <= c < b.
Then if the duplicate number is within range [a, c], there will be at most (b - c) elements
within range [c + 1, b], at least (k - b + c) elements within [a, c].
If the duplicate is within range [c + 1, b], there will be at most (c - a + 1) elements within
[a, c], and (k - c + a - 1) elements within [c + 1, b].

Now, it's time to do binary search.

Actually, the count compare statement can be changed to: count <= mid?


4. Two pointers - cycle detection

Cycle Detection model! Just like in linked list cycle detection.
Cycle detection or cycle finding is the algorithmic problem of finding a cycle in
a sequence of iterated function values(a function from some set X to itself).

The original statement that array is of length n + 1, containing values in [1, n], can be
reworded that array length is n, containing value in range [1, n -1] => [0, n - 2].
----------------------------------------------------------------------------------------------

Using pigeonhole principle, there will definitely be duplicate values.

Think of array as defining a FUNCTION MAPPING from DOMAIN onto RANGE of itself:
    the set {0, 1, ..., n - 1} onto itself {0, 1, ..., n - 2}.
This function is defined by f(i) = A[i], and x_{t+1} = f(x_{t}).
Given this setup, a duplicated value corresponds to a pair of indices i != j such that f(i) = f(j).

Moreover, note that since the array elements range from 0 to n - 2 inclusive, there is
no array index that contains n - 1 as a value.

Our challenge, therefore, is to find this pair (i, j).  Once we have it, we can easily find the
duplicated value by just picking f(i) = A[i].

But how are we to find this repeated value?  It turns out that this is a
well-studied problem in computer science called cycle detection.  The general
form of the problem is as follows.  We are given a iterated function f.  Define the
sequence x_i as

   x_0     = k       (for some k)
   x_1     = f(x_0)
   x_2     = f(f(x_0))
   ...
   x_{n+1} = f(x_n)

Assuming that f maps from a domain into itself, this function will have one
of three forms.
First, if the domain is INFINITE, then the sequence could be
infinitely long and nonrepeating.  For example, the function f(n) = n + 1 on
the integers has this property - no number is ever duplicated.

Second, the sequence could be a CLOSED LOOP, which means that there is some i so that
x_0 = x_i.  In this case, the sequence cycles through some fixed set of values indefinitely.

    x_0 -> x_1 -> ... x_i
     ^                 ^
     |                 |
     ------------------+

Finally, the sequence could be "RHO-SHAPED", where there exists no such x_i that x_i = x_0.
In this case, the sequence looks something like this:


    x_0 -> x_1 -> ... x_k -> x_{k+1} ... -> x_{k+j}
                       ^                       |
                       |                       |
                       +-----------------------+

That is, the sequence begins with a chain of elements that enters a cycle,
then cycles around indefinitely.  We'll denote the first element of the cycle
that is reached in the sequence the "entry" of the cycle.

----------------------------------------------------------------------------------------------
Lemma
If a iterated function maps from [0, n - 1], to [0, n -1], then there must be a cycle,
when the sequence length is equal to or greater than n.
Proof
Similar to pigeonhole principle.
1) If this iterated function has duplicate values, then there will be cycle, absolutely.
Such as [0, 0], or [1, 1].

2) If there is no duplicate values, then the range is the full set of [0, n - 1].
Prove by contradiction, assuming no cycle.
Then first n - 1 sequence, x_0, ..., x_{n - 2} must have no duplicates. And none of
them will be x_0, otherwise there will be duplicate values leading to cycle.
Obviously, first n - 1 non-repeating elements have used n - 1 values.
And x_0 isn't included, which means, all possible values except x_0 have already
appeared.
Now, for the last value x_{n - 1}, what value will it hold? There are only n unique values,
and first n - 1 elements in the sequence have claimed n - 1 element. Only one option x_0!
If f(x_{n-1}) = x_0, then we have a loop...

Such as [1, 0], when n = 2, giving closed loop.

----------------------------------------------------------------------------------------------
In this particular problem, sequence length is n, with value range corresponding to [0, n - 2].
So THERE MUST BE A CYCLE in the sequence!

There is no mapping to the end of the array, so the END OF ARRAY CAN NEVER BE PART OF THE CYCLE.

This indicates visiting from end of the array, such sequence is rho-shaped: forms a cycle
but not closed loop.

There will be a cycle when applying this iterated function given by array nums, and the sequence
will be rho-shaped if visiting from the end of array.
And, obviously, THE ENTRY OF THIS CYCLE IS THE DUPLICATE NUMBER, if visiting from end of array.
----------------------------------------------------------------------------------------------

Then, the end of array is the sequence start x_0, and we will find the cycle entry x_k.
Now, this problem, is similar to finding the cycle entry in linked list.

There is a famous algorithm due to Robert Floyd that, given a rho-shaped
sequence, finds the entry point of the cycle in linear time and using only
constant space.  This algorithm is often referred to as the "tortoise and hare" algorithm.

For the rest of analysis, refer to `linkedListCycleII.py`.

Complexity: O(N), O(1)


Reference
https://en.wikipedia.org/wiki/Cycle_detection
http://keithschwarz.com/interesting/code/?dir=find-duplicate


'''

class Solution(object):

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self._findDuplicateBinarySearch(nums)
        return self._findDuplicateTwoPointers(nums)

    def _findDuplicateBinarySearch(self, nums):
        if len(nums) <= 1: return

        n = len(nums) - 1 # 2
        total = n + 1
        low, high = 1, n # 1, 2

        while low < high:
            mid = (low + high) // 2 # 1
            count = 0
            # count now
            for num in nums:
                if low <= num <= mid:
                    count += 1 # 1
            # if count >= total - (high - mid):
            if count > mid:
                total = count #
                high = mid #
            else:
                total -= count #
                low = mid + 1 # 2
        return low

    def _findDuplicateTwoPointers(self, nums):
        # TODO: Two pointers
        n = len(nums)
        if n <= 1: return None
        slow = fast = nums[n - 1] # 2
        # slow = fast = n #
        while True:
            slow = nums[slow - 1] # 2
            fast = nums[nums[fast - 1] - 1] # 2
            if slow == fast: break # fast and slow pointers meet

        finder = nums[n - 1]
        while finder != slow: # finder and slow pointers meet
            finder = nums[finder - 1]
            slow = nums[slow - 1]
        return finder

def test():
    solution = Solution()

    assert(solution.findDuplicate([]) is None)
    assert(solution.findDuplicate([1]) is None)
    assert(solution.findDuplicate([1, 1]) == 1)
    assert(solution.findDuplicate([2, 2, 1]) == 2)
    assert(solution.findDuplicate([2, 2, 2]) == 2)
    assert(solution.findDuplicate([1, 2, 1]) == 1)
    assert(solution.findDuplicate([1, 1, 1]) == 1)
    assert(solution.findDuplicate([2, 2, 1, 3]) == 2)
    assert(solution.findDuplicate([2, 1, 3, 2]) == 2)

    print("self test passed")

if __name__ == '__main__':
    test()
