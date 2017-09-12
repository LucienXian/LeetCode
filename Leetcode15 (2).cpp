class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        std::sort(nums.begin(), nums.end());
        for(int i=0;i<nums.size();i++){
            int target = -nums[i];
            int front = i+1;
            int rear = nums.size()-1;
            while(front<rear){
                int sum = nums[front]+nums[rear];
                if(sum>target)  rear--;
                else if(sum<target) front++;
                else{
                    vector<int> temp;
                    temp.push_back(nums[i]);
                    temp.push_back(nums[front]);
                    temp.push_back(nums[rear]);
                    res.push_back(temp);
                    while(front<rear&&nums[front]==temp[1]) front++;
                    while(front<rear&&nums[rear]==temp[0]) rear--;
                }
            }
            while(i<nums.size()-1&&nums[i]==nums[i+1]) i++;
        }
        return res;
    }
};