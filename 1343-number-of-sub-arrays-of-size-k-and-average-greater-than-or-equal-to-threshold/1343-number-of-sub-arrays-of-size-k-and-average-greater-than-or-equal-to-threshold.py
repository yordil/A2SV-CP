class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
       
        counter = 0
        Sum = 0
        left = 0
        for i in range(len(arr)):
            Sum += arr[i]
            
            if i >= k-1:
                if Sum/k >= threshold:
                    counter +=1
                Sum -= arr[left]
                left+=1
                
        return counter