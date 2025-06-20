"""Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

For each point i, we iterate over every other point j > i and compute the slope between point i and j using (dy, dx) reduced by GCD to normalize slopes.

If two points are identical, we count them as duplicates.

For each unique slope, we count how many times it appears (i.e., how many points form the same slope with point i).

For every base point i, we find the maximum number of collinear points and add duplicates + 1 (the point itself) to get the total.

We track the global maximum over all base points.

We manually calculate the GCD (to handle negative values and edge cases like vertical/horizontal lines), and use the reduced slope as a key in a hash map.
"""

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        result = 1
        for i in range(len(points)):
            slopes = {}
            duplicates = 0
            cur_max = 0
            for j in range(i+1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue
                # Compute gcd manually (since LeetCode may not allow math.gcd)
                def calc_gcd(a, b):
                    while b:
                        a, b = b, a % b
                    return a
                g = calc_gcd(dy, dx)
                if g != 0:
                    dy //= g
                    dx //= g
                slope = (dy, dx)
                slopes[slope] = slopes.get(slope, 0) + 1
                cur_max = max(cur_max, slopes[slope])
            result = max(result, cur_max + duplicates + 1)
        return result