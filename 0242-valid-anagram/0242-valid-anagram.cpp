class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin() , s.end());
        sort(t.begin() , t.end());
       // int len1 =  , len2 =  ;
          if(t.size() !=s.size())
              return false;
        
           if( s != t)
               return false;
               
        
        return true;
    }
};