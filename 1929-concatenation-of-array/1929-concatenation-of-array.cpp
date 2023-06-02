class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> Copy = nums;
        nums.insert(nums.end() , Copy.begin() , Copy.end());
        
        return nums;
    }
};