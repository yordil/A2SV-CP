class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l , r = 0 , len(s) -1
        flag = 0 
        
        while l < r :
            if s[l] != s[r]:
                lefts , right = s[l+1 : r+1] , s[l : r]
                
                return (
                    lefts == lefts[::-1] or right == right[::-1])
            
            l +=1
            r -= 1
         
           
        return True
                
                
                
            
            
            
# class Solution:
#     def validPalindrome(self, s: str) -> bool:
        
#         l , r = 0 , len(s) -1
#         flag = 0 
        
#         while l <= r :
            
#             if s[l] == s[r] :
#                 l+=1
#                 r-=1   
#             elif s[l] != s[r] and flag < 1:
#                 if s[l+1] == s[r]:
#                     l +=2
#                     r -=1
#                 elif s[l] == s[r-1]:
#                     l+=1
#                     r -=2    
#                 else:
#                     return False
                
#                 flag +=1
           
#             else:
#                 return False
            
           
#         return True
                
                
                
            
            