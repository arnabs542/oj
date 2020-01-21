'''
4. Median of Two Sorted Arrays

Total Accepted: 119892
Total Submissions: 595820
Difficulty: Hard

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

[1, 4, 7]
[2, 3, 9]
[2, 3, 9]
[1, 7]

SOLUTION
================================================================================

1. Brute force - sort

Complexity:
O((M+N)log(M+N))

Brute force count (m+n)/2 numbers in a way like merge sort.
Complexity: O(M+N).

2. Brute force - binary search verify
Exhaust all numbers in nums1, find lower bound in nums2. Then verify whether that
evenly partitions two arrays.
If not found, repeat to exhaust all numbers in nums2.

Complexity:
O(MlogN+NlogM)

3. Brute force optimization - use binary search to exhaust all numbers in nums1/nums2

Complexity:
O(logMxlogN)

--------------------------------------------------------------------------------
Sorted array, divide and conquer!

How do we get a median from two sorted arrays?
The median can be determined by kth number of the sorted array, where
k = ceil((m+n)/2), or the average with its neighbour. Given one array,
median may depend on two numbers(if array size is even).
Now given two arrays, median may depend on four numbers.

And such kth element must be a partition point that divides two arrays into parts:
First k elements, and last (m+n-k) elements, where first part is no smaller than
second part.
And k numbers can be decomposed to:
    k = k+0=k-1+1=...= 0+k = i + j.
First k numbers can be composed of i numbers from first array, and j numbers from
second array.
And we need to determine the value of i and j(j = k-i).
And two arrays are all sorted, use a divide and conquer technique: binary search!

Keep track of (
    i: number of elements from first array,
    j: number of elements from second array,
    ), where i+j = k.

State transition in binary search:
...

--------------------------------------------------------------------------------

4. Single level of binary search
    For logarithm time complexity, we may adopt BINARY SEARCH related algorithm to DIVIDE and CONQUER.
    In statistics, the median is used for dividing a set into two EQUAL LENGTH
subsets, that one subset is always greater than the other

    Search for two positions `i`, `j` that can divide the two sorted array by
TWO ALMOST EVEN HALVES .

Cut A into two parts at a position i:
      left_A             |        right_A
A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
where i is in [0, m]

Cut B into two parts at a random position j:
      left_B             |        right_B
B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

Put left_A and left_B into one set, and put right_A and right_B into another set. Let's name them left_part and right_part :
      left_part          |        right_part
A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

Then these conditions must be satisfied:
    1) len(left_part) == len(right_part) plus-minus 1
    2) left_part <= right_part <====> max(left_part) <= min(right_part)
if but and only if:
    (1) i + j == (m - i) + (n - j) (or: m - i + n - j + 1) == half_length plus-minus 1
        if n >= m, we just need to set: i = 0 ~ m, j = (m + n + 1)/2 - i
    (2) B[j-1] <= A[i] and A[i-1] <= B[j]
Then we only procedure is a binary search:
    low, high = 0, m; mid = (low+high)/2
    Binarily searching i in [low, high], to find such index `i = (low+high)/2` that:
    B[j-1] <= A[i] and A[i-1] <= B[j], ( where j = (m + n + 1)/2 - i )
    if B[j-1] > A[i]: then i is too small, increase it by adjust the range low = mid + 1
    else if A[i-1] > B[j]: then i is too large, decrease it, high = mid - 1

Consider the edges cases where i=0,i=m,j=0,j=n so A[i-1],B[j-1],A[i],B[j] may not exist.
For example, if i=0, then A[i-1] doesn't exist, then we don't need to check A[i-1] <= B[j].

Note that, if we constrain `i + j = k`, then this algorithm could generalize to find kth element.
The time complexity is O(log(min(m, n))).

FOLLOW UP
================================================================================

1. kth largest given two sorted array
1) merge sort: O(m+n). Quick select O(m+n).
2) Divide and conquer
Decompose k into k = i+j, and perform binary search for i.
Complexity: O(log(min(m,n,k)))

2. Find median in in row wise sorted matrix
1) Brute force: sort O(MNlogMN), or use heap to find kth.
2) Divide and conquer like above, decompose k = p1+p2+...+pm.
But this is a m-tuple, searching for such state is complex.

3) VALUE SPACE SEARCH AND VERIFY: search in the VALUE SPACE and VERIFY!
Such matrix has MN values, and we can search in the value space and verify
whether there are k numbers in the matrix no larger than it.

Complexity: O(MlogNlogMN) = O(32MlogMN)

4) HEAP: Maintain a min heap of size m, containing (i, j) coordinates from each row.
The process is like merge sort comparing to retrieve the minimal so far.

Complexity: O((m+n)/2logM)
To find kth element in row wise sorted matrix, pop and insert for k times.
Complexity: O(klogM)




'''

class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        result = self.findMedianSortedArraysDivideAndConquerForK(nums1, nums2)

        print(nums1, nums2, result)

        return result

    def findMedianSortedArraysDivideAndConquerForK(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            # return self.findMedianSortedArrays(nums2, nums1)
            m, n = n, m
            nums1, nums2 = nums2, nums1
        k = (m + n + 1) // 2 # ceil((m+n)/2)
        low, high = 0, m # m <= k, [0, m], m-k ∈ [,]

        while low <= high:
            i = (low + high) >> 1
            j = k - i
            # conditions about median properties are satisfied
            # print(low, high, i, j, m, n)
            # XXX(done): edge cases when i=0,m; j=0,n
            if i > 0 and nums1[i - 1] > nums2[j]: # too many numbers from first array
                high = i - 1
            elif i < m and nums2[j - 1] > nums1[i]: # j > 0 and nums1[i] < nums2[j-1]
                # too few numbers from second array
                low = i + 1
            else: # found (i+j=k)th element, compute median
                # matching i and j
                if i == 0:
                    left_max = nums2[j - 1]
                elif j == 0:
                    left_max = nums1[i - 1]
                else:
                    left_max = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2:
                    # total number is odd
                    return left_max

                # even number of total elements
                if i == m:
                    right_min = nums2[j]
                elif j == n:
                    right_min = nums1[i]
                else:
                    right_min = min((nums1[i], nums2[j]))

                return 0.5 * (left_max + right_min)

    def findKthSortedArrays(self, nums1, nums2, k):
        m, n = len(nums1), len(nums2)
        result = float('-inf')
        if not 0 < k <= m + n: return float('-inf')
        low, high = 0, min(k, m) # [0, min(m,k)]
        while low <= high:
            i = (low + high) >> 1 # binary search divide evenly
            j = k - i
            if j > n: # too few from first array
                low = i + 1
            elif 0<=i< m and n>=j>=1 and nums2[j-1] > nums1[i]: # too few from first array
                low = i + 1 # go right
            elif m>=i>=1 and 0<=j<n and nums1[i-1] > nums2[j]: # too many from first array
                high = i - 1 # go left
            else:
                # print('found', i, j, k)
                result = max(nums1[i-1] if i >= 1 else float('-inf'),
                           nums2[j-1] if j >= 1 else float('-inf')
                           )
                break
        print(nums1, nums2, k, result)
        return result

def test():
    solution = Solution()
    # edge cases
    assert solution.findMedianSortedArrays([], [1]) == 1

    assert solution.findMedianSortedArrays([1, 3], [2]) == 2
    assert solution.findMedianSortedArrays([1, 2], [3]) == 2
    assert solution.findMedianSortedArrays([1, 3], [7]) == 3
    assert solution.findMedianSortedArrays([1, 4], [2, 3]) == 2.5
    assert solution.findMedianSortedArrays([1, 3], [2, 4]) == 2.5
    assert solution.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert solution.findMedianSortedArrays([7], [1, 3]) == 3
    assert solution.findMedianSortedArrays([1, 3, 4], [7]) == 3.5
    assert solution.findMedianSortedArrays([1, 3, 4], [7, 9, 10]) == 5.5

    nums1 = [1, 3, 4]
    nums2 = [7, 9, 10]
    nums = list(sorted(nums1+nums2))
    for i, e in enumerate(nums):
        assert solution.findKthSortedArrays(nums1, nums2, i+1) == e

    nums1 = []
    nums2 = [7, 9, 10]
    nums = list(sorted(nums1+nums2))
    for i, e in enumerate(nums):
        assert solution.findKthSortedArrays(nums1, nums2, i+1) == e

    print('self tests passed!')

if __name__ == '__main__':
    test()
