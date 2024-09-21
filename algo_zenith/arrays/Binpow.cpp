#include <bits/stdc++.h>
#define int long long
using namespace std;

int binpow(int x, int n)
{
    if (n == 0)
    {
        return 1;
    }
    if (n % 2 == 1)
    {
        return x * binpow(x, n - 1);
    }
    else
    {
        int temp = binpow(x, n / 2);
        return temp * temp;
    }
}
signed main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int x, n;
    cin >> x >> n;
    cout << binpow(x, n) << "\n";
}