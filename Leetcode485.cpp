class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max=-1, count = 0;
        for(auto &i:nums){
            if(i==1) count++;
            else count = 0;
            max = max>count ? max:count;
        }
        return max;
    }
};