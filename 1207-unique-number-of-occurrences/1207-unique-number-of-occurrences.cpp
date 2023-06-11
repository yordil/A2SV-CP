class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        sort(arr.begin() , arr.end());
        vector<int>value;
        int x;
        for(int i =  0 ; i < arr.size() ; i += x){
           x =  count(arr.begin() , arr.end(), arr[i]);
            
            value.emplace_back(x);
            
        }
        sort(value.begin() , value.end());
        for(int i = 0 ; i < value.size() -1  ; i++){
            if(value[i] == value[i+1] ){
                return false;
            }
        }
        
        return true;
    }
};