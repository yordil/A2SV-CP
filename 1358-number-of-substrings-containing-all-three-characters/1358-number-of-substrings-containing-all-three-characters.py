class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = 0
        indices = [0, 0, 0] 
        
        for i in range(len(s)):
            if s[i] == 'a':
                indices[0] = i + 1
            elif s[i] == 'b':
                indices[1] = i + 1
            else:
                indices[2] = i + 1
            
           
            if all(idx > 0 for idx in indices):
               
                counter += min(indices)
        
        return counter

                
                
            