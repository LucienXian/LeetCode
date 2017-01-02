class Solution {
public:
    string longestPalindrome(string s) {
        if(s.empty()) 
            return "";
        int max_len=1,start=0;
        for(int i=0;i<s.size();){
            if(s.size()-i<=max_len/2) break;
            int left=i, right=i;
            while(right<s.size()-1&&s[right]==s[right+1])//skip the same characters
                right++;
            i=right+1;
            while(right<s.size()-1&&left>0&&s[left-1]==s[right+1]){
                right++;
                left--;
            }
            int new_len = right-left+1;
            if(new_len>max_len){
                start = left;
                max_len = new_len;
            }
        }
        return s.substr(start, max_len);
    }
};