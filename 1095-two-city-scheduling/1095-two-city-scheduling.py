class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        total_cost = 0
        
      
        for i in range(len(costs)):
            if i < n:
                total_cost += costs[i][0]  # city 
            else:
                total_cost += costs[i][1]  # city B
        
        return total_cost