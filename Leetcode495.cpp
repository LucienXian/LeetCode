class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        if(timeSeries.size()==0)
            return 0;
        int count = 0;
        int other = 0;
        for(int i=0;i<timeSeries.size()-1;i++){
            if(timeSeries[i+1]-timeSeries[i]>=duration){
                count += duration;
                other = 0;
            }
            else{
                other = duration-(timeSeries[i+1]-timeSeries[i]);
                count += (duration-other);
            }
        }
        count += duration;
        return count;
    }
};