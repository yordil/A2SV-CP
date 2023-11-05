class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right  = 0 , len(height)-1
        area = 0
        width = 0
        elementdiff = 0
        while left < right:
            
            width = right - left 
            elementdiff =  min(height[right] , height[left])
            
            area = max(area , width *elementdiff)
            
            if height[left] < height[right]:
                left +=1
            elif height[right] < height[left]:
                right -=1
            else:
                left +=1
                right -=1
                
        return area
            
            
            
            
            
        
        
        
            