class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        Str = ""
        
        for i in s:
            if i.isalnum():
                Str +=i.lower()
            
        return Str == Str[::-1]