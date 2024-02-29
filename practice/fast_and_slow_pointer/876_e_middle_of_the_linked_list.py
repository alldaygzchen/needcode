from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head 

        while True:
            #  check first and check last
            if not (fast and fast.next):
                return slow

            slow = slow.next
            fast = fast.next.next


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

    s= Solution()
    print(s.middleNode(l1).val)   

    print('##############################################')

    l1 = ListNode(1) 
    l2 = ListNode(2)
    l3 = ListNode(3) 
    l4 = ListNode(4)   
    l5 = ListNode(5)
    l6 = ListNode(6)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next =l6
    s= Solution()
    print(s.middleNode(l1).val)     



