# DFS memoization
# Time: O(n*m) Space: O(n*m)
class Solution:
    def __init__(self,profit, weight, capacity):
        self.profit = profit
        self.weight = weight
        self.capacity =capacity
        self.cache = [[None]*(capacity+1) for _ in range(len(profit))]

    def bruteforce(self,idx,capacity):
        
        if idx == len(self.profit):
            return 0
        
        if self.cache[idx][capacity]:
            return self.cache[idx][capacity]
        
        self.cache[idx][capacity] = self.bruteforce(idx+1,capacity)

        left_capacity = capacity - self.weight[idx]
        if left_capacity>=0:
            leftProfit = self.profit[idx] + self.bruteforce(idx,left_capacity)

            self.cache[idx][capacity] = max(leftProfit,self.cache[idx][capacity])
        return self.cache[idx][capacity]




# Brute Force
# Time: O(2^c) Space:O(2^c)
# class Solution:
#     def __init__(self,profit, weight, capacity):
#         self.profit = profit
#         self.weight = weight
#         self.capacity =capacity

#     def bruteforce(self,idx,capacity):
        
#         if idx == len(self.profit):
#             return 0
        
#         rightProfit = self.bruteforce(idx+1,capacity)

#         left_capacity = capacity - self.weight[idx]
#         if left_capacity>=0:
#             leftProfit = self.profit[idx] + self.bruteforce(idx,left_capacity)

#             maxProfit = max(leftProfit,rightProfit)
#             return maxProfit
#         return rightProfit

# Brute Force
# class Solution:
#     def __init__(self,profit, weight, capacity):
#         self.profit = profit
#         self.weight = weight
#         self.capacity =capacity

#     def bruteforce(self,capacity):
        
#         if capacity<=0:
#             return 0
        
#         collect = [] 
#         for i in range(len(self.profit)):
#             if self.weight[i]<=capacity:
#                 collect.append(self.profit[i]+self.bruteforce(capacity-self.weight[i]))
#         return max(collect)
if __name__=="__main__":
    profit = [4,4,7,1]
    weight = [5,2,3,1]
    capacity =8
    s = Solution(profit,weight,capacity)
    print('profit is',s.bruteforce(0,8))
    # print('profit is',s.bruteforce(8))