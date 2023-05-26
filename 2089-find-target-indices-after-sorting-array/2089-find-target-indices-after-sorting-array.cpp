class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
         sort(nums.begin(), nums.end());
         vector <int> index;
         int len = nums.size();
          for (int i= 0 ; i < len ; i++ ){
              if(nums.at(i) == target)
               index.push_back(i);
              
          }
          return index;

    }
};