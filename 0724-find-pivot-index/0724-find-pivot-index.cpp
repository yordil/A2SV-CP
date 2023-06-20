class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        
        int left_sum =0 ;
        int right = accumulate(nums.begin() , nums.end(), 0);
        for(int i= 0 ; i< nums.size() ;++i){
            
            int rightcpy;
            left_sum += nums[i];
            rightcpy = right - left_sum + nums[i];
           
            if(left_sum == rightcpy)
               return i;
        }
               
               return -1;
    }
};