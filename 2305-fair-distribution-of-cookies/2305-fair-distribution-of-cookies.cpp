class Solution {
public:

    void backtrack(int num, vector<int>& cookies, int k, int& ans, vector<int>& count){

        if(num == cookies.size()){
            int maxi = 0;
            for(int i = 0 ; i < k ; i++) maxi = max(maxi, count[i]);
            ans = min(ans, maxi);
            return;
        }
        if(*max_element(count.begin(), count.end()) >= ans) 
            return;

        for(int i = 0 ; i < k ; i++){
            count[i] += cookies[num];
            backtrack(num+1, cookies, k, ans, count);
            count[i] -= cookies[num];
            if(count[i] == 0) 
                break;
        }
    }

    int distributeCookies(vector<int>& cookies, int k) {
        sort(cookies.begin(), cookies.end());
        int ans = INT_MAX;
        vector<int> count(k);

        backtrack(0, cookies, k, ans, count);
        return ans;
    }
};