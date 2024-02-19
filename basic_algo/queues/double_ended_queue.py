# aware of the direction 
# first: self.head.next.next.prev = self.head second:self.head.next = self.head.next.next

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        

    def append(self, value: int) -> None:
        new_node = Node(value)
        new_node.next = self.tail
        new_node.prev = self.tail.prev

        self.tail.prev.next = new_node
        self.tail.prev = new_node


    def appendleft(self, value: int) -> None:
        
        new_node = Node(value)
        new_node.prev = self.head
        new_node.next = self.head.next

        self.head.next.prev = new_node
        self.head.next = new_node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        value = self.tail.prev.value
        
        self.tail.prev.prev.next=self.tail
        self.tail.prev = self.tail.prev.prev

        return value
    
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        value = self.head.next.value
        
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        

        return value