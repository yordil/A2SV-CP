class Solution {
public:
    int maximumNumberOfStringPairs(vector<string>& words) {
        
        int counter = 0 ;
        
        for(int i = 0 ; i < words.size()-1 ; ++i){
            for(int j = i+1 ; j < words.size() ; ++j){
                 string rev  = words[j];
                reverse(rev.begin() , rev.end());
                if(words[i] == rev )
                    counter++;
                
            }
        }
        
        return counter;
    }
};