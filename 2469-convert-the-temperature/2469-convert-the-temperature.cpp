class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        setprecision(6);
        
        double kelvin = celsius + 273.15 ; 
        double far = celsius * 1.80 +32 ;
        
        vector <double> ret = {kelvin , far};
        
        return ret;
        
    }
    
    
};