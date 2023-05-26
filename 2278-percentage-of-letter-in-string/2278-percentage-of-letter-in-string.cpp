class Solution {
public:
    int percentageLetter(string s, char letter) {
        float len = s.size();
        float counter = count(s.begin() , s.end() , letter);
        float x = (counter*100)/len; 

        return x;
    }
};