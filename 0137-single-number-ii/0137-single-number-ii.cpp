class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int len = nums.size();
        int single = 5;
        vector<int> index;
         int flag;
        for(int i= 0 ; i < len ; i++){
            flag = 0 ;
            for(int j = 0 ; j < len ; j++ ){
                if(nums.at(i) == nums.at(j))
                   flag++;

            }
            index.push_back(flag); 
             if(flag == 1){
             single = nums.at(i);
             goto returnn;
             }
        }
    
        returnn: return single;
    }
};