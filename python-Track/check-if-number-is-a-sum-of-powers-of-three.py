class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        Sum = 0
        
        for i in range(16 , -1 , -1):
            if 3 ** i > n:
                continue
            elif Sum + 3 **i <= n:
                Sum += 3**i
        
        return Sum == n
        

