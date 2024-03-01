from typing import List,Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        idx = 0

        while True:

            if slow == fast and idx!=0:
                return True

            if not (fast and fast.next):
                return False
            
            slow = slow.next
            fast = fast.next.next
            idx+=1
            



if __name__=="__main__":
    s= Solution()
    l1 = ListNode(3) 
    l2 = ListNode(2)
    l3 = ListNode(0) 
    l4 = ListNode(-4)   
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next =l2
    print(s.hasCycle(l1)) #1
    l1 = ListNode(1) 
    l2 = ListNode(2)
    l1.next = l2
    l2.next = l1
    print(s.hasCycle(l1)) #0
    l1 = ListNode(1) 
    print(s.hasCycle(l1)) #-1