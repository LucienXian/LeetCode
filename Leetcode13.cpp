class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> T = { { 'I' , 1 }, { 'V' , 5 }, { 'X' , 10 }, { 'L' , 50 }, { 'C' , 100 }, { 'D' , 500 }, { 'M' , 1000 } };
        if(s.empty()) return 0;
        int sum = T[s.back()];
        for(int i=s.length()-2;i>=0;i--)
            sum += (T[s[i+1]]>T[s[i]] ? -T[s[i]]:T[s[i]]);
        return sum;
    }
};