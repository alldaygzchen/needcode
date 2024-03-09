import heapq

class Median:
    def __init__(self):
        self.small = []
        self.large = []

    def insert(self,num):
        heapq.heappush(self.small,-1*num)

        
        if (self.small and self.large and (-1*self.small[0])>self.large[0]):
            tmp = -1*heapq.heappop(self.small)
            heapq.heappush(self.large,tmp)


        # handle uneven should be in the last
        if len(self.large)>len(self.small)+1:
            tmp = heapq.heappop(self.large)
            heapq.heappush(self.small,-1*tmp)


        if len(self.small)>len(self.large)+1:
            tmp = -1*heapq.heappop(self.small)
            heapq.heappush(self.large,tmp)


        # print('max heap',m.small)
        # print('min heap',m.large)

    def getMedian(self):
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2
    
if __name__=="__main__":
    m= Median()
    m.insert(5)
    m.insert(9)
    m.insert(10)
    m.insert(11)

    # m.insert(11)
    # m.insert(5)
    # m.insert(9)
    # m.insert(10)
    print('max heap',m.small)
    print('min heap',m.large)
    print('the median', m.getMedian())
