class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter = 0
        newheight = sorted(heights)
        
        for i in range(len(heights)):
            if newheight[i] != heights[i]:
                counter +=1
                
        return counter
            
        