class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        flag1 , flag0 = 0 , 0 
        
        max1 , max0 = 0 , 0 
        
        for i in range(len(s)):
            
            if s[i] == '0':
                flag0+=1 
                max1 = max(max1 , flag1)
                flag1 = 0
            elif s[i] == '1':    
                flag1+=1
                max0 = max(max0 , flag0)
                flag0 = 0
                
        max0 = max(max0 , flag0)
        max1 = max(max1 , flag1)
        
        return True if max1 > max0 else False
    