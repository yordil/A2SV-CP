class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        Stack = []
        n = len(nums)-1
        comp = float('-inf')
        
        for i in range(n , -1 , -1 ):
            if nums[i]  < comp:
                return True
            while Stack and nums[i] > Stack[-1]:
                comp = Stack.pop()
            
            Stack.append(nums[i])
            
            
        return False
            
