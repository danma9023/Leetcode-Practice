# 70. Climbing Stairs
# Easy

# 6978

# 217

# Add to List

# Share
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45

# S1

class Solution:
    def climbStairs(self, n: int) -> int:
        curr = 1 
        pre = 1

        for i in range(1, n):
            summ = curr + pre
            pre = curr
            curr =summ
        return curr
      
# S2

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n
        ans = [1, 1]
        for i in range(2, n+1):
            ans.append(ans[i-1]+ans[i-2])
        return ans[n]
