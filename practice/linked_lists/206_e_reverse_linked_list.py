# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head

        while True:
            if not curr:
                return prev
            tmp = curr.next
            curr.next = prev

            # change to other step
            prev = curr
            curr = tmp

class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # base case
        if not head:
            return None

        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next= head
        else:
            new_head = head
            head.next = None
        return new_head




if __name__=="__main__":
    l1 = ListNode(1) 
    l2 = ListNode(2)
    l3 = ListNode(3) 
    l4 = ListNode(4)   
    l5 = ListNode(5)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    # s= Solution()
    s= Solution1()
    print(s.reverseList(l1).val)   

    print('###########################')
    
    
    l1 = ListNode(1) 
    l2 = ListNode(2)

    l1.next = l2

    # s= Solution()
    s= Solution1()
    print(s.reverseList(l1).val)   