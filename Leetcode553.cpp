class Solution {
public:
    string optimalDivision(vector<int>& nums) {
        if (!nums.size()) return "";
        string res = to_string(nums[0]);
        if (nums.size() == 1) return res;
        if (nums.size() == 2) return res + "/" + to_string(nums[1]);
        res += "/(";
        for (int i = 1; i < nums.size()-1; i++){
            res += to_string(nums[i]);
            res += "/";
        }
        res += to_string(nums[nums.size()-1]) + ")";
        return res;
    }
};