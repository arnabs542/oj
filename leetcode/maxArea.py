'''
Container With Most Water

Given n non-negative integers a1, a2, ..., an, where each
represents a point at coordinate (i, ai). n vertical lines are drawn
such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container,
such that the container contains the most water.

Note: You may not slant the container.
'''

class Solution:
    # @param height,integer list
    # @return an integer
    def maxArea(self,height):
        i = 0
        j = len(height) - 1
        maxa = 0
        while i < j:
            if height[i] < height [j]:
                area = height[i]*(j-i)
                i = i + 1
            else:
                area = height[j]*(j-i)
                j = j - 1

            if area > maxa:
                maxa = area

        return maxa

