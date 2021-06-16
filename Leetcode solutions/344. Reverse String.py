# 344. Reverse String
# Easy

# 2527

# 792

# Add to List

# Share
# Write a function that reverses a string. The input string is given as an array of characters s.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is a printable ascii character.

# Solution 1
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

# Solution 2
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
            
