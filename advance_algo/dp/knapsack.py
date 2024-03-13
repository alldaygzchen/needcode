# Dynamic Programming
# Time: O(n*m) Space: O(m)
class Solution:
    def __init__(self,profit, weight, capacity):
        self.profit = profit
        self.weight = weight
        self.capacity =capacity
        self.row = len(profit)
        self.col = capacity+1
        self.cache = [0]*(self.col)

    def dp(self):

        for c in range(self.col):
            if self.weight[0]<=c:
                self.cache[c] = self.profit[0]
            else:
                self.cache[c] = 0

        for r in range(1,self.row):
            curRow = [0]*(self.col)
            for c in range(1,self.col):
                skip = self.cache[c]
                if c - self.weight[r]>=0:
                    include = self.profit[r] + self.cache[c - self.weight[r]]
                else:
                    include = 0
                curRow[c] = max(include,skip)
            self.cache =curRow
        return self.cache[-1]

# Dynamic Programming
# Time: O(n*m) Space: O(n*m)
# class Solution:
#     def __init__(self,profit, weight, capacity):
#         self.profit = profit
#         self.weight = weight
#         self.capacity =capacity
#         self.row = len(profit)
#         self.col = capacity+1
#         self.cache = [[None]*(self.col) for _ in range(self.row)]

#     def dp(self):

#         for r in range(self.row):
#             self.cache[r][0] = 0

#         for c in range(self.col):
#             if self.weight[0]<=c:
#                 self.cache[0][c] = self.profit[0]
#             else:
#                 self.cache[0][c] = 0

#         for r in range(1,self.row):
#             for c in range(1,self.col):
#                 skip = self.cache[r-1][c]
#                 if c - self.weight[r]>=0:
#                     include = self.profit[r] + self.cache[r-1][c - self.weight[r]]
#                 else:
#                     include = 0
#                 self.cache[r][c] = max(include,skip)

#         # print('self.cache',self.cache)
#         return self.cache[-1][-1]



# DFS memoization
# Time: O(n*m) Space: O(n*m)
# class Solution:
#     def __init__(self,profit, weight, capacity):
#         self.profit = profit
#         self.weight = weight
#         self.capacity =capacity
#         self.cache = [[None]*(capacity+1) for _ in range(len(profit))]

#     def dfs(self,idx,capacity):
        
#         if idx == len(self.profit):
#             return 0
#         if self.cache[idx][capacity]:
#             return self.cache[idx][capacity]
        
#         self.cache[idx][capacity] = self.dfs(idx+1,capacity)

#         left_capacity = capacity - self.weight[idx]
#         if left_capacity>=0:
#             leftProfit = self.profit[idx] + self.dfs(idx+1,left_capacity)
#             self.cache[idx][capacity] = max(leftProfit,self.cache[idx][capacity])
        
#         return self.cache[idx][capacity]


# Brute Force
# class Solution:
#     def __init__(self,profit, weight, capacity):
#         self.profit = profit
#         self.weight = weight
#         self.capacity =capacity

#     def bruteforce(self,idx,capacity):
        
#         if idx == len(self.profit):
#             # print('idx',idx,'capacity',capacity)
#             return 0
        
#         rightProfit = self.bruteforce(idx+1,capacity)

#         left_capacity = capacity - self.weight[idx]
#         if left_capacity>=0:
#             leftProfit = self.profit[idx] + self.bruteforce(idx+1,left_capacity)

#             maxProfit = max(leftProfit,rightProfit)
#             return maxProfit
#         return rightProfit
    
if __name__=="__main__":
    profit = [4,4,7,1]
    weight = [5,2,3,1]
    capacity =8
    s = Solution(profit,weight,capacity)
    # print('profit is',s.bruteforce(0,8))
    # print('profit is',s.dfs(0,8))
    print('profit is',s.dp())


        

