#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void solve() {
    ll n;
    cin >> n;  // Read the value of n first

    vector<ll> arr1(n), arr2(n);  // Use vectors to handle dynamic array size

    for (ll i = 0; i < n; i++) {
        cin >> arr1[i];
    }
    for (ll i = 0; i < n; i++) {
        cin >> arr2[i];
    }

    sort(arr1.begin(), arr1.end());
    sort(arr2.begin(), arr2.end());

    for (ll i = 0; i < n; i++) {
        if (arr1[i] != arr2[i]) {
            cout << "no" << "\n";
            return;  // Exit early if arrays are not equal
        }
    }
    cout << "yes" << "\n";
}

signed main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
