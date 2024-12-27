#include<bits/stdc++.h>
using namespace std;
#define int long long
map<int,int> mp;
vector<int> b;
int n = 3;
void rec(int level){
	if(level == n){
		for(int i = 0; i < n; i++){
			cout << b[i] << " ";
		}
		cout << "\n";
		return;
	}
	for(auto&it: mp){
		if(it.second != 0){
			b.push_back(it.first);
			it.second--;
			rec(level + 1);
			it.second++;
			b.pop_back();
		}
	}
}
void solve(){
	//cin >> n;
	vector<int> a = {2,1,3};
	for(int i = 0; i < n; i++){
		//cin >> a[i];
		mp[a[i]]++;
	}
	rec(0);
}
signed main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);cout.tie(0);
	solve();
	return 0;
}