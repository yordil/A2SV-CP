class Solution:
    def fib(self, n: int) -> int:
        
        if n <= 1:
            return n
        
        fibb = [0] * (n+1)
        
        fibb[0] = 0 
        fibb[1] = 1
        
        for i in range(2 , n+1):
            fibb[i] = fibb[i-1] + fibb[i-2]
            
            
        return fibb[n]
    

# using dynamic programming approach we can avoid redundent calculation    
            
            
            
            
            
            
#   my previous cpp implemnation using recursion           
            
#             class Solution {
# public:
#     int fib(int n) {
#         if(n == 0)
#            return 0;
#            else if ( n == 1)
#              return 1;
#              else
#            return fib(n-1) + fib(n-2);
#     }
# };