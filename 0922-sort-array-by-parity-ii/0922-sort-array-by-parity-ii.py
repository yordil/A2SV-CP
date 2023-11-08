class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        arr =[0] * len(nums)
        
        
        even = 0
        odd = 1
        
        for i in nums:
            if i % 2:
                arr[odd] = i
                odd +=2
            else:
                arr[even] = i
                even +=2
        return arr
                