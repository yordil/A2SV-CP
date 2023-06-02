class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        int len = nums.size()-1;
        sort(nums.begin() , nums.end());
        
        if ( nums.at(len) * nums.at(len - 1) * nums.at(len -2)  > nums.at(0) * nums.at(1) * nums.at(len) )
           return nums.at(len) * nums.at(len - 1) * nums.at(len -2) ;
        else
            return nums.at(0) * nums.at(1) * nums.at(len) ; // if the first two element - ve their product will be high
        
    }
};