class Solution {
public:
    int countPrimes(int n) {
       
        if(n< 3)
         return 0;
      
	vector<bool> prime (n, true);
	prime[0] = false ; 
    prime[1] = false;
	
	for(int p = 2 ; p*p < n ; ++p){
		if(prime[p] == false)
			continue;
		  for(int i = 2*p ; i < n ; i +=p){
			  prime[i]=false;
		  }
       
	}
            
       
        
         return count(prime.begin() , prime.end() , true);
}
    
};

// seive implmentation