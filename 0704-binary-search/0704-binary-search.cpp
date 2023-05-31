class Solution {
public:
    int search(vector<int>& nums, int target) {
        int index = 0;
        int a =  0 , b = nums.size() - 1;
        
        while (a <= b){
           index =(a+b) / 2 ;
            if (nums.at(index) == target)
                 return index;
            if( nums.at(index) > target)
                b = index -1;
            else
                a = index + 1 ;
        }
        return -1;
        
    }
        
};