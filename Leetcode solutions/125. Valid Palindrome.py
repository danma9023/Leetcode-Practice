# 125. Valid Palindrome
# Easy

# 2106

# 3952

# Add to List

# Share
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

# Solution 1

class Solution:
    def isPalindrome(self, s: str) -> bool:
        b, e  = 0, len(s)-1
        while b< e:
            while b < e and not s[b].isalnum():
                b += 1
            while b<e and not s[e].isalnum():
                e-=1
            
            if s[b].lower() != s[e].lower():
                return False
            b+=1 
            e-=1 
        return True
      
# Solution 2

class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''.join([x.lower() for x in s if x.isalnum()])
        return a == a[::-1]
