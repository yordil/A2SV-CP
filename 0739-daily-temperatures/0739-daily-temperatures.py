class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for idx , tmp in enumerate(temperatures):
            while stack and stack[-1][0] < tmp:
                stackval , stackidx = stack.pop()
                ans[stackidx] = idx - stackidx
            stack.append([tmp , idx])
            
        return ans
        
        
        
        
        
        
        
        
#   previous brute force approach 
#         counter = 0
        
#         for i in range(len(temperatures)-1):
#             counter = 0
#             for j in range(i+1 , len(temperatures)):
#                 counter+=1
#                 if temperatures[i] < temperatures[j]:
#                     ans[i] = counter
#                     break
                    
                
#         return ans