class Solution {
public:
    int thirdMax(vector<int>& nums) {
          set<int> dist(nums.begin() , nums.end());
        vector<int>num (dist.begin() , dist.end());
        sort(num.begin() , num.end());
        int len = num.size();
        if(num.size()  < 3)
            return num[len-1];
            return num[num.size()-3];
    }
};