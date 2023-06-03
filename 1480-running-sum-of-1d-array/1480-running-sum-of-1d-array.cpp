class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int len = nums.size();
        vector <int> numscpy = nums ; 
        for(int i = 1 ; i < len ; i++ ){
            for(int j = 0 ; j < i ; j++){
                numscpy[i] +=nums[j];
            }
        }
        return numscpy;
    }
};