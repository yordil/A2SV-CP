class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
         sort(nums.begin() , nums.end());
        vector<int> major;
        int x;
      for(int i = 0 ; i < nums.size() ; i+=x){
           x = count(nums.begin(), nums.end() , nums[i]);
              if( x > floor(nums.size() / 3))
               major.push_back(nums[i]);
      }
          return major; 
    }
};