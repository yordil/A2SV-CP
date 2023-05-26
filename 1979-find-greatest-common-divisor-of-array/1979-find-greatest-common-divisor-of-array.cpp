class Solution {
public:
    int findGCD(vector<int>& nums) {
       int len = nums.size();
       int GCD {};
       sort(nums.begin() , nums.end());
       int first_element = nums.at(0);
       for(int i = 1 ; i <= first_element; i++){
           if( first_element % i == 0 && nums.at(len-1) % i == 0)
               GCD = i;
       }

       return GCD;
    }
};