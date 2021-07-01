# 680. Valid Palindrome II
# Easy

# 2819

# 180

# Add to List

# Share
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.

# Solution

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                new1 = s[l+1: r+1]
                new2 = s[l:r]
                return new1 == new1[::-1] or new2 == new2[::-1]
            l+=1
            r-=1
            
        return True
            
