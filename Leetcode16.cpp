class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int closest = nums[0]+nums[1]+nums[2];
        std::sort(nums.begin(), nums.end());
        int i=0;
        if(nums[i]+nums[i+1]+nums[i+2]>=target)
            return nums[i]+nums[i+1]+nums[i+2];
        if(nums[nums.size()-1]+nums[nums.size()-2]+nums[nums.size()-3]<target)
             return nums[nums.size()-1]+nums[nums.size()-2]+nums[nums.size()-3];
        for(;i<nums.size(); i++){
            int front = i+1;
            int rear = nums.size()-1;
            while(front<rear){
                int temp = nums[i]+nums[front]+nums[rear];
                if(temp==target) return temp;
                if(abs(temp-target)<abs(closest-target))
                    closest = temp;
                if(temp<target) front++;
                else rear--;
            }
        }
        return closest;
    }
}