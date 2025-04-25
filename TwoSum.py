# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Initialize a dictionary to store the elements and its indices.
        index_dict = {}
        for i, num in enumerate(nums):
            # target minus current element should be the other element.
            difference = target - num
            # checks if other element is there in the dictionary
            if difference in index_dict:
                # if yes, we found the answer
                return [i, index_dict[difference]]
            else:
                # else we add the current element and its index to the dictionary
                index_dict[num] = i
        return None