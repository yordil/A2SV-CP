class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        l = 0
        l2 = 0
        S= ""
        while l < len(word1) and l2 < len(word2):
            
            S+=word1[l]
            S+=word2[l2]
            l+=1
            l2+=1
        if l < len(word1):
            while l < len(word1):
                S+=word1[l]
                l+=1
        elif l2 < len(word2):
            while l2 < len(word2):
                S+=word2[l2]
                l2+=1
                
        return S
            
            
            