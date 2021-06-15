# 34. Find First and Last Position of Element in Sorted Array
# Medium

# 5990

# 211

# Add to List

# Share
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.boundFinder(nums, target, True)
        if lb == -1:
            return[-1, -1]
        ub = self.boundFinder(nums, target, False)
        return[lb, ub]
      
    def boundFinder(self, nums:list, target:int, lower:True):
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                if lower:
                    if mid==start or nums[mid-1] < target:
                        return mid
                    else:
                        end = mid -1
                else:
                    if mid == end or nums[mid+1]>target:
                        return mid
                    else:
                        start = mid+1
            elif nums[mid]>target:
                end = mid-1
            else:
                start = mid +1
        return -1

