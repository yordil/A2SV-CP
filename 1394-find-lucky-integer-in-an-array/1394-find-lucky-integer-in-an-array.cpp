class Solution {
public:
    int findLucky(vector<int>& arr) {
        
        int lucky = -1;
        int x = 0;
        sort(arr.begin() , arr.end());
        
        for(int i = 0 ; i <  arr.size() ; i+=x){
             x = count(arr.begin() , arr.end() , arr[i]);
            if (arr[i] == x )
                lucky = x;
        }
        
        return lucky;
    }
};