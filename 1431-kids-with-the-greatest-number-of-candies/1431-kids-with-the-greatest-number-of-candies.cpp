class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> value;
      
        int Max  = *max_element(candies.begin() , candies.end());
         
        for(int i = 0 ; i <candies.size() ;  ++i){
            if(candies[i] + extraCandies >= Max )
                value.push_back(true); 
            else  
                value.push_back(false);
        }
        
        return value;
    }
};