class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int > val;
         int len = nums.size();
         int flag  = 0 ;
        for(int i= 0 ; i < len ;i++){
            flag = 0 ;
            for(int j = 0 ; j < len ; j++){
                if(nums[i] > nums[j])
                    flag++;
            }
            val.emplace_back(flag);
        }
        
        return val;
    }
};