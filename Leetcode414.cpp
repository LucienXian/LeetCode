class Solution {
public:
    int thirdMax(vector<int>& nums) {
        long a, b, c;
        a = b = c = LONG_MIN;
        for(auto &i:nums){
            if(i<=c||i==a||i==b) continue;
            c = i;
            if(c>b) swap(c, b);
            if(b>a) swap(b, a);
        }
        if(c==LONG_MIN) return a;
        else return c;
    }
};