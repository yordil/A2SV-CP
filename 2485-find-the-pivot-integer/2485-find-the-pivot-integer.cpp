class Solution {
public:
    int pivotInteger(int n) {
        int sumright = 0 , sumleft = 0;
        
        for (int i = 1 ; i <= n ; i++){
            sumleft += i;
            sumright = 0 ;
            for(int j = i ; j <= n ; j++){
                
                sumright +=j  ;
            }
            if(sumleft == sumright)
                return i;
        }
        
        return -1 ;
    }
};