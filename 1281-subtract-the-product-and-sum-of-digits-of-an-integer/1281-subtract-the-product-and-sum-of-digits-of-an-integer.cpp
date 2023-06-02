class Solution {
public:
    int subtractProductAndSum(int n) {
        int pro = 1 , sum = 0; 
        do{
            int num = n %10;
            pro *= num;
            sum +=num;
            
            n /=10 ;
        }while(n != 0);
        
        return pro - sum;
    }
};