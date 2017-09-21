class Solution {
private:
    const string validIPv6Chars = "0123456789abcdefABCDEF";
       bool IsValidIP4(const string& block){
           bool first = true;
           int count = 0;
           int l = block.size();
           if(l>0&&l<4){
               for(char c:block){
                   if(!isdigit(c)||(first&&c=='0'&&l>1))
                       return false;
                   count *= 10;
                   count += c - '0';
               }
               return count <= 255;
           }
           return false;
       }
        bool IsValidIP6(const string& block){
            int l = block.size();
            if (l>0&&l<5){
                for (char c : block)
                    if (validIPv6Chars.find(c) == string::npos) return false;
                return true;
            }
            return false;
        }
public:
    string validIPAddress(string IP) {
        string ans[3] = {"IPv4", "IPv6", "Neither"};
    	stringstream ss(IP);
    	string block;
    	// ipv4 candidate
    	if (IP.substr(0, 4).find('.') != string::npos) {
    	    for (int i = 0; i < 4; i++) {
    		if (!getline(ss, block, '.') || !IsValidIP4(block))
    	   	    return ans[2];
    	    }
    	    return ss.eof() ? ans[0] : ans[2];
    	}
    	// ipv6 candidate
    	else if (IP.substr(0, 5).find(':') != string::npos) {
    	    for (int i = 0; i < 8; i++) {
    		if (!getline(ss, block, ':') || !IsValidIP6(block))
    		    return ans[2];
    	    }
    	    return ss.eof() ? ans[1] : ans[2];
    	}
    
    	return ans[2];
    }
};