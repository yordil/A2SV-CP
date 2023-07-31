class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
         
        double sum = accumulate(nums.begin() , nums.begin()+k  , 0);
        
        double avg = sum/k ;
        
         for(int i = k ; i < nums.size() ; ++i){
             sum += nums[i] - nums[i-k];
             avg = max(avg , sum/k);
             
         }
        
        return avg;
    }
};