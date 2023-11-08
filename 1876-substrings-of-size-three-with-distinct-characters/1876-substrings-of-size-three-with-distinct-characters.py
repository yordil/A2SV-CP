from collections import deque
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        if len(s) < 3:
            return 0
        arrays = list(s)
        counter = 0 
        sub = deque()
        for i in range(len(s)):
            sub.append(s[i])
            
            if i >=2:
                if sub[0] != sub[1] and sub[1] != sub[2] and sub[0] != sub[2]:
                    counter +=1
                sub.popleft()
                
        return counter
                
            
        
            
            