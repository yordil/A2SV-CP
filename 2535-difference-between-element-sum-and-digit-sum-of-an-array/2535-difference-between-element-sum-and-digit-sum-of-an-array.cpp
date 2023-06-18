class Solution {
public:
    int differenceOfSum(vector<int>& nums) {
        int sum = accumulate(nums.begin() , nums.end() , 0);
        int i = 0 ;
        int sum_d = 0;
        int dig =0;
           while(nums[i] != 0){
            
          dig =  nums[i] % 10 ;
            sum_d += dig;
            
            nums[i] /= 10 ;
            
            if(nums[i] == 0 && i < nums.size()-1){
                i++;
                
            }
        }
        
        return abs(sum - sum_d);
        
        
        
    }
};