# 332. Reconstruct Itinerary
# Medium

# 2855

# 1303

# Add to List

# Share
# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

 

# Example 1:


# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]
# Example 2:


# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
 

# Constraints:

# 1 <= tickets.length <= 300
# tickets[i].length == 2
# fromi.length == 3
# toi.length == 3
# fromi and toi consist of uppercase English letters.
# fromi != toi

# Solution
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.dic = collections.defaultdict(list)
        for t in tickets:
            ori, des = t[0], t[1]
            self.dic[ori].append(des)
        for o, d in self.dic.items():
            d.sort(reverse=True)
        
        self.res=[]
        self.DFS('JFK')
        return self.res[::-1]
    
    def DFS(self, ori:str):
        ori_list  = self.dic[ori]
        while ori_list:
            ori1 = ori_list.pop()
            self.DFS(ori1)
        self.res.append(ori)
            
