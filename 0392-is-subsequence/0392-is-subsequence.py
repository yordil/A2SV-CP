class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        empty = ""
        
        sptr , tptr = 0 , 0
        
        for i in range(len(t)):
            if sptr == len(s):
                break
            
            if t[i] == s[sptr]:
                empty+=t[i]
                sptr+=1
                
        return True if s == empty else False