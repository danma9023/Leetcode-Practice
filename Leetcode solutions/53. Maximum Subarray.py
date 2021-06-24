# 53. Maximum Subarray
# Easy

# 12629

# 607

# Add to List

# Share
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -105 <= nums[i] <= 105
 

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
  
  
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i-1]>0:
                nums[i] += nums[i-1]
            max_sub = max(max_sub, nums[i])
        return max_sub
              
