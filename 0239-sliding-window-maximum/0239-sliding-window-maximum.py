class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans  = []

        myque = deque()


        for i in range(len(nums)):
            
            while myque and myque[0] <= i-k:
                myque.popleft()

            while myque and nums[i] >= nums[myque[-1]]:
                myque.pop()

            myque.append(i)


            if i >= k-1:
                ans.append(nums[myque[0]])

        return ans