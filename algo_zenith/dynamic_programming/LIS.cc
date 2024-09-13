#include <bits/stdc++.h>

void solve(){
    vector<int> lis;
    for (int i = 0; i < n; i++){
        if (lis.empty() || lis.back() < arr[i]){
            lis.push_back(arr[i]);
        }else{
            auto it = lower_bound(lis.begin(), lis.end(), arr[i]);
            *it = arr[i]
        }
    }
}

int main(){

}