# 122. Best Time to Buy and Sell Stock II
# Easy

# 4495

# 2073

# Add to List

# Share
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e., max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 3 * 104
# 0 <= prices[i] <= 104


S1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro = 0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                max_pro += prices[i+1]-prices[i]
           
        return max_pro
        
S2

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0 
        i = 0
        
        while i < len(prices):
            while i < len(prices)-1 and prices[i] >= prices[i+1]:
                i+=1
            j = i + 1
            
            while j < len(prices) - 1 and prices[j] <= prices[j+1]:
                j += 1
            
            max_prof += prices[j]-prices[i] if j < len(prices) else 0
            i = j + 1
        return max_prof
