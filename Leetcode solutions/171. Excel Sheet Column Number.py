# 171. Excel Sheet Column Number
# Easy

# 1803

# 210

# Add to List

# Share
# Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: columnTitle = "A"
# Output: 1
# Example 2:

# Input: columnTitle = "AB"
# Output: 28
# Example 3:

# Input: columnTitle = "ZY"
# Output: 701
# Example 4:

# Input: columnTitle = "FXSHRXW"
# Output: 2147483647
 

# Constraints:

# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"].

# S1

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in range(len(columnTitle)):
            res = res*26
            res += (ord(columnTitle[i])-ord('A')+1)
                          
        return res
      
# S2

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        map = {chr(i+65):i+1 for i in range(26)}
        n= len(columnTitle)
        for i in reversed(range(n)):
                          curr_char = columnTitle[n-1-i]
                          res += map[curr_char] * (26**i)
                          
        return res
                        
                         
