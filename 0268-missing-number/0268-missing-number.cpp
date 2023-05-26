class Solution {
public:
    int missingNumber(vector<int>& nums) {
       int len = nums.size();
       int check = 0;
       int index=0;
       
       sort(nums.begin() , nums.end());

       for(int i = 0 ; i < len ; i++){
           if( nums.at(i) != check){
               index = i ;
               break;
           }
           check++;
             
       }
       return check;

    }
};