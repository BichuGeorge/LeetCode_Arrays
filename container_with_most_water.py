"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

First we will use a two-pointer approach to find the maximum area between two lines. The idea is to start with the widest container (the two ends of the array) and move towards the center, always keeping track of the maximum area found so far.
Then we will calculate the area between the two lines by taking the minimum height of the two lines and multiplying it by the distance between them. We will then update the maximum area if the current area is larger than the previous maximum.
Finally, we will return the maximum area found.
"""
from itertools import combinations
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea