class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
         int left = 0;
        int right = nums.size() - 1;
        vector<int> result(nums.size(), 0);
        int i = nums.size() - 1;

        while (left <= right) {
            if (abs(nums[left]) > abs(nums[right])) {
                result[i] = nums[left] * nums[left];
                left++;
            } else {
                result[i] = nums[right] * nums[right];
                right--;
            }
            i--;
        }

        return result;
    }
    
};