#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void solve(){
    ll n;
    cin >> n;
    ll arr[n];

    for(ll i = 0; i < n; i++){
        cin >> arr[i];
    }
    ll min = arr[0];
    ll freq = 1;
    for(ll i = 1; i < n; i++){
        if (min > arr[i]){
            freq = 0;
            min = arr[i];
        }
        if(arr[i] == min){
            freq += 1;
        }
        
    }
    if (freq % 2 == 1){
        cout << "Lucky" << "\n";
    }else{
        cout << "Unlucky" << "\n";
    }
}

signed main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}