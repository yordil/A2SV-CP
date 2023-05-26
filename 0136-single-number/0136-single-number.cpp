class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int len = nums.size();
        int x = 0;
        int value;
        for(int i = 0 ; i < len ; i++){
            x = count(nums.begin(), nums.end(), nums.at(i));
              if( x == 1){
                  value = nums.at(i);
                  break;
              }
                
        }
        return value;
    }
};