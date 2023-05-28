class Solution {
public:
    int findMaxK(vector<int>& nums) {
        int len = nums.size();
       sort(nums.begin() , nums.end());
           
           for(int i = len - 1 ; i >= 0 ; --i){
               for(int j = 0 ; j < len ; j++){
                   if(nums.at(i) == (-1)*nums.at(j))
                       return nums.at(i);
               }
           } 
        return -1 ;
    }
};