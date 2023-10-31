class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        Sum = sum(nums)
        
        prefix = 0
        
        rightsum = 0 
        for i in range(len(nums)):
            prefix +=nums[i]
            rightsum = Sum - prefix + nums[i]
            
            if(prefix == rightsum):
                return i
            
         
            
        return -1
    
    
# my previous cpp implmentation   


# class Solution {
# public:
#     int pivotIndex(vector<int>& nums) {
        
#         int left_sum =0 ;
#         int right = accumulate(nums.begin() , nums.end(), 0);
#         for(int i= 0 ; i< nums.size() ;++i){
            
#             int rightcpy;
#             left_sum += nums[i];
#             rightcpy = right - left_sum + nums[i];
           
#             if(left_sum == rightcpy)
#                return i;
#         }
               
#                return -1;
#     }

# };

            
        
        
      
            
            
        