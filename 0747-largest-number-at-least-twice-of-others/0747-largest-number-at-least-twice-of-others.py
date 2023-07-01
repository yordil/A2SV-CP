class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        num = sorted(nums)
        if(num[len(num)-1] >= 2*(num[len(num)-2])): 
              x = num[len(num)-1]
              return nums.index(x)
       
        return -1;
# since numbers are unique 