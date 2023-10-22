class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        Hash = {}
        
        for i in range(len(arr)):
            
            if arr[i] in Hash:
                Hash[arr[i]] += 1
            else:
                Hash[arr[i]] = 1
                
        # Sort dictionary by their frequency (descending order)
        num_freq = sorted(Hash.values(), reverse=True) 
        
        half = len(arr) // 2
        size = 0
        
        while half > 0:
            half -= num_freq[size]
            size += 1
        
        return size
        
        


        
            
            
            
            
            