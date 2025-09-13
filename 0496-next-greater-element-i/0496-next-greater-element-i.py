class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_great =  {}
        
        stack = []

        for num in nums2:

            while stack and stack[-1] < num:
                next_great[stack[-1]] = num
                stack.pop()

            stack.append(num)


        ans  = []

        for num in nums1:
            if num in next_great:
                ans.append(next_great[num])
            
            else:
                ans.append(-1)

        return ans 

            


        