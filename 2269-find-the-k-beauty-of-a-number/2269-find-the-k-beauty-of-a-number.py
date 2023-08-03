class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        counter =0
        
        strarr = str(num)
        
    
        for i in range(len(strarr)):
            if i + k <= len(strarr):
                divisor = int(strarr[i:k+i])
                if divisor != 0:
                    if num % int(strarr[i:k+i]) == 0:
                        counter+=1
            else:
                break
                
        return counter