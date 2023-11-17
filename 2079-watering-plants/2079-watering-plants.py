class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        counter = 0
        cap= capacity
        left = 0
        
        while left < len(plants):
            
            if cap >= plants[left]:
                cap -= plants[left]
                counter +=1
                left +=1
            else:
                cap = capacity
                counter += 2*left
                
        return counter
            
            