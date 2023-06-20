class Solution {
public:
    bool isPalindrome(int x) {
        string  num = to_string(x);
        string num1 = num;
        reverse(num.begin() , num.end());
        if(num == num1)
            return  true;
        return false;
    }
};