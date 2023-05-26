class Solution {
public:
    void sortColors(vector<int>& nums) {
        int len = nums.size();
        for(int i = 0 ; i < len ; i++){
            for(int j=0 ; j < len ; j++){
                if(nums.at(i) < nums.at(j))
                  swap(nums.at(i) , nums.at(j));    
                  // to align with instruction (DON't USE SORT() function)
            }
        }
    }
};