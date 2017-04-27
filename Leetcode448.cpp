class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> temp(nums.size()+1,0);
        for(int i=0;i<nums.size();i++){
            temp[nums[i]] = 1;
        }
        vector<int> ret;
        for(int i=1;i<temp.size();i++)
            if(!temp[i]) ret.push_back(i);
        return ret;
    }
};