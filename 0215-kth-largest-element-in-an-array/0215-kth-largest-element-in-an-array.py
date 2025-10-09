class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        myheap = []

        for num in nums:

            if len(myheap)>= k:
                if num > myheap[0]:
                    heappop(myheap)
                    heappush(myheap , num)
            else:
                heappush(myheap , num)

           

        return myheap[0]