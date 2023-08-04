class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = ''.join(char for char in s if char.isalnum()).lower()
       # alnum.lower()
       
        
        return alnum == alnum[::-1]