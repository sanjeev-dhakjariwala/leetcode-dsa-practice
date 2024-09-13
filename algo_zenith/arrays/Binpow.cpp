#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll binpow(ll x, ll y)
{
    if (y == 0)
    {
        return 1;
    }
    if (y % 2 == 1){
        ll temp = binpow(x, y - 1);
        return x * temp;
    }else{
        ll temp = binpow(x, y / 2);
        return temp * temp;
    }
}
signed main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    /* ll x, y;
    cin >> x;
    cin >> y; */
    cout << binpow(2, 3);
    return 0;
}