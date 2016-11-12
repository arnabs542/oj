class Solution:
    # @param height, a list of integer
    # @return an integer

    # TODO: what's going on here?
    def largestRectangleArea(self, height):
        n = len(height)
        if n == 0:
            return 0
        elif n == 1:
            return height[0]

        i, j = 0, n - 1
        maxarea = min(height[i], height[j]) * (j - i + 1)
        while i < j:
            area = min(height[i], height[j]) * (j - i + 1)
            if height[i] < height[j]:
                i = i + 1
            else:
                pass
