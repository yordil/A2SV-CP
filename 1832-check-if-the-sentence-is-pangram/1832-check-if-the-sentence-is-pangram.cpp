class Solution {
public:
    bool checkIfPangram(string sentence) {
        sort(sentence.begin() , sentence.end());
            int x = 97;
           int ct;
          for(int i = 0 ; i< sentence.size() ; i+=ct){
               ct = count(sentence.begin() , sentence.end() , sentence[i]);
                if( x == sentence[i])
                     x++;
                else
                    return false;
            }
             if( x == 123 )
               return true;
               return false;
        }
    
};