class Solution {
public:
    int countSubstrings(string s) {
        int res = 0;
        int l = s.length();
        for (int i = 0; i < l; i++){
            for(int j = 0; i>=j&& i+j < l && s[i-j]==s[i+j];j++) res++;
            for(int j = 0; i>=j&& i+j < l && s[i-j]==s[i+j+1];j++) res++;
        }
        return res;
    }
};