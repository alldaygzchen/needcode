class SegmentTree:
    def __init__(self,sum,L,R):
        
        # node
        self.left = None
        self.right = None

        # range
        self.L = L
        self.R = R

        # sum
        self.sum = sum

    # O(n) 
    @staticmethod
    def build(nums,L,R):

        """
        since it is divide and conquer, its  purpose is to pass the value e.g. L, R and return the segment tree node
        then go up  
        """

        # base case
        if L==R:
            return SegmentTree(nums[L],L,R)
        
        M = (L+R)//2
        root = SegmentTree(0,L,R)
        root.left = SegmentTree.build(nums,L,M)
        root.right = SegmentTree.build(nums,M+1,R)
        root.sum = root.left.sum + root.right.sum
        return root
    
    # O(logn)
    def update(self,index,val):

        """
        since it is divide and conquer, its purpose is to modify when l = r == index and modify parent sum
        then go up  
        """
        # base case
        if index == self.L == self.R:
            self.sum =  val
            return 

        M = (self.L + self.R) //2
        if index>M:
            self.right.update(index,val)    
        else:
            self.left.update(index, val)
        self.sum = self.left.sum + self.right.sum


    def rangeQuery(self,L,R):

        """
        
        since it is divide and conquer, its purpose is to  return in l = r 
        then go up  
        
        """
        
        # base case
        if L == self.L and R==self.R:
            return self.sum
        
        M = (self.L + self.R) //2
        if L>M:
            return self.right.rangeQuery(L, R)
        elif R <= M:
            return self.left.rangeQuery(L, R)
        
        else:
            return (self.left.rangeQuery(L, M) +
                    self.right.rangeQuery(M + 1, R))


        

        


