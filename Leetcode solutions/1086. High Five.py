# 1086. High Five
# Easy

# 502

# 84

# Add to List

# Share
# Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from a student with IDi, calculate each student's top five average.

# Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj and their top five average. Sort result by IDj in increasing order.

# A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division.

 

# Example 1:

# Input: items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
# Output: [[1,87],[2,88]]
# Explanation: 
# The student with ID = 1 got scores 91, 92, 60, 65, 87, and 100. Their top five average is (100 + 92 + 91 + 87 + 65) / 5 = 87.
# The student with ID = 2 got scores 93, 97, 77, 100, and 76. Their top five average is (100 + 97 + 93 + 77 + 76) / 5 = 88.6, but with integer division their average converts to 88.
# Example 2:

# Input: items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
# Output: [[1,100],[7,100]]
 

# Constraints:

# 1 <= items.length <= 1000
# items[i].length == 2
# 1 <= IDi <= 1000
# 0 <= scorei <= 100
# For each IDi, there will be at least five scores.

# S1

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        score_dic = dict()
        for id in items:
            if id[0] not in score_dic:
                score_dic[id[0]] = [id[1]]
            else: 
                score_dic[id[0]].append(id[1])
                score_dic[id[0]].sort(reverse=True)
                
        return [[id, sum(score_dic[id][:5])//5] for id in sorted(score_dic.keys())]
                
                
                
# S2

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        score_dic =collections.defaultdict(list)
        for id, score in items:
            heapq.heappush(score_dic[id], score)
            while len(score_dic[id]) > 5:
                heapq.heappop(score_dic[id])
        return [[id, sum(score_dic[id])//5] for id in sorted(score_dic.keys())]
