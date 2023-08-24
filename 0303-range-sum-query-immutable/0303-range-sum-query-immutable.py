class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        self.left = left
        self.right = right
        
        sumt = 0
        
        while left <=right:
            sumt+= self.nums[left]
            left+=1
        return sumt
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)