class Solution {
public:
    int findNumbers(vector<int>& nums) {
        
        string a {} ;
        int counter = 0;
        
        for(int i = 0 ; i < nums.size() ; ++i){
            int c = nums[i];
            
            a = to_string(c);
             if(a.size() % 2 == 0)
                 counter++;
             
        }
        
        return counter;
    }
};