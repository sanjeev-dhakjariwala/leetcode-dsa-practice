#include <bits/stdc++.h>
using namespace std;
using ll = long long;

void merge(int low, int mid, int high, int arr[])
{
    int temp[high - low + 1];
    int i = low, j = mid + 1, k = 0;
    while (i <= mid && j <= high)
    {
        if (arr[i] < arr[j])
        {
            temp[k++] = arr[i];
            i++;
        }
        else
        {
            temp[k++] = arr[j];
            j++;
        }
    }
    while (i <= mid)
    {
        temp[k++] = arr[i];
        i++;
    }
    while (j <= high)
    {
        temp[k++] = arr[j];
        j++;
    }
    for (int i = 0; i < high - low + 1; i++)
    {
        arr[low + i] = temp[i];
    }
}
void mergeSort(int low, int high, int arr[])
{
    if (low < high)
    {
        int mid = low + (high - low) / 2;
        mergeSort(low, mid, arr);
        mergeSort(mid + 1, high, arr);
        merge(low, mid, high, arr);
    }
}
void solve()
{
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    mergeSort(0, n - 1, arr);
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
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