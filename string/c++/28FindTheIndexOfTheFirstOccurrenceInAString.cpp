#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int strStr(string haystack, string needle)
    {
        if (haystack.length() < needle.length())
        {
            return -1;
        }

        for (int i = 0; i <= haystack.length() - needle.length(); i++)
        {
            string temp = haystack.substr(i, needle.length());
            if (temp == needle)
            {
                return i;
            }
        }

        return -1;
    }
};

signed main()
{
    Solution sol;
    cout << sol.strStr("hello", "ll") << "\n";
}