class Solution {
public:
    int nextGreaterElement(int n) {
        string s = to_string(n);
        int len = s.size();
        int i = len - 1;
        while (i>0 && s[i]<=s[i-1]) i--;
        if (i == 0) return -1;
        for(int j = len-1; j >= i ; j--){
            if (s[j]>s[i-1]) {
                swap(s[j], s[i-1]);
                break;
            }
        }
        sort(s.begin()+i, s.end());
        return stol(s) > INT_MAX ? -1 : stol(s);;
    }
};