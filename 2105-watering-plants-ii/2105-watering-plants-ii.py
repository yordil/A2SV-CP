class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        alice , bob = capacityA , capacityB
        left  , right = 0 , len(plants) -1 
        refill = 0
        while left <= right:
            if left == right:
                if alice >=bob:
                    if alice < plants[left]:
                        refill +=1
                else:
                     if bob < plants[left]:
                        refill +=1
                break
            if  alice < plants[left]:
                alice = capacityA
                refill +=1
                 
            if bob < plants[right]:
                bob = capacityB
                refill +=1
            alice -= plants[left]    
            bob -= plants[right]
            
            left+=1 
            right -=1 
            
            
        return refill
            
            
            
            