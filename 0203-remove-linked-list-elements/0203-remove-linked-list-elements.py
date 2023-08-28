# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        
        
        pr , curr = dummy , head
        
        while curr:
            
            nxtptr = curr.next
            
            if curr.val == val:
                pr.next = nxtptr
            else:
                pr = curr
                
            curr = curr.next
            
        return dummy.next