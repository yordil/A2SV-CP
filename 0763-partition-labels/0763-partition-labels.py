class Solution:
    def partitionLabels(self, s: str) -> List[int]:
       
    
        hashidx = {}
        ans = []
        size = 0
        end= 0
        
        for i , v in enumerate(s):
            hashidx[v] = i
            
        
        for i in range(len(s)):
            end = max(end , hashidx.get(s[i]))
            size +=1
            
            if end == i:
                ans.append(size)
                size=0
                
        return ans
            
        
        