class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
        
        l , r = 0 , len(plants) -1 
        diffa = 0 
        diffb = 0
        refill_flag = 0    
        ca = capacityA
        cb = capacityB
        
        while l <= r:
            
            if  l == r:
                if ca >= cb:
                    if ca < plants[l]:
                        refill_flag+=1
                else:
                    if cb < plants[r]:
                        refill_flag +=1
                break
            
            if ca < plants[l]:
                ca = capacityA
                refill_flag +=1
        
            if cb < plants[r]:
                cb = capacityB
                refill_flag+=1  
                
            
            
            ca -= plants[l]
            cb -= plants[r]
            
            l+=1
            r-=1
            
            
        return refill_flag
            
            
            
            
            