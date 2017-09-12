class Solution {
public:
    string reverseStr(string s, int k) {
        int l = s.size();
        int i = 0;
        while (i < l){
            if (i+2*k<l||(i+2*k>=l&&i+k<l)) reverse(s.begin()+i, s.begin()+i+k);
            else if (i + k >= l) {reverse(s.begin()+i, s.end()); break;}
            i += 2*k;
        }
        return s;
    }
};