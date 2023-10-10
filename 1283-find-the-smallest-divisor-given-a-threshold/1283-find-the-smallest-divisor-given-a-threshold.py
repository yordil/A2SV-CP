class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        divisor = [ i for i in range(1, max(nums) + 1)]

        res = 1
        l = 0
        r = len(divisor) - 1
        while l <= r:
            mid =  (r+l) // 2
            
            Sum = 0
            for num in nums:
                Sum += math.ceil(num / divisor[mid])
            
            if Sum > threshold:
                l = mid + 1
            else:
                r = mid - 1

        res = divisor[l]

        return res
        

# class Solution:
#     def smallestDivisor(self, nums: List[int], threshold: int) -> int:
#         nums.sort()
        
#         Sum = sum(nums)
      
#         left , right = 0  , len(nums) -1 
#         Max = 0
#         while left <= right:
            
#             mid = left + (right - left)//2
            
#             if ceil(Sum/nums[mid]) <= threshold:
#                 return nums[mid]
#             elif ceil(Sum/nums[mid]) > threshold:
#                 left = mid + 1
          
#         return Max