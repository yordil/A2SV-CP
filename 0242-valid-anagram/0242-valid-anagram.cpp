class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin() , s.end());
        sort(t.begin() , t.end());
        int len1 = t.size() , len2 = s.size() ;
          if(len1 != len2)
              return false;
        for(int i = 0 ; i <  len1 ; i++){
           if( s[i] != t[i])
               return false;
               
        }
        return true;
    }
};