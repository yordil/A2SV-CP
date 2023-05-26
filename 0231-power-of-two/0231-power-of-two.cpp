class Solution {
public:
    bool isPowerOfTwo(int n) {
        bool x {false};
        
        for(long  i = -31 ; i < 32 ; i++){
             if( n == pow(2 , i) ){
                x = true;
                break;
             }
        }
        return x;
    }
};