class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        c = []
        def back(i,j):
            if len(j)==k:
                c.append(j.copy())
                return
            
            for i in range(i , n+1):
                j.append(i)
                back(i+1 , j)
                j.pop()
        back(1 , [])
        return c
        