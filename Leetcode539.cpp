class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        int len = timePoints.size();
        if (len > 1440) return 0;
        vector<int> time;
        for (int i = 0; i < len; i++) time.push_back(to_min(timePoints[i]));
        sort (time.begin(), time.end());
        int res = time[0] + 1440 - time[len-1];
        for (int i = 1; i < len; i++)
            res = min(res, time[i] - time[i-1]);
        return res;
    }
private:
    int to_min(string& t){
        int h = (t[0]-'0')*10 + (t[1] - '0');
        int m = (t[3]-'0')*10 + (t[4] - '0');
        return h*60 + m;
    }
};