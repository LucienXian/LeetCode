class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int i = (int)nums.size()-1;
        while(i > 0 && nums[i] <= nums[i-1])
            i--;
        if(i>0){
            i--;
            int last = (int)nums.size()-1;
            while(i < last && nums[last] <= nums[i])
                last--;
            swap(nums[i], nums[last]);
            reverse(nums.begin() + i + 1, nums.end());
        }
        else
            reverse(nums.begin(), nums.end());
    }
};