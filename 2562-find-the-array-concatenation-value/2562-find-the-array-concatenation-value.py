class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        
        left , right = 0 , len(nums) -1 
        S = ""
        num = 0
        while left <= right:
            S = ""
            if left == right:
                num +=nums[left]
                break
                
            else:
                S = str(nums[left]) + str(nums[right])
                num += int(S)
                
            left +=1
            right -=1
            
        return num
                
                
            