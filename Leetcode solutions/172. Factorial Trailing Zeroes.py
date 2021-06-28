# 172. Factorial Trailing Zeroes
# Easy

# 1412

# 1442

# Add to List

# Share
# Given an integer n, return the number of trailing zeroes in n!.

# Follow up: Could you write a solution that works in logarithmic time complexity?

 

# Example 1:

# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:

# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# Example 3:

# Input: n = 0
# Output: 0
 

# Constraints:

# 0 <= n <= 104


# S1
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ini = 1
        for i in range(1, n+1):
            ini *= i
        cnt = 0
        while ini % 10 ==0:
            cnt += 1
            ini //= 10
        return cnt

# S2

class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        for i in range(5, n+1, 5):
            while i % 5 == 0:
                cnt +=1
                i //= 5
        return cnt
            
