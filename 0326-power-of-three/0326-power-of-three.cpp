class Solution {
public:
    bool isPowerOfThree(int n) {
        bool x = false;

        for(int i = -31 ; i < 32 ; i++ ){
            if( n == pow(3 , i)){
                x = true;
                break;
            }
        }
        return x;
    }
};