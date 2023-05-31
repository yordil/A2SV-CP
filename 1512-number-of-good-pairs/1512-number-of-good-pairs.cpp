class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int counter {};
        
        for(int i = 0 ; i < nums.size() -1 ; i++){
            for(int j = i+1 ; j < nums.size() ; j++){
                if ( i < j   && nums.at(i) == nums.at(j))
                    counter++;
            }
        }
        return counter;
    }
};