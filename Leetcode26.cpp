class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int begin = 1;
        int l = nums.size();
        if (l<2) return l;
        for (int i = 1; i < l; i++)
            if(nums[i] != nums[i-1])
                nums[begin++] = nums[i];      
        return begin;
    }
};