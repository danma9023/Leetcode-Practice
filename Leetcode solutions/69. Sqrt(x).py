# 69. Sqrt(x)
# Easy

# 2155

# 2452

# Add to List

# Share
# Given a non-negative integer x, compute and return the square root of x.

# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

# Example 1:

# Input: x = 4
# Output: 2
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
 

# Constraints:

# 0 <= x <= 231 - 1

S1
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        left = int(e**(.5*log(x)))
        right = left +1
        return left if right**2 >x else right
        
S2
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l<=r:
            mid = (l+r)//2
            if mid**2 == x:
                return mid
            elif mid**2>x:
                r = mid -1
            else:
                l = mid +1
        return r
