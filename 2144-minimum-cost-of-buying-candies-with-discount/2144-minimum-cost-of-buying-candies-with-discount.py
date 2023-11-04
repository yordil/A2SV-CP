class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        
        cost.sort(reverse=True)    
        n = len(cost)
        if n < 3: return sum(cost)
        
        left = 0 
        right = 1
        maxcost  = 0
        while right < n:
            maxcost += cost[left]  + cost[right]
            left +=3
            right +=3
            
        
        while left < n:
            maxcost += cost[left]
            left+=1
            
        return maxcost