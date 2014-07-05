class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        n = len(height)
        if n == 0:
            return 0
        elif n == 1:
            return height[0]

        i = 0, j = n - 1
        maxarea = min(height[i],height[j])*(j-i+1)
        while i < j:
            area = min(height[i],height[j])*(j-i+1)
            if height[i] < height[j]:
                i = i + 1
            else:
