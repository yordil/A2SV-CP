class Solution {
public:
    vector<long long> sumOfThree(long long num) {
        vector<long long> sum;
         
        if( num % 3 != 0 ){
            return sum;
        }
        
        long long val = num / 3;
           sum.insert(sum.end() , { val -1 , val , val+1});
           
        
           return sum;
            
    }
};