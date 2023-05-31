class Solution {
public:
    int commonFactors(int a, int b) {
        int factor = 0;
          int len;
          if( a <= b )
              len = a;
           else 
               len=b;
        for(int i = 1 ;  i <= len ; i++){
            if( a % i == 0 && b % i == 0)
                factor++;
        }
        
        return factor;
              
    }
};