# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # // my first implmentation using hashset and O(n) memory space
        
        # val = 0 ;
         
        slow , fast =  head , head
        
        while fast and fast.next:
           
            
            slow = slow.next 
            fast = fast.next.next
            
            if slow == fast:
                break
                
        if not fast or not fast.next:
            return None
        
        anotherslow = head
        
        while anotherslow != slow:
            anotherslow= anotherslow.next
            slow =slow.next
            
        return anotherslow
            
            
            
       
    
    
    
# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         # // my first implmentation using hashset and O(n) memory space
        
#         # val = 0 ;
        
#         myhash = set()
        
#         slow , fast =  head , head
        
#         while fast and fast.next:
            
#             if slow in myhash:
#                 return slow
            
#             myhash.add(slow)
            
#             slow = slow.next
#             fast = fast.next.next
            
            
            
#         return None