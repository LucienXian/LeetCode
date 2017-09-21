class Solution {
public:
    bool repeatedSubstringPattern(string str) {
        int l = str.length();
        for (int i = 1; i <= l/2; ++i)
        {
        	if (l%i==0&&str.substr(i)==str.substr(0, l-i))
        		return true;
        }
        return false;
    }
};

class Solution {
public:
    bool repeatedSubstringPattern(string str) {
        int l = str.length();
        string temp(str+str);
        temp = temp.substr(1, 2*l-2);
        return temp.find(str) != string::npos;
    }
};