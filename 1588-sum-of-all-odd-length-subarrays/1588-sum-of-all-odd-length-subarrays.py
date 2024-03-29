class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        #first sum of all element in the list
        
        first_sum = sum(arr)
        
        for i in range(len(arr)): 
            for j in range(2+i , len(arr) , 2):
                first_sum += sum(arr[i:j+1])
                
                
        return first_sum
            
# since in the constraint we have told that the length of the array is <=
# 100 so O(n^2) so normal in this condition