"""
Since it is a complete tree,
elements can be order from top to bottom and from left to right in array

the index one element will be the root for calculation simplicity
"""
class Heap:
    def __init__(self):
        # this is a list
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        
        # get the last index 
        i = len(self.heap) - 1

        # Percolate up  (to locate the current i index)
        while True:
            if i==1:
                return
            if i>1 and self.heap[i//2]>self.heap[i]:
                #swap the children to the parent till satisifies  
                tmp = self.heap[i//2]
                self.heap[i//2] =  self.heap[i]
                self.heap[i] = tmp
                i = i//2

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        # to satisfy the structure property, we percolate down the last element
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i=1
        # Percolate down (to locate the current i index)
        while True:
            if ((2*i<=len(self.heap)-1 and 2*i+1<=len(self.heap)-1) and 
                (self.heap[2*i]>self.heap[2 * i + 1]) and
                (self.heap[i] > self.heap[2 * i + 1])):#self.heap[2*i+1] is the smallest
                tmp = self.heap[i]
                self.heap[i] = self.heap[2*i+1]
                self.heap[2*i+1] = tmp
                i=2*i+1

            elif ((2*i<=len(self.heap)-1) and self.heap[i] > self.heap[2 * i]):
                tmp = self.heap[i]
                self.heap[i] = self.heap[2*i]
                self.heap[2*i] = tmp
                i=2*i+1
            else:
                break
        return res
    
    def top(self):
            if len(self.heap) > 1:
                return self.heap[1]
            return None

    def heapify(self, arr):
        # 0-th position is moved to the end
        arr.append(arr[0])

        self.heap = arr
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            # Percolate down
            i = cur
            while 2 * i < len(self.heap):
                if (2 * i + 1 < len(self.heap) and 
                self.heap[2 * i + 1] < self.heap[2 * i] and 
                self.heap[i] > self.heap[2 * i + 1]):
                    # Swap right child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2 * i]:
                    # Swap left child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp
                    i = 2 * i
                else:
                    break
            cur -= 1



