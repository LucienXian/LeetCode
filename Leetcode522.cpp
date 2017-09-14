class Solution {
private:
    bool IsSub(const string& s1, const string& s2){
        int j = 0;
        for (int i = 0; i < s1.size(); i++){
            while(j < s2.size()&&s1[i]!=s2[j]) j++;
            if (j == s2.size()) return false;
            j++;
        }
        return true;
    }    
public:
    int findLUSlength(vector<string>& strs) {
        unordered_map<string, int> s;
        for (int i = 0; i < strs.size(); i++) ++s[strs[i]];
        vector<pair<string,int>> v;
        for(auto it = s.begin(); it != s.end(); ++it)
           v.push_back(*it);
        sort(v.begin(), v.end(), [](pair<string,int> &a, pair<string,int> &b){
            return a.first.size() > b.first.size();
        });
        for (int i = 0; i < v.size(); i++){
            if (v[i].second == 1){
                int j = 0;
                for (;j < i; j++)
                    if (IsSub(v[i].first, v[j].first)) break;
                if (i == j) return v[i].first.size();
            }
        }
        return -1;
    }
};