class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        setprecision(6);
       vector<double> conv {273.15 + celsius , celsius*1.80 + 32.00};
        return conv;
    } 
};