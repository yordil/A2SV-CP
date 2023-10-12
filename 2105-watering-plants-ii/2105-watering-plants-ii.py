class Solution:
    def minimumRefill(self, plants: List[int], ca: int, cb: int) -> int:
        a,b=0,len(plants)-1
        alice,bob=ca,cb
        res=0
        while a<=b:
            if a==b:
                if alice>=bob:
                    if alice<plants[a]:
                        res+=1
                    return res
                else:
                    if bob<plants[b]:
                        res+=1
                    return res
            if plants[a]>alice:
                alice=ca
                res+=1
            if plants[b]>bob:
                bob=cb
                res+=1
            alice-=plants[a]
            bob-=plants[b]
            a+=1
            b-=1
        return res








# class Solution:
#     def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
        
#         l , r = 0 , len(plants) -1 
#         diffa = 0 
#         diffb = 0
#         refill_flag = 0    
#         ca = capacityA
#         cb = capacityB
        
#         while l <= r:
            
#             if  l == r:
#                 if ca >= cb:
#                     if ca < plants[l]:
#                         refill_flag+=1
#                     else:
#                         if cb < plants[r]:
#                             refill_flag +=1
#                 break
            
#             if ca < plants[l]:
#                 ca = capacityA
#                 refill_flag +=1
        
#             if cb < plants[r]:
#                 cb = capacityB
#                 refill_flag+=1  
                
            
            
#             ca -= plants[l]
#             cb -= plants[r]
            
#             l+=1
#             r-=1
            
            
#         return refill_flag
            
            
            
            
            