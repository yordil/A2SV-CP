class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        vector<string> cp = words;
        for(int i= 0 ; i < words.size() ; i++ ){
            reverse(words[i].begin() , words[i].end());
            if(words[i] == cp[i] )
                return words[i];
        }
        
        return "";
    }
};