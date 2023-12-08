class Solution:
    def totalMoney(self, n: int) -> int:
        weekly = 28
        if n < 8:
            return sum(range(1, n + 1))
        else:
            divs = n // 7
            mod = n % 7
#             the normal weeks they 
            normal_week = divs * 28 + divs * (divs - 1) // 2 * 7
#     The last week
            mod_week = divs * mod + mod * (mod + 1) // 2
            
            return normal_week + mod_week

    
    
        
#         S = 0
#         j = 0
#         counter = 0
#         for i in range(1 , n+1):
            
#             if (i-1) % 7 == 0:
#                 counter +=1
#                 # j=0
#                 j = counter
#             S+=j
            
            
#             j+=1
#         return S
            
