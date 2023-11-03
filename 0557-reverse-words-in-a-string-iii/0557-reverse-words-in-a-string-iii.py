class Solution:
    def reverseWords(self, s: str) -> str:
        
        word = s.split()
        ans = ""
        
        for i in range(len(word)):
            Str = word[i][::-1]
            
            ans += Str
            ans += " "
            
        return ans.strip()
            
            