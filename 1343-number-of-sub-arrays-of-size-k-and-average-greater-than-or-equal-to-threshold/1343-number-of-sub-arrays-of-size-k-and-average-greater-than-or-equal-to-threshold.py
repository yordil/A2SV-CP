class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left , right = 0 , k
        
        counter = 0
        
        Sum = sum(arr[: right])
        
        if Sum/k >= threshold:
            counter +=1
            
        for i in range(len(arr)-k):
            Sum += -arr[left] + arr[right]
            left +=1
            right+=1
            
            if  Sum / k >= threshold :
                counter+=1
            
        return counter
            