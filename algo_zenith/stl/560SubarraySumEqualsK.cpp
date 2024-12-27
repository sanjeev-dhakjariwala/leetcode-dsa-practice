#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        map<int, int> mp;
        mp[0] = 1;
        int n = nums.size();
        int prefixSum = 0;
        int ans = 0;
        for(int i = 0; i < n; i++){
            prefixSum += nums[i];
            int temp = prefixSum - k;
            ans += mp[temp];
            mp[prefixSum]++;
        }
        return ans;
    }
};
int main(){
    vector<int> arr = {1, -1, 0, 0};
    int k = 0;
    Solution sol;
    cout << "Ans is "<< sol.subarraySum(arr, k);
    return 0;
}