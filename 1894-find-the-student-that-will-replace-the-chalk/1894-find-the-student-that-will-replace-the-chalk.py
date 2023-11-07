class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        total = sum(chalk)
        remainder = k % total
        
#         prefix = [chalk[0]] * len(chalk)
        
#         for i in range(1, len(chalk)):
#             prefix[i] = prefix[i-1] * chalk[i]
            
        
        for i in range(len(chalk)):
            if(chalk[i]) > remainder:
                return i
            remainder -= chalk[i]
    
#     3  7  8  10    ->  k=25 - 10 -8 -7 
#  5  1  5 - > 5  6 11 ->   k = 22 