# 14. Longest Common Prefix
# Easy

# 4413

# 2288

# Add to List

# Share
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.

# S1

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ''
        pre = min(strs, key=len)
        for i, l in enumerate(pre):
            for s in strs:
                if s[i] != l:
                    return s[:i]
        return pre
      
# S2 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ''
        strs.sort()
        pre = min(len(strs[0]), len(strs[-1]))
        i = 0
        while i < pre and strs[0][i] == strs[-1][i]:
            i+=1
        return strs[0][:i]
        
