class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> res;
        for(int i=0;i<nums.size();i++){
            int index = abs(nums[i])-1;
            nums[index] = -1*nums[index];
            if(nums[index]>0) res.push_back(abs(nums[i]));
        }
        return res;
    }
};

class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> res;
        for(int i=0;i<nums.size();i++){
            int index = abs(nums[i])-1;
            if(nums[index]<0) res.push_back(abs(nums[i]));
            nums[index] = -1*abs(nums[index]);
            
        }
        return res;
    }
};