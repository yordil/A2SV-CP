class Solution:
    def reverseVowels(self, s: str) -> str:
        ls = ['a' , 'e' , 'i' , 'o' , 'u' , 'A' , 'E' , 'I' , 'O' , 'U']
        
        left = 0
        right = len(s)-1
        ss = list(s)
        
        while left < right :
            
            if ss[left]  in ls and ss[right] in ls:
                ss[left] , ss[right] = ss[right] , ss[left]
                left+=1
                right-=1
            elif ss[left]  not in ls and s[right] in ls:  
                left+=1
            elif ss[left] in ls and ss[right] not in ls:  
                right-=1
            else:  
                right-=1
                left+=1
                
                
        return "".join(ss)
                
                
            
           