#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int sumSubarrayMins(vector<int> &arr)
    {
        int n = arr.size();
        long long ans = 0;
        vector<int> left(n), right(n);
        stack<int> st;

        // Calculate left boundaries
        for (int i = 0; i < n; i++)
        {
            while (!st.empty() && arr[st.top()] > arr[i])
            {
                st.pop();
            }
            left[i] = st.empty() ? -1 : st.top();
            st.push(i);
        }

        // Clear stack for the right boundaries calculation
        while (!st.empty())
            st.pop();

        // Calculate right boundaries
        for (int i = n - 1; i >= 0; i--)
        {
            while (!st.empty() && arr[st.top()] >= arr[i])
            {
                st.pop();
            }
            right[i] = st.empty() ? n : st.top();
            st.push(i);
        }
        // Calculate the sum of subarray minimums
        for (int i = 0; i < n; i++)
        {
            int l = (i - left[i]);
            int r = (right[i] - i);
            ans += (long long) l * r * arr[i];
            ans %= 1000000007; // to avoid overflow
        }
        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> arr = {3, 1, 2, 4};
    cout << sol.sumSubarrayMins(arr) << "\n";
    return 0;
}