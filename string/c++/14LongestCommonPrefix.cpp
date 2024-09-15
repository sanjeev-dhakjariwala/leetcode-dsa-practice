#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
    
        // Take the first string as the reference
        string prefix = strs[0];
        
        for (int i = 1; i < strs.size(); ++i) {
            // Compare the current prefix with the next string
            while (strs[i].find(prefix) != 0) {
                // Reduce the prefix length until we find a common prefix
                prefix = prefix.substr(0, prefix.size() - 1);
                if (prefix.empty()) return "";
            }
        }
        
        return prefix;
    }
};

signed main(){
    Solution sol;
    vector<string> arr = {"flower","flow","flight"};
    cout << sol.longestCommonPrefix(arr);
}