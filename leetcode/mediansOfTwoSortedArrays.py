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

SOLUTION:
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
'''

class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
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
        half_length = (m + n + 1) // 2
        low, high = 0, m

        while low <= high:
            # XXX(done): binary search here
            mid = (low + high) >> 1
            i = mid
            j = half_length - i
            # conditions about median properties are satisfied
            # print(low, high, i, j, m, n)
            # XXX(done): edge cases when i=0,m; j=0,n
            if i > 0 and nums1[i - 1] > nums2[j]:
                # nums[i] is large, decrease it
                high = mid - 1
            elif i < m and nums1[i] < nums2[j - 1]:
                # nums[i] is small, decrease it
                low = mid + 1
            else:
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
    print('self tests passed!')

if __name__ == '__main__':
    test()
