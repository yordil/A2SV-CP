class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        Hash = {}
        
        for i in range(len(arr)):  # time  O(N)
            
            if arr[i] in Hash:
                Hash[arr[i]] += 1   # o(N ) space complexity , where n is the size of the array
            else:
                Hash[arr[i]] = 1
                
        # Sort dictionary by their frequency (descending order)
        
        num_freq = sorted(Hash.values(), reverse=True) 
        # in here we have 2 things 1. extracting from the Hash and Sorting 
        # to extrac O(N)-> and to sort in worest scenario using built in O(N*logN)
        # we use array of num_freq and it is space complexity is O(N)
        
        half = len(arr) // 2
        
        size = 0
        
        print(num_freq)
        
        while half > 0: #we have here # O(n/2) time complexity so reduced to O(N)
            half -= num_freq[size]
            size += 1
        
        return size
    
    
# so as a concliusion we have O(N*logN) Time  and O(N) space complexity
        
        


        
            
        
            
            
            