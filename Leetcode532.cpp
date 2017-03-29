class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        if(nums.size()==0) return 0;
        std::sort(nums.begin(), nums.end());
        int count = 0;
        for(int i = 0; i < nums.size()-1; i++){
            if(nums[i+1]==nums[i]&&k!=0) continue;
            if(nums[i+1]==nums[i]&&k==0){
                count++;
                while(nums[i+1]==nums[i]) i++;
//                j--;
            }
            for(int j = i+1; j < nums.size(); j++){
                if(nums[j]-nums[i]==k) { count++; break; }
                else if(nums[j]-nums[i]>k) break;
            }
        }
        return count;
    }
};