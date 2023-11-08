class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        arr = [0] * 2*n
        
        left = 0
        right = 1
        i = 0 ;
        
        for i in range(n):
            arr[left] = nums[i]
            arr[right] = nums[n+i]
            left +=2
            right +=2
            
        return arr