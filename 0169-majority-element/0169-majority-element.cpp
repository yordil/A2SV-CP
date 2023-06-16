class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin() , nums.end());
        int x;
      for(int i = 0 ; i < nums.size() ; i+=x){
           x = count(nums.begin(), nums.end() , nums[i]);
              if( x > floor(nums.size() / 2))
                  return nums[i];
      }
          return 0 ; // unnecessary line to make the code to work correcctly
    }
       
};