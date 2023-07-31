class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
         # create a string which is equal length with s1
        
        Str = s2[:len(s1)]
        itr = 0 
            
        for i in range(len(s1) , len(s2)+1):
            if sorted(Str) == sorted(s1):
                return True
            itr +=1
            Str = s2[itr:i+1]
        return False
        