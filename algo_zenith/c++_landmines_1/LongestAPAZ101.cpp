#include <bits/stdc++.h>
using namespace std;
using ll = long long;

void solve()
{
    /* ll n;
    cin >> n;
    ll arr[n];

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    } */
    ll arr[] = {1, 2, 4, 5, 6};
    ll max_len = 2;
    for (int i = 0; i < (sizeof(arr) / sizeof(arr[0])) - 1; i++)
    {
        ll diff = arr[i + 1] - arr[i];
        ll c = 2;
        for (int j = i + 2; j < sizeof(arr) / sizeof(arr[0]); j++)
        {
            if (arr[j] - arr[j - 1] == diff)
            {
                c += 1;
                max_len = max(max_len, c);
            }
            else
            {
                c = 2;
            }
        }
    }
    cout << max_len << "\n";
}

signed main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}

/*
If this is the testcase:
1
5
1 2 4 5 6

Your op:4
Correct op:3

*/