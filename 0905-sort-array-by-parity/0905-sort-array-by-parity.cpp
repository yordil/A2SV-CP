class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        
        for(int i = 0 ; i < nums.size() ; ++i){
            int index = i;
            for(int j = 0 ; j < nums.size() ; j++){
                 if(nums[j] % 2 != 0){
                     index = j; break;}
            }
            swap(nums[index] , nums[i]);
        }
        
        return nums;
    }
};

//  selection sort algorithm