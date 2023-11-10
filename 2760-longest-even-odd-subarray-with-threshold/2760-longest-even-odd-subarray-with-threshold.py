class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        counter = 0
        long = 0
        left , right = 0 , 1 
        while left < len(nums):
            if nums[left] > threshold or nums[left] %2 !=0:
                left +=1
                right = left +1
                continue
            else:
                while right < len(nums):
                    if nums[right] > threshold:
                        break;

                    if nums[right- 1] %2 != nums[right]%2:
                         right +=1

                    else:
                        break
                long = max(long , right-left)
                left +=1
                right =left +1

        return long
                
                
        