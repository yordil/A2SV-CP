class Solution {
public:
    int alternateDigitSum(int n) {
        int r , sum =0;
        vector<int> dig;
        while(n !=0){
            
            r = n % 10;
            dig.emplace_back(r);
            n /= 10;
        }
        
         reverse(dig.begin() , dig.end());
        
        for( int i = 0 ; i < dig.size(); i++){
             if( i %2 ==0)
                 sum += dig[i];
            else
                sum -=dig[i];
           
        }
        
        return sum;
    }
};