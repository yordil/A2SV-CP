class Solution:
    def defangIPaddr(self, address: str) -> str:
        num = ""
        
        for i in address:
            if i == '.' :
               num +="[.]"
            else:
               num+=(i)
            
        return num