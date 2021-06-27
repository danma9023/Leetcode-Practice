# 204. Count Primes
# Easy

# 3392

# 823

# Add to List

# Share
# Count the number of prime numbers less than a non-negative number, n.

 

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0
 

# Constraints:

# 0 <= n <= 5 * 106


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n< 2:
            return 0
        ans = {}
        for i in range(2, int(sqrt(n))+1):
            if i not in ans:
                for m in range(i**2, n, i):
                    ans[m] = 1
        return n - len(ans)-2
