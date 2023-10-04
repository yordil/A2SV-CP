class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        seats.sort()
        students.sort()
        
        maxmove = 0 
        
        for i in range (len(seats)):
            
            maxmove += abs(seats[i] - students[i])
        
        return maxmove
        
        
        
        # 