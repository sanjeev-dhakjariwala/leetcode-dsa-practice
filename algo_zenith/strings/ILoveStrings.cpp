#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void solve(){
    string s1, s2;
    cin >> s1;
    cin >> s2;
    ll i = 0;
    ll j = 0;
    string ans = "";
    while (i < s1.size() && j < s2.size()){
        ans += s1[i] + s2[j];
        i++;
        j++;
    }
    while(i < s1.size()){
        ans += s1[i++];
    }
    while(j < s2.size()){
        ans += s2[j++];
    }
    cout << ans << "\n";
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