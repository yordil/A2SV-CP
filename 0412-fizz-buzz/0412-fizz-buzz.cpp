class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> fizb;
        for(int i = 1 ; i <= n ; i++){
            if( i % 3 == 0 && i % 5 ==0 )
            fizb.push_back("FizzBuzz");

            else if( i % 3 == 0 )
            fizb.push_back("Fizz");

           else if( i % 5 == 0 ) 
            fizb.push_back("Buzz");  
            
           else
                fizb.push_back(to_string(i));
          
        }
       return fizb; 
    }
};  