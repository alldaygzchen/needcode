from typing import List

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:

    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:

        res =[]

        for idx in range(1,len(pairs)):
            prev_idx = idx-1
            while prev_idx>=0 and pairs[prev_idx].key>pairs[prev_idx+1].key:
                tmp = pairs[prev_idx+1]
                pairs[prev_idx+1]=pairs[prev_idx]
                pairs[prev_idx]=tmp
                prev_idx-=1
            res.append(pairs[:])
        return res



#########################################################
def insertionSort(arr):

    for idx in range(1,len(arr)):
        prev_idx = idx-1
        while prev_idx>=0 and arr[prev_idx]>arr[prev_idx+1]:
            tmp = arr[prev_idx+1]
            arr[prev_idx+1]=arr[prev_idx]
            arr[prev_idx]=tmp
            prev_idx-=1
    return arr

class SolutionRec1:
    def insertionSortRec(self,arr):
        self.arr =arr
        self.sort = []
        self.helper(0)
        return self.sort
    
    def helper (self,idx):
        # the output is to calculate (start,idx) self.sort 
        if idx == len(self.arr):
            return self.sort 
        
        self.sort.append(self.arr[idx])
        prev_idx = idx-1
        while prev_idx>=0 and self.sort[prev_idx]>self.sort[prev_idx+1]:
            tmp = self.sort[prev_idx+1]
            self.sort[prev_idx+1]=self.sort[prev_idx]
            self.sort[prev_idx]=tmp
            prev_idx-=1            
        return self.helper(idx+1)



# too much work
# class SolutionRec2:
#     def insertionSortRec(self,arr):
#         self.arr =arr
#         self.sort = []
#         self.helper(len(self.arr)-1)
#         return self.sort
    
#     def helper (self,idx):
#         if idx<0:
#             return self.sort 
        
#         self.sort.append(self.arr[idx])
#         next_idx = idx+1
#         print("idx",idx,"next_idx",next_idx,'self.arr',self.arr)
#         print('self.sort',self.sort)
#         while next_idx<=len(self.arr)-1 and self.arr[next_idx]<self.arr[next_idx-1]:
#             print("idx",idx,"next_idx",next_idx,"a",len(self.arr)-1-(next_idx-1),"b",len(self.arr)-next_idx)
#             tmp = self.arr[next_idx-1]
#             self.sort[len(self.arr)-1-(next_idx-1)]=self.arr[next_idx]
#             self.sort[len(self.arr)-next_idx]=tmp
#             next_idx+=1            
#         return self.helper(idx-1)
    


if __name__=="__main__":
    s=SolutionRec1()
    print(s.insertionSortRec([2,3,4,1,6]))