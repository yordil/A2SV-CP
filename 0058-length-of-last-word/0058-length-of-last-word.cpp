class Solution {
public:
    int lengthOfLastWord(string s) {
        int counter{};
        for(int i = s.size() -1;i>= 0  ; --i){
            if( counter > 0 && s[i] ==' ' )
                 break;
            
            if(s[i] ==' ' && counter == 0)
                continue;
            
            else 
                counter++;
             if( counter > 0 && s[i] ==' ' )
                 break;
     }
        
        return counter ;
    }
};