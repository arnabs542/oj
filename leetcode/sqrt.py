'''
Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x.
'''

'''
Solution:
    binary search for k ,for which k*k<=x while (k+1)*(k+1)>x'
'''

class Solution:
    # @param x,an integer
    # @return an integer
    def sqrt(self,x):
        low = 0
        high = x
        while low <= high:
            k = (low + high)/2
            if k*k > x:
                high = k - 1
            elif (k+1)*(k+1) <= x:
                low = k + 1
            else:
                return k

if __name__ == "__main__":
    print Solution().sqrt(9)
    print Solution().sqrt(19)
    print Solution().sqrt(26)
