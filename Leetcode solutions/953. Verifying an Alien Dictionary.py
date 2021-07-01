# 953. Verifying an Alien Dictionary
# Easy

# 1868

# 744

# Add to List

# Share
# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.

# Solution
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict ={}
        for i, w in enumerate(order):
            order_dict[w] = i
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False 
                # '=' because j starts from 0 
                if words[i][j] != words[i+1][j]:
                    if order_dict[words[i][j]] >order_dict[words[i+1][j]]:
                        return False
                    break
# jump out of the for j loop to compare next letter of words[i] and words[i+1]
        return True

