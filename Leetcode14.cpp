class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string com="";
        for(int i=0;strs.size()>0;com+=strs[0][i++])
            for(int j=0;j<strs.size();j++)
                if(i>=strs[j].size()||strs[j][i]!=strs[0][i]) return com;
        return com;
    }
};