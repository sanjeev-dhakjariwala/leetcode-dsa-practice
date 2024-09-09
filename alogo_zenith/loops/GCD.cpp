#include <bits/stdc++.h>
using namespace std;

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int a, b;
    cin >> a >> b;
    if (b > a)
    {
        swap(a, b);
    }
    while (b != 0){
        int temp = b;
        b = a % b;
        a = temp;
    }
    cout << a << "\n";
    return 0;
}