#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> arr = {1,2,3};
    int n = arr.size();
    for(int i = 0; i < n; i++){
        for(int j = i; j < n; j++){
            for(int k = i; k <= j; k++){
                cout << arr[k] << " ";
            }
            cout << "\n";
        }
    }

    return 0;
}