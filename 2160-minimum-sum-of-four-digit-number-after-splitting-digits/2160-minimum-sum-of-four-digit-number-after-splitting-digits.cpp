class Solution {
public:
    int minimumSum(int num) {
        vector<int> dig;
        int r;
        while(num != 0){
            
            r = num % 10;
            dig.emplace_back(r);
            
            num /=10;
            
        }
        
          sort(dig.begin() , dig.end());
        
          return (dig[0]*10 + dig[3] + dig[1]* 10 + dig[2]) ;
    }
}; 