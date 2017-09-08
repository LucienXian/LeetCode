class Solution {
public:
    bool judgeCircle(string moves) {
        unordered_map<char, int> c;
        for (char &m : moves)
            ++c[m];
        return c['U'] == c['D'] && c['L'] == c['R'];
    }
};