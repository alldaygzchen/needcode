class Solution:
    def __init__(self,profit, weight, capacity):
        self.profit = profit
        self.weight = weight
        self.capacity =capacity

    def bruteforce(self,idx,capacity):
        
        if idx == len(self.profit):
            return 0
        
        rightProfit = self.bruteforce(idx+1,capacity)

        left_capacity = capacity - self.weight[idx]
        if left_capacity>=0:
            leftProfit = self.profit[idx] + self.bruteforce(idx+1,left_capacity)

            maxProfit = max(leftProfit,rightProfit)
            return maxProfit
        return rightProfit
    
if __name__=="__main__":
    profit = [4,4,7,1]
    weight = [5,2,3,1]
    capacity =8
    s = Solution(profit,weight,capacity)
    print('profit is',s.bruteforce(0,8))


        

