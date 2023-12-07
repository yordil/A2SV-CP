class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        ans=""
        left= 0
        r = 0
       
        
        
        
        for i in range(len(s)):
            
            if r < len(spaces) and i == spaces[r]:
                r+=1
                ans+=" "
            ans+=s[i]
            
        return ans
            
            
            
        
#         while left < len(s):
            
#             if left == spaces[i]:
#                 ans+=" "
#                 i+=1
                
#             ans += s[left]
            
#             r+=1
#             left+=1
                
#         return ans
                
            
            
            