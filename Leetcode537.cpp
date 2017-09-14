class Solution {
public:
    string complexNumberMultiply(string a, string b) {
        pair<int, int> a_p = parse(a);
        pair<int, int> b_p = parse(b);
        int t = a_p.first*b_p.first - a_p.second*b_p.second;
        int f = a_p.first*b_p.second + a_p.second*b_p.first;
        return to_string(t) + "+" + to_string(f) + "i";
    }
private:
    pair<int, int> parse(const string& n){
        int plus = find(n.begin(), n.end(), '+') - n.begin();
        int i = find(n.begin(), n.end(), 'i') - n.begin();
        int t = stoi(n.substr(0, plus));
        int f = stoi(n.substr(plus+1, i-plus));
        return {t, f};
    }
};