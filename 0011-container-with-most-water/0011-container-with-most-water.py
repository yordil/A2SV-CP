class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        Max = 0 
        
        l , r  = 0 , len(height)-1
        
        while l < r :
           
            diff = r - l
        
            elementdiff = min(height[l] , height[r])
        
            Max = max(Max  , diff * elementdiff)
            
            if height[l] < height[r]:
                l+=1
            elif height[l] > height[r]:
                r-=1
            else:
                l+=1
                r-=1
            
        return Max
        
        
        
            