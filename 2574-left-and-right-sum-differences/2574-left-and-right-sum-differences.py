class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        answer =[0] * len(nums)
        Sum = 0 
        
        
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i-1]
            
        for i in range(len(nums)-2 , -1 , -1):
            postfix[i] = postfix[i+1] + nums[i+1]
            
        for i in range(len(nums)):
            answer[i] = abs(prefix[i] - postfix[i])
            
        print(prefix)
        print(postfix)
            
        return answer
            
        