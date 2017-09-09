class Solution {
public:
    vector<vector<string>> findDuplicate(vector<string>& paths) {
        unordered_map<string, vector<string>> files;
        vector<vector<string>> res;
        for (auto path : paths){
            stringstream ss(path);
            string root;
            string s;
            getline(ss, root, ' ');
            while(getline(ss, s, ' ')){
                string filename = root + '/' + s.substr(0, s.find('('));
                string content = s.substr(s.find('(')+1, s.find(')') - s.find('(') - 1);
                files[content].push_back(filename);
            }
        }
        for (auto file:files){
            if(file.second.size()>1)
                res.push_back(file.second);
        }
        return res;
    }
};