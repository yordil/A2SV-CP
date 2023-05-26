class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        int flag{};
        int sum{};
        int len = nums.size();
        for(int i= 0 ; i < len ; i++ ){
            flag = 0 ;
             for(int j = 0 ; j < len ; j++ ){
                 if(nums.at(i) == nums.at(j))
                   flag++;
             }

             if (flag == 1)
             sum +=nums.at(i);
        }

        return sum;
    }
};