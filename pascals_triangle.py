"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1], [1,1]]
        else:
            triangle = []
            triangle= [[1], [1,1]]
            i=2
            while i < numRows:
                p_tr = [1]
                p_tr_middle = [triangle[i-1][j] + triangle[i-1][j+1] for j in range(i-1)]
                p_tr_final = p_tr + p_tr_middle + [1]
                triangle.append(p_tr_final)
                i+=1
            return triangle