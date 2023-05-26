class Solution {
public:
    bool isPerfectSquare(int num) {
        bool x = {false} ;
        
        if( sqrt(num) == (int)sqrt(num))
            x =true;
        
        return x;
        
    }
};