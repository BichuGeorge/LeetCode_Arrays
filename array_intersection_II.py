"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Intuition
We need to find all common elements in two arrays, including duplicates.
So, we can count how many times each number appears in both arrays, and then take the minimum count for each common number.

Approach
We are iterating through hm1 and checking each element against hm2 to see how many times it appears in both arrays.
Then, we add that element to the result list based on the minimum number of times it appears in both.
"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = {}
        count2 = {}
        result = []
        for i in nums1:
            if i in count1:
                count1[i] += 1
            else:
                count1[i] = 1
        for i in nums2:
            if i in count2:
                count2[i] += 1
            else:
                count2[i] = 1
        for key,value in count1.items():
            if key in count2:
                result += min(value, count2[key])*[key]
        return result
        