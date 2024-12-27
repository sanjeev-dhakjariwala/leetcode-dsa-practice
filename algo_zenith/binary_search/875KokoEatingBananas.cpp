#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int check(int mid, int h, vector<int>& arr){
        int n = (int)arr.size();
        int t = 0;
        for(int i = 0; i < n; i++){
            t += ceil((1.0 *  arr[i]) / mid);
        }
        return t <= h;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int n = (int) piles.size();
        sort(piles.begin(), piles.end());
        int low = 1;
        int high = piles[n - 1];
        int ans = -1;
        while(low <= high){
            int mid = low + (high - low) / 2;
            if(check(mid, h, piles)){
                ans = mid;
                high = mid - 1;
            }else{
                low = mid + 1;
            }
        }
        return ans;
    }
};
int main(){
    Solution sol;
    vector<int> piles = {312884470};
    int h = 968709470;
    cout << sol.minEatingSpeed(piles, h);
    return 0;
}